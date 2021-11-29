from core.menu import Menu
from core.mode_handler import ModeHandler
from core.file_path_handler import FilePathHandler
from core.file_action_handler import FileActionHandler
from constants.constants import default_menu_text, print_good_bye


class App:
    def __init__(self):
        self.menu = Menu(default_menu_text)
        self.mode_handler = ModeHandler()
        self.file_path_handler = FilePathHandler(self.end_app, self.change_mode_and_file_path)
        self.file_action_handler = FileActionHandler()

        self.exit = False

        self.mode = None
        self.file_path = None
        self.init_properties()

    def init_properties(self):
        self.mode = self.get_mode()
        self.file_path = self.get_file_path()

    def start_action_with_file(self):
        self.file_action_handler.get_file_handler_by_extension(self.file_path)
        self.file_action_handler.do_action(self.mode)
        self.handler_call_menu()

    def get_mode(self):
        return self.mode_handler.get_mode()

    def get_file_path(self):
        return self.file_path_handler.get_file_path()

    def change_mode(self):
        self.mode = self.get_mode()
        self.start_action_with_file()

    def change_file_path(self):
        self.file_path = self.get_file_path()
        self.start_action_with_file()

    def change_mode_and_file_path(self):
        self.mode = self.get_mode()
        self.file_path = self.get_file_path()
        self.start_action_with_file()

    def end_app(self):
        print(print_good_bye)
        self.exit = True

    def handler_call_menu(self):
        if not self.exit:
            return self.show_menu()

    def show_menu(self):
        menu_modes = {
            '1': self.change_mode,
            '2': self.change_file_path,
            '3': self.change_mode_and_file_path,
            '4': self.end_app,
        }

        self.menu.run_menu(menu_modes)
