from constants.constants import read_mode, write_mode, mode_one, mode_two


class ModeHandler:
    def get_mode(self):
        mode = input(
            f'{mode_one}: {read_mode} \n'
            f'{mode_two}: {write_mode} \n'
            'Выберите номер метода: \n'
        )

        return self.check_mode(mode)

    def check_mode(self, mode):
        modes = {
            mode_one: read_mode,
            mode_two: write_mode
        }

        if mode in modes.keys():
            return modes[mode]

        elif mode in modes.values():
            return mode

        else:
            print('Неопознаный метод')
            return self.get_mode()
