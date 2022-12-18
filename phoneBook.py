

phoneBook=[]
def find(strToFind:str,config):
    global phoneBook
    ids=[]
    if config['registrFree']=='on':
        strToFind=strToFind.lower()
    for j,contact in enumerate(phoneBook):
        for i in range(0,3):
            if config['registrFree'] == 'on':
                contact[i] = contact[i].lower()
            if strToFind in contact[i]:
                ids.append(j)
    return list(set(ids))

def editContact(id,type,newVal):
    global phoneBook
    phoneBook[id][type]=newVal

def addContact(contact):
    global phoneBook
    phoneBook.append(contact)

def delID(id):
    global phoneBook
    del phoneBook[id-1]

def convertToStr ()->str:
    global phoneBook
    str=[]
    for contact in phoneBook:
        str.append(';'.join(contact)+'\n')
    str[-1]=str[-1][:-2]
    return str

def convertFromStr (strings):
    global phoneBook
    phoneBook.clear()
    for s in strings:
        phoneBook.append(s.replace('\n','').split(';'))
