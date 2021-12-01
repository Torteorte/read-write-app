number_of_string_for_read = 5

read_mode = 'read'
write_mode = 'write'
csv_extension = '.csv'
txt_extension = '.txt'
doc_extension = '.doc'

allowed_extensions = [csv_extension, txt_extension, doc_extension]

mode_one = '1'
mode_two = '2'

modes = {
       mode_one: read_mode,
       mode_two: write_mode
}

input_get_mode = \
       f'{mode_one}: {read_mode} \n' \
       f'{mode_two}: {write_mode} \n' \
       'Выберите номер метода: '

default_menu_text = \
       '\n ' \
       '1. Изменить метод. \n ' \
       '2. Выбрать другой файл. \n ' \
       '3. Изменить метод и файл. \n ' \
       '4. Закончить работу с приложением. \n' \
       'Выберите один из пунктов: '

# file_handler_menu_text = \
#        '\n ' \
#        '1. Изменить метод. \n ' \
#        '2. Изменить путь к файлу. \n ' \
#        '3. Выйти из приложеня. \n' \
#        'Выберите один из пунктов: '

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

print_good_bye = '\n Всего доброго.'
print_empty_file = 'Пустой файл.'
input_file_path = 'Путь к файлу: '
menu_test_text = 'test text for input'
print_wrong_item = 'Такого пункта нет.'
print_unknown_method = 'Неопознаный метод'
print_success_write = 'Запись в файл прошла успешно.'
print_wrong_path = 'Такого файла или пути не существует'
print_wrong_extension = 'Неверное расширение файла. Валидные расширения .csv, .txt, .doc'
