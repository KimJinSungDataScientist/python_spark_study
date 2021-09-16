
def sayHello():
    print('hello')
    
def getKey(keypath):
    d=dict()
    f=open(keypath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d
