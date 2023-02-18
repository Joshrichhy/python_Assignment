class entry:
    def __init__(self, title, body, id_number):
        self.title = title
        self.body = body
        self.id_number = id_number

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_body(self, body):
        self.body = body

    def get_body(self):
        return self.body

    def set_id_number(self, id_number):
        self.id_number = id_number

    def get_id_number(self):
        return self.id_number

    def __str__(self):
        toShow = ""
        toShow += "Entry id: " + str(self.id_number) + "\n"
        toShow += "Entry title:  " + str(self.title) + "\n"
        toShow += "Entry body: " + str(self.body) + "\n"
        toShow += "\n"
        return toShow
