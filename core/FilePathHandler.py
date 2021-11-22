import os
from constants.constants import csv_extension, txt_extension, doc_extension


class FilePathHandler:
    def __init__(self):
        self.valid_status = False

    def get_file_path(self):
        file_path = input('Путь к файлу: ')
        return self.check_file(file_path)

    def validate_file_path(self, file_path):
        try:
            self.check_file_status(file_path)
            self.check_file_extension(file_path)
            self.valid_status = True

        except TypeError:
            self.valid_status = False

    def check_file(self, file_path):
        self.validate_file_path(file_path)

        if not self.valid_status:
            return self.get_file_path()

        return file_path

    @staticmethod
    def check_file_status(file_path):
        file_status = os.path.exists(file_path)

        if not file_status:
            print('Такого файла или пути не существует')
            raise TypeError()

    @staticmethod
    def check_file_extension(file_path):
        file_extension = os.path.splitext(file_path)[1]
        allowed_extensions = [csv_extension, txt_extension, doc_extension]

        if file_extension not in allowed_extensions:
            print('Неверное расширение файла. Валидные расширения .csv, .txt, .doc')
            raise TypeError()
