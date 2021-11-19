from core.App import App
from core.FileHandler import FileHandler
from core.FilePathHandler import FilePathHandler


def init_app():
    file_path_handler = FilePathHandler()

    reader_app = App(file_path_handler)

    return reader_app


def init_file_handler(app):
    file_path = app.file_path

    file_handler = FileHandler(file_path)

    return file_handler


def start_app():
    reader_app = init_app()
    file_handler = init_file_handler(reader_app)

    mode = reader_app.mode
    file_handler.do_action(mode)


start_app()
