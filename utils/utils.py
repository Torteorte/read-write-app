import os


def default_write_to_file(file_path, default_text):
    file = get_file(file_path)

    for line in default_text:
        file.write(line)

    file.close()
    print('Запись в файл прошла успешно.')


def get_file(file_path, mode='w'):
    return open(file_path, mode)


def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]
