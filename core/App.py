from core.Reader import Reader
from core.Writer import Writer


class App:
    def __init__(self, mode, file_path):
        self.mode = mode
        self.file_path = file_path
        self.reader = Reader(file_path)
        self.writer = Writer(file_path)

    # def check_mode(self):
    #     if self.mode == 'read':
    #
    #     elif self.mode == 'write':
