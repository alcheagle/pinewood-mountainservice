import os
from languageMods.models import * 
def func ():
    try:
        FILE=open ("./languagedb.txt", "r")
    except IOError:
        print 'Can\'t open db file'
        exit (1)
    for line in FILE:
        language=line[0 : 2]
        fieldBool=True
        i=4
        while fieldBool:
            c=line[i]
            if c != '|':
                i=i+1
            else:
                fieldBool=False
        field=line[3:i]
        #textBool=True
        #a=0
        # while textBool:
        #     try:
        #         c=values[a]
        #     except:
        #         print ''
        #     if c != '\'':
        #         text=text+str(c)
        #         a=a+1
        #     else:
        #         textBool=False
        text=line[i+1:]
        #print (language+" | "+field+" | "+text)
        Language.objects.create(language=language, text=text, campo=field)
            #print os.popen(comand).read()
