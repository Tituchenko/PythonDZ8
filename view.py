def showFinded(ids,phoneBook):
    for i,contact in enumerate(phoneBook):
        if i in ids:
            print (i+1,*contact)
    if len(ids) == 0:
        print ('Не найдено!')

def findInput():
    findString=input ('Введите текст для поиска: ')
    return findString


def editContact (phoneBook):
    while True:
        try:
            id = int(input('Введите номер пункта для редактирования, 0 - отмена: '))
            if id==0:
                return None,None,None
            if id in range(1, len(phoneBook) + 1):
                id-=1
                print(f'1.Имя: {phoneBook[id][0]}')
                print(f'2.Телефон: {phoneBook[id][1]}')
                print(f'3.Комментарий: {phoneBook[id][2]}')
                print(f'0.Отмена, выбрать другую запись.')
                while True:
                    try:
                        whatEdit=int(input ('Введите то что Вы хотите изменить'))
                        if whatEdit in range (0,4):
                            if not whatEdit==0:
                                newVal=input ('Введите новое значение: ')
                                return id,whatEdit-1,newVal
                            else:
                                break
                        else:
                            print ('Выберите пункт 0-3!')
                    except:
                        print('Некорректный пункт!')
            else:
                print('Нет такого пункта!')
        except:
            print('Некорректный пункт!')



def addContact():
    name=input('Введите имя: ')
    phone=input('Введите телефон: ')
    comment=input ('Введите комментарий: ')
    return name,phone,comment

def confirm (text):
    print (text)
    while True:
        conf=input()
        if conf=='y':
            return True
        elif conf=='n':
            return False

def inputIDforDel(phoneBook):
    while True:
        try:
            id=int(input('Введите номер пункта для удаления:'))
            if id in range (1,len(phoneBook)+1):
                if confirm (f"Точно хотите удалить пункт {id} (y/n)? "):
                    return id
                else:
                    return None
            else:
                print ('Нет такого пункта!')
        except:
            print('Некорректный пункт!')


def showText(text):
    print (text)

def showPause():
    input ('[Enter] - возврат к меню')

# 89263831094
def getBiutyTel(tel:str)->str:
    if len(tel)==11:
        return f'{tel[0]}({tel[1:4]}){tel[4:7]}-{tel[7:9]}-{tel[9:11]}'
    elif len(tel)==12 and tel[0]=='+':
        return f'{tel[0:2]}({tel[2:5]}){tel[5:8]}-{tel[8:10]}-{tel[10:12]}'
    else:
        return tel

def showPhoneBook(phoneBook,config):
    for i,contact in enumerate(phoneBook):

        if config['telMask']=='on':
            contact[1]=getBiutyTel(contact[1])
        print (i+1,*contact)
    if len(phoneBook) == 0:
        print ('Телефонный справочник пуст!')

def choiceMenu(maxPoint):
    while True:
        try:
            choice= int(input('Введите пункт меню: '))
            if choice in range (0,maxPoint+1):
                return choice
            else:
                print ('Нет такого пункта!')
        except:
            print ('Некорректный пункт!')

def showMenu ():
    print ('\nМеню:')
    print('\n1.Показать телефонный справочник')
    print('2.Загрузить телефонный справочник')
    print('3.Сохранить телефонный справочник')
    print('4.Удалить запись')
    print('5.Добавить запись')
    print('6.Изменить запись')
    print('7.Поиск')
    print('8.Настройки')
    print('0.Выход\n')
    return choiceMenu(8)

def showOnOff(val):
    if val=='on':
        return '[on] off '
    else:
        return ' on [off]'


def showMenuConfig (config):
    print ('\nМеню конфигурации:')
    print('1.Сохранить конфигурацию')
    print('{:<60}{:<40}'.format('2.Имя файла справочника',config['fileName']))
    print('{:<60}{:<40}'.format('3.Поиск регитронезависимый',showOnOff(config['registrFree'])))
    print('{:<60}{:<40}'.format('4.Выводить телефон по маске 1(123)383-10-94',showOnOff(config['telMask'])))
    print('0.Выход\n')
    return choiceMenu(4)


def logOff():
    print ('До свиданья!')

def inputFileName():
    fileName=input('Введите название файла')
    return fileName