class Note(object):

    def __init__(self, note_id=None, title=None, body=None, create_date=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.create_date = create_date
        self._note_id = None
        self._title = None
        self._body = None
        self._create_date = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def note_id(self):
        return self._note_id

    @note_id.setter
    def note_id(self, note_id):
        self._note_id = note_id

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body):
        self._body = body

    @property
    def date(self):
        return self.create_date

    @date.setter
    def date(self, create_date):
        self._create_date = create_date

    def __str__(self):
        return str({"Заметка номер: ": self._note_id, "Название: ": self._title,
               "Описание: ": self._body, "Время создание: ": self._create_date})


