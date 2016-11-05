from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from languageMods.models import Language, Report
import utils

def ReportForm (request, lang):
    DB = Language.objects.filter (language=lang)
    titlereport=""
    pathName=""
    reportdescription=""
    obstacleevaluation=""
    send=""
    delete=""
    for language in DB:
        if language.campo=="titlereport":
            titlereport=language.text
        elif language.campo=="pathName":
            pathName=language.text
        elif language.campo=="reportdescription":
            reportdescription=language.text
        elif language.campo=="obstacleevaluation":
            obstacleevaluation=language.text
        elif language.campo=="send":
            send=language.text
        elif language.campo=="delete":
            delete=language.text
    template=loader.get_template('report/reportForm.html')
    defDescription=""
    defEvaluation=""
    defPathName="i.e. O101 o Sentiero Maestro Enrico Albertini"
    reportModyBool=False
    extension='main/mainPage.html'
    extensionCSS='report/reportForm.css'
    context = {
        'lang': lang,
        'titlereport' : titlereport,
        'pathName' : pathName,
        'reportdescription' : reportdescription,
        'obstacleevaluation' : obstacleevaluation,
        'send' : send,
        'delete' : delete,
        'defDescription' : defDescription,
        'defEvalutation' : defEvaluation,
        'defPathName' : defPathName,
        'reportMody' : reportModyBool,
        'extension' : extension,
        'extensionCSS' : extensionCSS,
    }
    return (HttpResponse( template.render(context, request)))

def ReportPage (request, lang):
    DB = Language.objects.filter (language=lang)
    template=loader.get_template('report/report.html')
    extension = 'main/mainPage.html'
    extensionCSS = 'report/report.css'
    context = {
        'DB': DB,
        'lang': lang,
        'extension': extension,
        'extensionCSS': extensionCSS,
    }
    return (HttpResponse( template.render(context, request)))

def getReport (request, lang):
    Evaluation=""
    PathName=""
    Description=""
    pathnameBool=True
    descriptionBool=True
    evaluationBool=True
    template=False
    report=Report()
    DB=Language.objects.filter(language=lang)
    if request.method=='POST':
        #CONTROLLO CHE TUTTI I CAMPI VADANO BENE
        if (utils.empty(request.POST.get('description', 'Fake description')) or len(request.POST.get('description', 'Fake description'))==0 or request.POST.get('description', 'Fake description')=='Fake description' or request.POST.get('description', 'Fake description')=='      '):
            descriptionBool=False
        else:
            Description=utils.getImportant(request.POST.get('description', 'Fake description'))
        if (request.POST.get('evaluation', 'Fake evaluation')=='' or request.POST.get('evaluation', 'Fake evaluation')=='Fake evaluation'):
            evaluationBool=False
        else:
            try:
                evaluationapp=int(request.POST.get('evaluation', 'Fake evaluation'))
            except:
                evaluationBool=False
            if evaluationBool:
                if (evaluationapp>10 or evaluationapp<0):
                    evaluationBool=False
                else:
                    Evaluation=utils.getImportant(request.POST.get('evaluation', 'Fake evaluation'))
        if (utils.empty(request.POST.get('pathname', 'Fake path\'s name')) or len(request.POST.get('pathname', 'Fake path\'s name'))==0 or request.POST.get('pathname', 'Fake path\'s name')=='Fake path\'s name'):
            pathnameBool=False
        else:
            PathName=request.POST.get('pathname', 'Fake path\'s name')
        #print('pathnameBool: '+str(pathnameBool)+'     pathname: '+PathName+
        #    '\ndescriptionBool: '+str(descriptionBool)+'       description: '+Description+
        #    '\nevaluationBool: '+str(evaluationBool)+'        evaluation: '+request.POST.get('evaluation', 'Fake path\'s name')+'      len: '+str(len(request.POST.get('evaluation', 'Fake path\'s name'))))
        if (not(pathnameBool) or not(descriptionBool) or not(evaluationBool)):
            template=loader.get_template('report/reportError.html')
            extension = 'main/mainPage.html'
            extensionCSS = 'report/reportError.css'
            context = {
                'DB' : DB,
                'lang' : lang,
                'PathName' : PathName,
                'Description' : Description,
                'Evaluation' : Evaluation,
                'pathnameBool' : pathnameBool,
                'descriptionBool' : descriptionBool,
                'evaluationBool' : evaluationBool,
                'extension' : extension,
                'extensionCSS' : extensionCSS,
            }
            return HttpResponse (template.render (context, request))
        KEY=utils.generateKEY(Description)
        try:
            Report.objects.create(description=Description, evaluation=Evaluation, pathName=PathName, KEY=KEY)
        except :
            return HttpResponse ('Report gia\' esistente')
        report=Report.objects.get(description=Description, evaluation=Evaluation, pathName=PathName, KEY=KEY)
        template=loader.get_template('report/reportSent.html')
        extension = 'main/mainPage.html'
        extensionCSS = 'report/reportSent.css'
        context = {
            'report' : report,
            'DB' : DB,
            'reportID' : report.id,
            'reportKEY' : report.KEY,
            'lang' : lang,
            'extension': extension,
            'extensionCSS': extensionCSS,
        }
        #return HttpResponse ('Report Sent')
        return HttpResponse (template.render (context, request))
    else:
        return HttpResponse ("Bad transition method")

def reportMody (request, lang):
    template=loader.get_template('report/reportForm.html')
    langDB = Language.objects.filter (language=lang)
    titlereport=""
    pathName=""
    reportdescription=""
    obstacleevaluation=""
    send=""
    delete=""
    for language in langDB:
        if language.campo=="titlereport":
            titlereport=language.text
        elif language.campo=="pathName":
            pathName=language.text
        elif language.campo=="reportdescription":
            reportdescription=language.text
        elif language.campo=="obstacleevaluation":
            obstacleevaluation=language.text
        elif language.campo=="send":
            send=language.text
        elif language.campo=="delete":
            delete=language.text
    if request.method=='POST':
        ID=request.POST.get('reportid', '')
        KEY=request.POST.get('reportkey', '')
        if (not len(KEY)==10):
            KEY=utils.getImportant(KEY)
        try:
            report = Report.objects.get (id=ID, KEY=KEY)
        except:
            return HttpResponse ('No corrisponding report. Already deleted?')
        defDescription=report.description
        defEvaluation=report.evaluation
        defPathName=report.pathName
        reportModyBool=True
        extension = 'main/mainPage.html'
        extensionCSS = 'report/reportForm.css'
        context = {
            'lang': lang,
            'titlereport' : titlereport,
            'pathName' : pathName,
            'reportdescription' : reportdescription,
            'obstacleevaluation' : obstacleevaluation,
            'send' : send,
            'delete' : delete,
            'reportid' : ID,
            'reportkey' : KEY,
            'defDescription' : defDescription,
            'defEvaluation' : defEvaluation,
            'defPathName' : defPathName,
            'reportMody' : reportModyBool,
            'extension': extension,
            'extensionCSS': extensionCSS,
        }
        return (HttpResponse( template.render(context, request)))
    else:
        return HttpResponse ('Bad transistion method')

def reportModified(request, lang):
    if request.method=='POST':
        app=request.POST.get ('delete', 'NO DELETE')
        DELETE=False
        SEND=False
        if (app!='NO DELETE'):
            DELETE=True
        else:
            app=request.POST.get('send', 'NO SEND')
            if (app=='NO SEND'):{}
            else:
                SEND=True
        ID=request.POST.get('reportid', 'Fake report id')
        KEY=request.POST.get('reportkey', 'Fake report key')
        pathname=request.POST.get('pathname', 'Fake path\'s name')
        description=utils.getImportant(request.POST.get('description', 'Fake description'))
        evaluation=request.POST.get('evaluation', 'Fake evaluation')
        print ("id: "+str(ID))
        print ('globalKEY: '+KEY)
        Report.objects.filter(KEY=KEY, id=ID).delete()
        if SEND:
            KEY=utils.generateKEY(description)
            Report.objects.create(pathName=pathname, description=description, evaluation=evaluation, KEY=KEY)
            ID=(Report.objects.get(pathName=pathname, description=description, evaluation=evaluation, KEY=KEY)).id
            return HttpResponse ("Report modified.New ID: "+str(ID)+"New Key: "+KEY)
        elif DELETE:
            return HttpResponse ("Report deleted")
        else:
            return HttpResponse ("Something's wrong")
    else:
        return HttpResponse ("Bad transition method")
