fileBase='phoneBook.csv'
configBase='config.txt'

def loadBase():
    global fileBase
    try:
        with open (fileBase,'r',encoding='UTF-8') as f:
            str=f.readlines()
    except:
        return False
    return str

def saveBase(phoneBook):
    global fileBase
    with open (fileBase,'w',encoding='UTF-8') as f:
        f.writelines(phoneBook)
def saveConfig(Config):
    global configBase
    with open(configBase, 'w', encoding='UTF-8') as f:
        f.writelines(Config)

def loadConfig():
    global configBase
    try:
        with open (configBase,'r',encoding='UTF-8') as f:
            str=f.readlines()
    except:
        return False
    return str