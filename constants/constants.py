number_of_string_for_read = 5

read_mode = 'read'
write_mode = 'write'
csv_extension = '.csv'
txt_extension = '.txt'
doc_extension = '.doc'

mode_one = '1'
mode_two = '2'

input_get_mode = \
       f'{mode_one}: {read_mode} \n' \
       f'{mode_two}: {write_mode} \n' \
       'Выберите номер метода: \n'

default_menu_text = \
       '\n ' \
       'Выберите один из следующих пунктов: \n ' \
       '1. Изменить метод. \n ' \
       '2. Изменить файл. \n ' \
       '3. Изменить метод и файл. \n ' \
       '4. Закончить работу с приложением. \n' \

file_handler_menu_text = \
       '\n ' \
       'Выберите один из следующих пунктов: \n ' \
       '1. Изменить метод. \n ' \
       '2. Изменить путь к файлу. \n ' \
       '3. Выйти из приложеня. \n' \

default_text = 'У Лукоморья дуб срубили\n' \
       'Златую цепь в музей снесли\n' \
       'Кота в зверятник запустили\n' \
       'Русалку в бочку посадили\n' \
       'И написали, «Огурцы»\n' \
       'И по морю пустили...\n\n' \
       'Там на неведомых дорожках\n' \
       'Уже давно растет картошка,\n' \
       'Скелеты бродят в босоножках\n' \
       'Следы разбитых Жигулей\n' \
       'И Мерседес на курьих ножках\n' \
       'Стоит без окон, без дверей'


test_jp = 'test.木'
test_csv = 'mythic.csv'
test_txt = 'text_files/some_test.txt'

test_txt_extension = 'test.txt'
test_csv_extension = 'test.csv'
test_doc_extension = 'test.doc'

test_csv_file_name = 'text_files/some_test.csv'
test_txt_file_name = 'text_files/some_test.txt'
test_doc_file_name = 'text_files/some_test.doc'
test_txt_file_empty = 'text_files/test_empty.txt'

test_text_to_write = 'Some text to write'

csv_test_text_to_write = \
       'Some\n' \
       'text\n' \
       'to, write'

csv_result_text = \
       'Some,text,"to, write"\n' \
       'text\n' \
       '"to, write"\n'

print_good_bye = 'Всего доброго.'
print_empty_file = 'Пустой файл.'
input_file_path = 'Путь к файлу: '
print_wrong_item = 'Такого пункта нет.'
print_unknown_method = 'Неопознаный метод'
print_success_write = 'Запись в файл прошла успешно.'
print_wrong_path = 'Такого файла или пути не существует'
print_wrong_extension = 'Неверное расширение файла. Валидные расширения .csv, .txt, .doc'

path_of_show_menu = 'core.app.App.show_menu'
path_of_get_mode = 'core.mode_handler.ModeHandler.get_mode'
path_of_start_action_with_file = 'core.app.App.start_action_with_file'
path_of_get_file_path = 'core.file_path_handler.FilePathHandler.get_file_path'
