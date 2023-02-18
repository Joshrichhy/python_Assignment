from diaryApplication.entry import entry


class diary:

    def __init__(self):
        self.entries = []

    def create_entry(self, title, body):
        id = len(self.entries) + 1
        new_entry = entry(title, body, id)
        new_entry.set_body(body)
        new_entry.set_title(title)
        self.entries.append(new_entry)

    def get_pages_in_diary(self):
        pages = len(self.entries)
        for page in range(0, len(self.entries), 1):
            if self.find_entry(page) == "null":
                pages -= 1

        return pages

    def find_entry(self, id_number: int):
        return self.entries[id_number - 1]

    def write_into_diary(self, id_number, title, body):
        id_number = entry(self.entries[id_number - 1])
        id_number.set_body(body)
        id_number.set_title(title)
        self.entries.append(id_number)

    def delete_entry(self, id_number):
        entry_to_be_deleted = self.find_entry(id_number)
        self.entries.remove(entry_to_be_deleted)
        self.entries.insert(id_number - 1, "null")

    def view_diary(self):
        for page in range(0, len(self.entries), 1):
            print(self.entries[page])
