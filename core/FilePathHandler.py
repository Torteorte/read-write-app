import os
from constants.constants import csv_extension, txt_extension, doc_extension


class FilePathHandler:
    def get_file_path(self):
        file_path = input('Путь к файлу: ')
        return self.check_file(file_path)

    def check_file(self, file_path):
        file_status = os.path.exists(file_path)
        file_extension = os.path.splitext(file_path)[1]
        allowed_extensions = [csv_extension, txt_extension, doc_extension]

        if not file_status:
            print('Такого файла или пути не существует')
            return self.get_file_path()

        elif file_extension not in allowed_extensions:
            print('Неверное расширение файла. Валидные расширения .csv, .txt, .doc')
            return self.get_file_path()

        else:
            return file_path
