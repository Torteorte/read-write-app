import os
from core.FileHandlerABS import CSVFileHandler, TXTFileHandler, DOCFileHandler
from constants.constants import read_mode, write_mode, csv_extension, txt_extension, doc_extension


class FileHandler:
    file_handler = None

    def start_action_with_file(self, file_path, mode):
        self.get_file_extension(file_path)
        self.do_action(mode)

    def get_file_extension(self, file_path):
        file_extension = os.path.splitext(file_path)[1]

        extensions = {
            csv_extension: CSVFileHandler(file_path),
            txt_extension: TXTFileHandler(file_path),
            doc_extension: DOCFileHandler(file_path)
        }

        if file_extension in extensions.keys():
            self.file_handler = extensions[file_extension]

    def do_action(self, mode):
        if mode == read_mode:
            self.file_handler.read_file()

        elif mode == write_mode:
            self.file_handler.write_to_file()
