from core.App import App
from utils.utils import select_mode, get_file_path


def start_app():
    mode = select_mode()
    file_path = get_file_path()
    app = App(mode, file_path)
    # app.reader.handler_read_file()
    app.writer.handler_write_to_file()


start_app()
