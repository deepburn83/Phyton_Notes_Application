from notes_manager import NotesManager


def main():
    file_path = "notes.json"  # Путь к файлу с заметками
    manager = NotesManager(file_path)
    manager.load_notes()

    while True:
        command = input("Введите команду (add/read/edit/delete/exit): ").strip().lower()

        if command == "add":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            manager.add_note(title, body)
            print("Заметка успешно добавлена.")
        elif command == "read":
            manager.print_notes()
        elif command == "edit":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            if manager.edit_note(note_id, title, body):
                print("Заметка успешно отредактирована.")
            else:
                print("Заметка с указанным ID не найдена.")
        elif command == "delete":
            note_id = int(input("Введите ID заметки для удаления: "))
            if manager.delete_note(note_id):
                print("Заметка успешно удалена.")
            else:
                print("Заметка с указанным ID не найдена.")
        elif command == "exit":
            print("Выход из программы.")
            break
        else:
            print("Неверная команда. Пожалуйста, выберите одну из доступных команд.")


if __name__ == "__main__":
    main()
