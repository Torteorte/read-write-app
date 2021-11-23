import csv
from abc import ABC, abstractmethod
from utils.utils import default_write_to_file
from constants.constants import number_of_string_for_read, default_text


class FileHandlerABC(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        file = open(self.file_path, 'r')
        counter = 0

        for line in file:
            print(line.strip())
            counter += 1

            if counter == number_of_string_for_read:
                break

        if counter == 0:
            print('Пустой файл')

    @abstractmethod
    def write_to_file(self):
        pass


class CSVFileHandler(FileHandlerABC):
    def write_to_file(self):
        with open(self.file_path, 'w', newline='') as File:
            content_of_file = csv.writer(File)
            content_of_file.writerow(default_text.split('\n'))

            for row in self.delete_first_row_in_text():
                content_of_file.writerow([row])

        File.close()
        print('Запись в файл прошла успешно.')

    @staticmethod
    def delete_first_row_in_text():
        text_without_first_row = default_text.split('\n').copy()
        del text_without_first_row[0]

        return text_without_first_row


class TXTFileHandler(FileHandlerABC):
    def write_to_file(self):
        default_write_to_file(self.file_path)


class DOCFileHandler(FileHandlerABC):
    def write_to_file(self):
        default_write_to_file(self.file_path)
