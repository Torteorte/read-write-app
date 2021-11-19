from utils.utils import read_file


class Reader:
    def __init__(self, file_path):
        self.file_path = file_path

    def handler_read_file(self):
        read_file(self.file_path)
