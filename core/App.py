from core.Reader import Reader
from core.Writer import Writer


class App:
    def __init__(self, mode, file_path):
        self.mode = mode
        self.file_path = file_path
        self.reader = Reader(file_path)
        self.writer = Writer(file_path)

    def start_selected_mode(self):
        if self.mode == 'read':
            self.reader.handler_read_file()

        elif self.mode == 'write':
            self.writer.handler_write_to_file()
