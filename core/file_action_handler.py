from utils.utils import get_file_extension
from core.file_handler import CSVFileHandler, TXTFileHandler, DOCFileHandler
from constants.constants import read_mode, write_mode, csv_extension, txt_extension, doc_extension, default_text


class FileActionHandler:
    extensions = {
        csv_extension: CSVFileHandler,
        txt_extension: TXTFileHandler,
        doc_extension: DOCFileHandler
    }

    file_handler_by_extension = None

    def get_file_handler_by_extension(self, file_path):
        file_extension = get_file_extension(file_path)

        self.file_handler_by_extension = self.extensions[file_extension](file_path)

        return self.file_handler_by_extension

    def do_action(self, mode):
        if mode == read_mode:
            self.file_handler_by_extension.read_file()

        elif mode == write_mode:
            self.file_handler_by_extension.write_to_file(default_text)
