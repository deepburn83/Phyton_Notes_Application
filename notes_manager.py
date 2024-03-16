import json
from datetime import datetime


class Note:
    def __init__(self, note_id, title, body, timestamp=None):
        self.id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp if timestamp else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "timestamp": self.timestamp
        }

    def __repr__(self):
        return f"Note(id={self.id}, title='{self.title}', body='{self.body}', timestamp='{self.timestamp}')"


class NotesManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []

    def load_notes(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.notes = [Note(**note_data) for note_data in data]
        except FileNotFoundError:
            self.notes = []

    def save_notes(self):
        with open(self.file_path, 'w') as file:
            data = [note.to_dict() for note in self.notes]
            json.dump(data, file, indent=4)

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        note = Note(note_id, title, body)
        self.notes.append(note)
        self.save_notes()
        return note

    def edit_note(self, note_id, title, body):
        for note in self.notes:
            if note.id == note_id:
                note.title = title
                note.body = body
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                return note
        return None

    def delete_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                self.save_notes()
                return True
        return False

    def print_notes(self):
        for note in self.notes:
            print(note)

