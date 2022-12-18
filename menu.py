import view
import phoneBook as pb
import database as db
import config

def start():
    config.convertFromStr(db.loadConfig())
    while True:
        choice = view.showMenu()
        if mainMenu(choice):
            view.logOff()
            break



def mainMenu(choice:int):

    match choice:
        case 1:
            view.showPhoneBook(pb.phoneBook,config.getConfig())
            view.showPause()
        case 2:
            strs=db.loadBase()
            if strs:
                pb.convertFromStr(strs)
                if len (pb.phoneBook)>0:
                    view.showText('Записи загружены из базы!')
                    view.showPhoneBook(pb.phoneBook,config.getConfig())
                else:
                    view.showText('База пуста!')
            else:
                view.showText('База не создана!')
        case 3:
            if len(pb.phoneBook)>0:
                db.saveBase(pb.convertToStr())
                view.showText('База сохранена')
            else:
                view.showText('База пуста, не может быть сохранена!')
        case 4:
            view.showPhoneBook(pb.phoneBook,config.getConfig())
            id=view.inputIDforDel(pb.phoneBook)
            if not id==None:
                pb.delID(id)
                view.showText(f'Запись {id} удалена')
        case 5:
            pb.addContact(view.addContact())
            view.showText('Запись добавлена')
        case 6:
            view.showPhoneBook(pb.phoneBook,config.getConfig())
            id,type,newVal =view.editContact(pb.phoneBook)
            if not id==None:
                pb.editContact(id,type,newVal)
                view.showText('Запись изменена')
        case 7:
            view.showFinded(pb.find(view.findInput(),config.getConfig()),pb.phoneBook)
        case 8:
            choiceConfig=view.showMenuConfig(config.getConfig())
            configMenu(choiceConfig)


        case 0:
            return True

def configMenu(choice:int):
    while True:

        match choice:
            case 1:
                db.saveConfig(config.convertToStr())
                view.showText('Конфигурация сохранена!')
            case 2:
                config.update ('fileName',view.inputFileName())
            case 3:
                config.update('registrFree', config.onOff('registrFree'))
            case 4:
                config.update('telMask', config.onOff('telMask'))
            case 0:
                return True
        choice = view.showMenuConfig(config.getConfig())