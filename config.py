config={'fileName':'phoneBook.csv','registrFree':'on','telMask':'on'}

def getConfig():
    global config
    return config

def convertToStr():
    global config
    str=[]
    for key,value in config.items():
        str.append(f'{key}={value}\n')
    # str[-1]=str[-1][:-2]
    return str

def update (key,val):
   global config
   config[key]=val

def onOff(key):
    global config
    if config[key]=='on':
        return 'off'
    else:
        return 'on'

def convertFromStr (strings):
    global config
    for s in strings:
        key,val=s.replace('\n','').split('=')
        config[key]=val
