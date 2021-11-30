import os

from constants.constants import input_file_path, print_wrong_path, print_wrong_extension, allowed_extensions
from utils.utils import get_file_extension


class FilePathHandler:
    def __init__(self, menu):
        self.menu = menu

        self.valid_status = False

    def get_file_path(self):
        file_path = input(input_file_path)
        return self.check_file(file_path)

    def validate_file_path(self, file_path):
        try:
            self.check_file_is_exist(file_path)
            self.check_file_extension(file_path)
            self.valid_status = True

        except TypeError:
            self.valid_status = False

    def check_file(self, file_path):
        self.validate_file_path(file_path)

        while not self.valid_status or file_path is None:
            return self.handler_wrong_path()

        return file_path

    @staticmethod
    def check_file_is_exist(file_path):
        file_status = get_file_extension(file_path)

        if not file_status:
            print(print_wrong_path)
            raise TypeError()

    @staticmethod
    def check_file_extension(file_path):
        file_extension = os.path.splitext(file_path)[1]

        if file_extension not in allowed_extensions:
            print(print_wrong_extension)
            raise TypeError()

    def handler_wrong_path(self):
        return self.menu.run_menu()
