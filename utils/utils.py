from constants.constants import default_text


def default_write_to_file(file_path):
    file = open(file_path, 'w')

    for line in default_text:
        file.write(line)

    file.close()
    print('Запись в файл прошла успешно.')
