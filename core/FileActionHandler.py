import os
from core.FileHandlerABS import CSVFileHandler, TXTFileHandler, DOCFileHandler
from constants.constants import read_mode, write_mode, csv_extension, txt_extension, doc_extension


class FileActionHandler:
    file_handler_by_extension = None

    def get_file_handler_by_extension(self, file_path):
        file_extension = os.path.splitext(file_path)[1]

        extensions = {
            csv_extension: CSVFileHandler(file_path),
            txt_extension: TXTFileHandler(file_path),
            doc_extension: DOCFileHandler(file_path)
        }

        if file_extension in extensions.keys():
            self.file_handler_by_extension = extensions[file_extension]

    def do_action(self, mode):
        if mode == read_mode:
            self.file_handler_by_extension.read_file()

        elif mode == write_mode:
            self.file_handler_by_extension.write_to_file()
