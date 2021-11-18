from constants.constants import number_of_string_for_read, default_text
from utils.utils import read_file


class Reader:
    number_of_string = number_of_string_for_read
    default_text = default_text

    def __init__(self, file_path):
        self.file_path = file_path

    def handler_read_file(self):
        read_file(self.file_path)
