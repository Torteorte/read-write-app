from core.App import App
from core.FileHandler import FileHandler
from core.Menu import Menu


def init_app():
    return App()


def init_file_handler():
    return FileHandler()


def init_menu(mode, get_new_mode, file_handler, get_new_file_path_handler):
    return Menu(mode, get_new_mode, file_handler, get_new_file_path_handler, start_app)


def start_app():
    reader_app = init_app()
    file_handler = init_file_handler()

    file_handler.start_action_with_file(reader_app.file_path, reader_app.mode)

    menu = init_menu(reader_app.mode, reader_app.get_mode, file_handler, reader_app.file_path_handler)
    menu.handler_call_menu()


if __name__ == "__main__":
    start_app()
