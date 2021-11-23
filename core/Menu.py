class Menu:
    def run_menu(self, menu_modes):
        number = self.get_menu_number()
        self.checkout_number(number, menu_modes)

    @staticmethod
    def get_menu_number():
        return input(
            '\n '
            'Выберите один из следующих пунктов: \n '
            '1. Изменить метод. \n '
            '2. Изменить файл. \n '
            '3. Изменить метод и файл. \n '
            '4. Закончить работу с приложением. \n'
        )

    @staticmethod
    def checkout_number(menu_number, menu_modes):
        if menu_number in menu_modes:
            return menu_modes[menu_number]()

        else:
            print('Такого пункта нет.')

