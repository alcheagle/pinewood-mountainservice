import random, time

def null (c):
    print(ord(c))
    if c==' ' or c=='\0' or c=='\n' or c=='\r' or c=='\t' or c==None:
        return True
    else:
        return False

def getImportant (string):
    print 'bkhhkoh!'
    i=0
    while null(string[i]):
        print(ord(string[i]))
        i=i+1
    return string[i:]

def empty (string):
    for c in string:
        if not(null(c)):
            return False
    return True

def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1)+fib(n-2)

def generateKEY (description):
    casuale='\-]JP}HQ\LC}orC?n"l63kuS_SIHVt'
    unoApp=random.randint(1, 10)
    uno=random.randint(1, unoApp*9)
    if (uno>9):
        uno=uno%10
    dueApp=(random.randint (1, unoApp*10))%25
    due=str(chr(dueApp + ord('a')))
    treApp=int(time.time())
    i=10
    tre=0
    while i>0:
        n=random.randint(1, 10)
        pot=pow(10, n)
        if treApp < pot:
            i=i-1
        else:
            tre=int((treApp%pot)/pow(10, (n-1)))
    if (i==0):
        if treApp < 100:
            tre=int(treApp%10)
        else:
            tre=int((treApp%100)/10)
    if uno==tre and tre==9:
        quattro=random.randint((uno if uno<tre else tre), ((tre if tre>uno else uno)+1))
    elif uno==tre and tre==0:
        quattro=random.randint(((uno if uno<tre else tre)-1), (tre if tre>uno else uno))
    else:
        quattro=random.randint((uno if uno<tre else tre), ((tre if tre>uno else uno)))
    cinqueApp=description[random.randint(0, len(description)-1)]
    while cinqueApp == ' ':
        cinqueApp = description[random.randint(0, len(description)-1)]
    cinque=cinqueApp
    seiApp = ord(cinque)
    while seiApp>9:
        seiApp=int((seiApp%10+random.randint(0, uno)))
    sei=seiApp
    setteApp=fib(random.randint(tre if tre<quattro else quattro, (quattro if quattro > tre else tre)+1))
    while setteApp>9:
        setteApp=setteApp % 6
    sette=setteApp
    ottoApp=random.randint(0, 3)
    ottoAppapp=int((random.randint(1, 10)*ottoApp))
    otto=casuale[ottoAppapp if ottoAppapp!=30 else 29]
    nove=random.randint(0, 9)
    dieci=random.randint(0, 9)
    return (str(uno)+str(due)+str(tre)+str(quattro)+str(cinque)+str(sei)+str(sette)+str(otto)+str(nove)+str(dieci))
