import json
from note import Note
import datetime
import ast
from pprint import pprint
from config import BASE_PATH
import os

class JsonHandler:


    def __init__(self):
        self.id = 1
        self.notes = list()
        self.note = Note()
        self.current_notes = self.read_file()

    def create_note(self, note: list):
        self.note.note_id = note[0]
        self.note.title = note[1]
        self.note.body = note[2]
        self.note.date = note[3]
        self.notes.append(self.note.__str__())
        self.write_file()


    def add_new_note(self):
        try:
            max_id = max([value["Заметка номер: "] for value in self.convent_to_dict(self.read_file())])
        except ValueError:
            max_id = None
        if max_id:
            self.id = max_id + 1
        new_note = list()
        new_note.append(self.id)
        new_note.append(input("Введите название заметки: "))
        new_note.append(input("Напишите заметку: "))
        new_note.append(str(datetime.datetime.now().replace(microsecond=0)))
        self.create_note(new_note)

    def write_file(self):
        with open(BASE_PATH, "w", encoding="utf-8") as f:
            number1 = json.dumps(self.current_notes + self.notes, default=str, ensure_ascii=False)
            f.write(number1)


    def read_file(self):
        if os.path.isfile(BASE_PATH):
            with open(BASE_PATH, "r", encoding="utf-8") as f:
                try:
                    result_json = json.load(f)
                    if len(result_json) > 0:
                        result_json = [self.convent_to_dict(value) for value in result_json]
                    result_json.sort(key=lambda x: x["Время создание: "])
                    return result_json
                except ValueError:
                    return []
        else:
            return []

    def del_note(self):
        id = int(input("Введите id для удаления: "))
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
