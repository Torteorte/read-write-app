import os
from core.menu import Menu
from constants.constants import csv_extension, txt_extension, doc_extension, file_handler_menu_text, input_file_path, \
    print_wrong_path, print_wrong_extension


class FilePathHandler:
    def __init__(self, exit_callback, return_to_get_mode_callback):
        self.menu = Menu(file_handler_menu_text)

        self.exit_callback = exit_callback
        self.return_to_get_mode_callback = return_to_get_mode_callback

        self.valid_status = False

    def get_file_path(self):
        file_path = input(input_file_path)
        return self.check_file(file_path)

    def validate_file_path(self, file_path):
        try:
            self.check_file_status(file_path)
            self.check_file_extension(file_path)
            self.valid_status = True

        except TypeError:
            self.valid_status = False

    def check_file(self, file_path):
        self.validate_file_path(file_path)

        while not self.valid_status:
            return self.handler_wrong_path()
        else:
            return file_path

    @staticmethod
    def check_file_status(file_path):
        file_status = os.path.exists(file_path)

        if not file_status:
            print(print_wrong_path)
            raise TypeError()

    @staticmethod
    def check_file_extension(file_path):
        file_extension = os.path.splitext(file_path)[1]
        allowed_extensions = [csv_extension, txt_extension, doc_extension]

        if file_extension not in allowed_extensions:
            print(print_wrong_extension)
            raise TypeError()

    def handler_wrong_path(self):

        menu_path_handler_modes = {
            '1': self.return_to_get_mode_callback,
            '2': self.get_file_path,
            '3': self.exit_callback,
        }

        return self.menu.run_menu(menu_path_handler_modes)
