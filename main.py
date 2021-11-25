from core.app import App


def init_app():
    return App()


def start_app():
    reader_app = init_app()
    reader_app.start_action_with_file()
    reader_app.handler_call_menu()


if __name__ == "__main__":
    start_app()
