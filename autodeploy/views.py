from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

PATH = '/var/www/pinewood-mountainservice'

@csrf_exempt
def hook_handler(request):

    if request.method == 'POST':
        '''
        in order the operation to be performed are:
            1 check payload for branch name if corrisponds
                1 pull from github done
                2 make migrations
                3 migrate
                4 reload source code
        '''
        import json
        import re

        github_post = json.loads(request.body.decode("utf-8")) #FIXME there could be no json object
        if "ref" in github_post:
            pushed_branch = re.search("^.{1,}\/.{1,}\/(.{1,})$", github_post['ref']).group(1) #TODO use compiled regex instead
            print(pushed_branch)
            from subprocess import call, check_output, Popen
            import os

            out = check_output(["git", "--git-dir={}".format(os.path.join(PATH)), "--work-tree={}".format(PATH),  "branch"]) #FIXME find why the server has troubles while running git commands, it seems to be in the right directory and as the right user
            actual_branch = re.search("^\* (.{1,})$", out.decode("utf-8")).group(1)

            if actual_branch == pushed_branch:
                res1 = check_output(["git", "--git-dir={}".format(os.path.join("{}/.git".format(PATH))), "--work-tree={}".format(PATH), "pull", "origin", actual_branch])

                res2 = check_output(['{}/manage.py'.format(PATH), 'makemigrations', 'base'])
                res3 = check_output(['{}/manage.py'.format(PATH), 'migrate'])

                res4 = call(['sudo', 'service', 'apache2.service', 'reload']) #WARNING this could be harmful, verify that is really github posting

                return HttpResponse("{} </br> {} </br> {} </br> {}".format(res1, res2, res3, res4))
            return HttpResponse("Nothing to do here")
    return HttpResponse('this link is used to update the git repo')
