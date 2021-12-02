import csv
from abc import ABC, abstractmethod

from utils.utils import default_write_to_file
from constants.constants import number_of_string_for_read, print_empty_file, print_success_write


class FileHandlerABC(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        file = open(self.file_path, 'r')
        line = file.read().split('\n')
        counter = 0

        while counter < number_of_string_for_read and counter != len(line):
            print(line[counter])
            counter += 1

        if line == ['']:
            print(print_empty_file)

        file.close()

    @abstractmethod
    def write_to_file(self, text):
        pass


class CSVFileHandler(FileHandlerABC):
    def write_to_file(self, default_csv_text):
        with open(self.file_path, 'w', newline='') as File:
            content_of_file = csv.writer(File)
            content_of_file.writerow(default_csv_text.split('\n'))

            for row in self.delete_first_row_in_text(default_csv_text):
                content_of_file.writerow([row])

        print(print_success_write)

    @staticmethod
    def delete_first_row_in_text(default_csv_text):
        text_without_first_row = default_csv_text.split('\n').copy()
        del text_without_first_row[0]

        return text_without_first_row


class TXTFileHandler(FileHandlerABC):
    def write_to_file(self, default_text):
        return default_write_to_file(self.file_path, default_text)


class DOCFileHandler(FileHandlerABC):
    def write_to_file(self, default_text):
        return default_write_to_file(self.file_path, default_text)
