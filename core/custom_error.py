class CustomError(Exception):
    def __init__(self, text):
        self.text = text


class FilePathError(CustomError):
    pass
