from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from languageMods.models import Language, Report


def IndexPage (request, lang):
    DB = Language.objects.filter(language=lang)
    extension='main/mainPage.html'
    extensionCSS='languageMods/index.css'
    template=loader.get_template('languageMods/index.html')
    context = {
        'DB': DB,
        'lang': lang,
        'extension' : extension,
        'extensionCSS' : extensionCSS
    }
    return (HttpResponse( template.render(context, request)))
