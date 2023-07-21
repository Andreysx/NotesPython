import json
from note import Note
import datetime

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
            return result_json
        except FileExistsError as ex:
            return ex

    def del_note(self, id):
        result = self.read_file()
        print()
        for i, value in enumerate(result):
            value = dict(value)
            if id == int(value["Заметка номер: "]):
                result.pop(i)
        self.notes = result
        self.write_file()






    # def write(self, notes):
    #     notes_list = list()
    #     for note in notes:
