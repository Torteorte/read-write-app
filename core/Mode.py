# from constants.constants import read_mode, write_mode
#
#
# class Mode:
#     def get_mode(self):
#         mode = input(
#             '1: read \n'
#             '2: write \n'
#             'Выберите номер метода: \n'
#         )
#
#         return self.check_mode(mode)
#
#     def check_mode(self, mode):
#         modes = {
#             '1': read_mode,
#             '2': write_mode
#         }
#
#         if mode in modes.keys():
#             return modes[mode]
#
#         else:
#             print('Неопознаный метод')
#             return self.get_mode()
