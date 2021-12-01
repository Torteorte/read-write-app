from test.utils.utils import test_function_one, test_function_two


test_jp = 'test.木'
test_csv = 'mythic.csv'
test_txt = 'text_files/some_test.txt'

test_txt_extension = 'test.txt'
test_csv_extension = 'test.csv'
test_doc_extension = 'test.doc'

test_csv_file_name = 'text_files/some_test.csv'
test_txt_file_name = 'text_files/some_test.txt'
test_txt_file_name_for_read = 'text_files/file_for_read.txt'
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

builtins_print = 'builtins.print'
builtins_input = 'builtins.input'

path_of_init_app = 'main.init_app'
path_of_get_mode = 'core.mode_handler.ModeHandler.get_mode'
path_of_run_menu = 'core.menu.Menu.run_menu'
path_of_show_menu = 'core.app.App.show_menu'
path_of_do_action = 'core.file_action_handler.FileActionHandler.do_action'
path_of_check_mode = 'core.mode_handler.ModeHandler.check_mode'
path_of_check_file = 'core.file_path_handler.FilePathHandler.check_file'
path_of_get_file_path = 'core.file_path_handler.FilePathHandler.get_file_path'
path_of_csv_read_file = 'core.file_handler.CSVFileHandler.read_file'
path_of_init_properties = 'core.app.App.init_properties'
path_of_checkout_number = 'core.menu.Menu.checkout_number'
path_of_handler_call_menu = 'core.app.App.handler_call_menu'
path_of_txt_write_to_file = 'core.file_handler.TXTFileHandler.write_to_file'
path_of_csv_write_to_file = 'core.file_handler.CSVFileHandler.write_to_file'
path_of_handler_wrong_path = 'core.file_path_handler.FilePathHandler.handler_wrong_path'
path_of_default_write_to_file = 'core.file_handler.default_write_to_file'
path_of_start_action_with_file = 'core.app.App.start_action_with_file'
path_of_get_file_handler_by_extension = 'core.file_action_handler.FileActionHandler.get_file_handler_by_extension'

test_number1 = '1'
test_number2 = '2'

test_menu_modes = {
       test_number1: test_function_one,
       test_number2: test_function_two,
}
