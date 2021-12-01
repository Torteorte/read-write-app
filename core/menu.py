from constants.constants import print_wrong_item


class Menu:
    def __init__(self, menu_text, menu_modes):
        self.menu_text = menu_text
        self._menu_modes = menu_modes

    def run_menu(self):
        number = self.get_menu_number()
        self.checkout_number(number)

    def get_menu_number(self):
        return input(self.menu_text)

    def checkout_number(self, menu_number):
        if menu_number in self._menu_modes:
            return self._menu_modes[menu_number]()

        else:
            print(print_wrong_item)
            self.run_menu()
