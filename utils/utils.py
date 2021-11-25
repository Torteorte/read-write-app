def default_write_to_file(file_path, default_text):
    file = get_file(file_path)

    for line in default_text:
        file.write(line)

    file.close()
    print('Запись в файл прошла успешно.')


def get_file(file_path):
    file = open(file_path, 'w')
    return file
