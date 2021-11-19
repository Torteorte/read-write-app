from constants.constants import read_mode, write_mode


class App:
    def __init__(self, file_path_handler):
        self.mode = self.get_mode()
        self.file_path = file_path_handler.get_file_path()

    def get_mode(self):
        mode = input('Выберите номер метода: \n'
                     '1: read \n'
                     '2: write \n')

        if mode == '1':
            mode = read_mode

        elif mode == '2':
            mode = write_mode

        else:
            print('Неопознаный метод')
            return self.get_mode()

        return mode
