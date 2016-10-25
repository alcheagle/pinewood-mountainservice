from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json, os, sys

PATH                    = '/var/www/pinewood-mountainservice'
CONFIG_FILE_NAME        = '.config.json'
CONFIG_FILE             = os.path.join(sys.path[0], CONFIG_FILE_NAME)
REQUIRE_GITHUB_SECRET   = True

@csrf_exempt
def hook_handler(request):
    #verify with secret from github
    if os.path.isfile(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as config_file:
            config = json.loads(config_file)

        import hmac, hashlib
        digest = hmac.new(config["SECRET"], msg=request.body, digestmod=hashlib.sha1)
        verified = hmac.compare_digest(request.META['HTTP_X_HUB_SIGNATURE'], digest)
    else:
        verified = not REQUIRE_GITHUB_SECRET 

    if verified and request.method == 'POST':
        '''
        in order the operation to be performed are:
            1 check payload for branch name if corrisponds
                1 pull from github done
                2 make migrations
                3 migrate
                4 reload source code
        '''
        import re

        github_post = json.loads(request.body.decode("utf-8")) #FIXME there could be no json object

        if "ref" in github_post:
            GIT_COMMAND = ["git", "--git-dir={}/.git".format(os.path.join(PATH)), "--work-tree={}".format(PATH)]
            MANAGE_COMMAND = ['{}/manage.py'.format(PATH)]

            pushed_branch = re.search("^.{1,}\/.{1,}\/(.{1,})$", github_post['ref']).group(1) #TODO use compiled regex instead
            print(pushed_branch)
            from subprocess import call, check_output, Popen

            out = check_output(GIT_COMMAD + ["branch"]) #FIXME find why the server has troubles while running git commands, it seems to be in the right directory and as the right user
            actual_branch = re.search("^\* (.{1,})$", out.decode("utf-8")).group(1)

            if actual_branch == pushed_branch:
                #check if the server is already up-to-date
                res1 = check_output(GIT_COMMAND + ["pull", "origin", actual_branch])

                res2 = check_output(MANAGE_COMMAND + ['makemigrations'])
                res3 = check_output(MANAGE_COMMAND + ['migrate'])

                res4 = call(['sudo', 'service', 'apache2.service', 'reload']) #WARNING this could be harmful, verify that is really github posting

                return HttpResponse("{} </br> {} </br> {} </br> {}".format(res1, res2, res3, res4))
            return HttpResponse("Nothing to do here")
    raise Http404