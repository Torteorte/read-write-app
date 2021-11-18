from utils.utils import write_to_file


class Writer:

    def __init__(self, file_path):
        self.file_path = file_path

    def handler_write_to_file(self):
        write_to_file(self.file_path)
