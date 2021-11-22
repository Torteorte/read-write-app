class Menu:
    def __init__(self, mode, get_mode, file_handler, new_file_path_handler, create_app):
        self.menu_number = None
        self.mode = mode
        self.exit = False
        self.get_new_mode_handler = get_mode
        self.file_handler = file_handler
        self.new_file_path_handler = new_file_path_handler
        self.create_app = create_app

    def handler_call_menu(self):
        self.select_menu_number()
        self.checkout_number()

        if not self.exit:
            return self.handler_call_menu()

    def select_menu_number(self):
        self.menu_number = input(
            '\n '
            'Выберите один из следующих пунктов: \n '
            '1. Изменить метод. \n '
            '2. Изменить файл. \n '
            '3. Изменить метод и файл. \n '
            '4. Закончить работу с приложением. \n'
        )

    def checkout_number(self):
        menu_numbers = {
            '1': self.get_new_mode,
            '2': self.get_new_file_path,
            '3': self.start_new_app,
            '4': self.end_app,
        }

        if self.menu_number in menu_numbers:
            return menu_numbers[self.menu_number]()

        else:
            print('Такого пункта нет.')

    def get_new_mode(self):
        self.mode = self.get_new_mode_handler()
        self.file_handler.do_action(self.mode)

    def get_new_file_path(self):
        file_path = self.new_file_path_handler.get_file_path()

        self.file_handler.start_action_with_file(file_path, self.mode)

    def start_new_app(self):
        self.create_app()

    # @staticmethod
    def end_app(self):
        print('Всего доброго.')
        self.exit = True
