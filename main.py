from core.App import App
from utils.utils import select_mode, get_file_path


def init_app():
    mode = select_mode()
    file_path = get_file_path()

    app = App(mode, file_path)

    return app


def start_app():
    app = init_app()
    app.start_selected_mode()


start_app()
