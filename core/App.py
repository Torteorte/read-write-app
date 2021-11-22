from constants.constants import read_mode, write_mode
from core.FilePathHandler import FilePathHandler


class App:
    def __init__(self):
        self.mode = self.get_mode()
        self.file_path_handler = FilePathHandler()

    @property
    def file_path(self):
        return self.file_path_handler.get_file_path()

    def get_mode(self):
        mode = input(
            '1: read \n'
            '2: write \n'
            'Выберите номер метода: \n'
        )

        return self.check_mode(mode)

    def check_mode(self, mode):
        modes = {
            '1': read_mode,
            '2': write_mode
        }

        if mode in modes.keys():
            return modes[mode]

        else:
            print('Неопознаный метод')
            return self.get_mode()
