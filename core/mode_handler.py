from constants.constants import read_mode, write_mode, mode_one, mode_two, input_get_mode, print_unknown_method


class ModeHandler:
    modes = {
        mode_one: read_mode,
        mode_two: write_mode
    }

    def get_mode(self):
        mode = self.input_mode()
        return self.check_mode(mode)

    @staticmethod
    def input_mode():
        return input(input_get_mode)

    def check_mode(self, mode):
        if mode in self.modes.keys():
            return self.modes[mode]

        elif mode in self.modes.values():
            return mode

        else:
            print(print_unknown_method)
            return self.get_mode()
