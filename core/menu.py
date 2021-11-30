from constants.constants import print_wrong_item


class Menu:
    def __init__(self, menu_text, menu_modes=None):
        self.menu_text = menu_text
        self._menu_modes = menu_modes

    def run_menu(self, menu_modes=None):
        if menu_modes is None and self._menu_modes is not None:
            menu_modes = self._menu_modes

        number = self.get_menu_number()
        self.checkout_number(number, menu_modes)

    def get_menu_number(self):
        return input(self.menu_text)

    def checkout_number(self, menu_number, menu_modes):
        if menu_number in menu_modes:
            return menu_modes[menu_number]()

        else:
            print(print_wrong_item)
            self.run_menu(menu_modes)
