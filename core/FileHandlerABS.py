from abc import ABC
from constants.constants import number_of_string_for_read, default_text


class FileHandlerABC(ABC):
    def __init__(self, file_path):
        self.file_path = file_path
        self.default_text = default_text

    def read_file(self):
        file = open(self.file_path, 'r')
        counter = 0

        for line in file:
            print(line.strip())
            counter += 1

            if counter == number_of_string_for_read:
                break

    def write_to_file(self):
        file = open(self.file_path, 'w')

        for line in self.default_text:
            file.write(line)

        file.close()
        print('Запись в файл прошла успешно.')


class CSVFileHandler(FileHandlerABC):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.change_text_for_write()

    def change_text_for_write(self):
        text_for_csv_format = self.default_text.split('\n')
        self.change_text_format_for_csv(text_for_csv_format)

        text_without_first_row = text_for_csv_format.copy()
        del text_without_first_row[0]

        self.default_text = ','.join(text_for_csv_format) + '\n' + '\n'.join(text_without_first_row)

    @staticmethod
    def change_text_format_for_csv(text):
        for index in range(len(text)):
            if ',' in text[index]:
                text[index] = '"' + text[index] + '"'


class TXTFileHandler(FileHandlerABC):
    pass


class DOCFileHandler(FileHandlerABC):
    pass
