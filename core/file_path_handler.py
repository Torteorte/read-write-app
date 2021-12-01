import os

from core.custom_error import CustomError

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

        except CustomError as error:
            print(error.text)
            self.valid_status = False

    def check_file(self, file_path):
        self.validate_file_path(file_path)

        while not self.valid_status:
            return self.handler_wrong_path()

        return file_path

    @staticmethod
    def check_file_is_exist(file_path):
        file_status = os.path.exists(file_path)

        if not file_status:
            raise CustomError(print_wrong_path)

    @staticmethod
    def check_file_extension(file_path):
        file_extension = get_file_extension(file_path)

        if file_extension not in allowed_extensions:
            raise CustomError(print_wrong_extension)

    def handler_wrong_path(self):
        return self.menu.run_menu()
