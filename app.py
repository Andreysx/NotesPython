from file_handler import JsonHandler

def run():
    handler = JsonHandler()
    while True:
        print("Добро пожаловать в заметки")
        command = int(input("1 - Создать заметку\n"
                        "2 - Посмотреть заметки\n"
                        "3 - Посмотреть заметку по id\n"
                        "4 - Изменить заметку\n"
                        "5 - Удалить заметку\n"
                        "6 - Выйти\n"
                        ))
        if command == 1:
            handler.add_new_note()
        elif command == 2:
            handler.show_all_notes()
        elif command == 3:
            handler.show_note()
        elif command == 4:
            handler.change_note()
        elif command == 5:
            handler.del_note()
        elif command == 6:
            break
        else:
            print("Команда не найдена")
