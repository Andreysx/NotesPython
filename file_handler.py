import json
from note import Note
import datetime

class JsonHandler:

    def __init__(self, file):
        self.file = file
        self.notes = list()
        self.note = Note()

    def create_note(self, note: list):
        self.note.note_id = note[0]
        self.note.title = note[1]
        self.note.body = note[2]
        self.note.date = note[3]

    def add_new_note(self):
        new_note = list()
        new_note.append(input("Введите id: "))
        new_note.append(input("Введите название заметки: "))
        new_note.append(input("Напишите заметку: "))
        new_note.append(str(datetime.datetime.now().replace(microsecond=0)))
        self.create_note(new_note)




    # def write(self, notes):
    #     notes_list = list()
    #     for note in notes:
