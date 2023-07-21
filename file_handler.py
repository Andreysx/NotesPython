import json
from note import Note
import datetime
import ast
from pprint import pprint



class JsonHandler:

    def __init__(self, file):
        self.id = 0
        self.file = file
        self.notes = list()
        self.note = Note()

    def create_note(self, note: list):
        self.note.note_id = note[0]
        self.note.title = note[1]
        self.note.body = note[2]
        self.note.date = note[3]
        self.notes.append(self.note.__str__())


    def add_new_note(self):
        self.id += 1
        new_note = list()
        new_note.append(self.id)
        new_note.append(input("Введите название заметки: "))
        new_note.append(input("Напишите заметку: "))
        new_note.append(str(datetime.datetime.now().replace(microsecond=0)))
        self.create_note(new_note)

    def write_file(self):
        with open("json_notes.json", "w", encoding="utf-8") as f:
            number1 = json.dumps(self.notes, default=str, ensure_ascii=False)
            f.write(number1)


    def read_file(self):
        try:
            with open("json_notes.json", "r", encoding="utf-8") as f:
                result_json = json.load(f)
                result_json.sort(key=lambda x: x["Время создание: "])
            return result_json
        except FileExistsError as ex:
            return ex

    def del_note(self):
        id = int(input("Введите id для изменения: "))
        result = self.read_file()
        print()
        for i, value in enumerate(result):
            value = self.convent_to_dict(value)
            if id == int(value["Заметка номер: "]):
                result.pop(i)
        self.notes = result
        self.write_file()


    def show_all_notes(self):
        all_notes = self.read_file()
        for i in all_notes:
            pprint(self.convent_to_dict(i))

    def show_note(self):
        id = int(input("Введите id для просмотра: "))
        all_notes = self.read_file()
        for i, value in enumerate(all_notes):
            value = self.convent_to_dict(value)
            if id == int(value["Заметка номер: "]):
                pprint(value)

    def change_note(self):
        id = int(input("Введите id для изменения: "))
        result = self.read_file()
        print()
        for i, value in enumerate(result):
            value = self.convent_to_dict(value)
            if id == int(value["Заметка номер: "]):
                value["Название: "] = input("Введите новое название: ")
                value["Описание: "] = input("Новое описание: ")
            result[i] = value
        self.notes = result
        self.write_file()

    @staticmethod
    def convent_to_dict(value):
        if isinstance(value, str):
            value = ast.literal_eval(value)
        return value





    # def write(self, notes):
    #     notes_list = list()
    #     for note in notes:
