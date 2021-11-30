import unittest
from unittest.mock import patch

from core.app import App

from constants.constants import print_good_bye, read_mode
from test.constants.constatns import path_of_show_menu, path_of_get_mode, path_of_start_action_with_file, \
    path_of_get_file_path


class TestApp(unittest.TestCase):

    @patch(path_of_get_mode)
    @patch(path_of_get_file_path)
    def setUp(self, *args):
        self.app = App()

    @patch(path_of_get_mode)
    @patch(path_of_get_file_path)
    def test_init_properties_is_called(self, mock_get_file_path, mock_get_mode):
        self.app.init_properties()

        self.assertTrue(mock_get_mode.called)
        self.assertTrue(mock_get_file_path.get_file_path)

    @patch(path_of_get_mode)
    @patch(path_of_get_file_path)
    def test_init_properties(self, mock_get_file_path, mock_get_mode):
        mock_get_file_path.return_value = 'some_test.txt'
        mock_get_mode.return_value = read_mode

        self.app.init_properties()

        self.assertEqual(self.app.file_path, 'some_test.txt')
        self.assertEqual(self.app.mode, read_mode)

    @patch('core.file_action_handler.FileActionHandler.get_file_handler_by_extension')
    @patch('core.file_action_handler.FileActionHandler.do_action')
    @patch('core.app.App.handler_call_menu')
    def test_start_action_with_file(self, mock_handler_call_menu, mock_do_action,  mock_get_file_handler_by_extension):
        self.app.start_action_with_file()

        self.assertTrue(mock_get_file_handler_by_extension.called)
        self.assertTrue(mock_do_action.called)
        self.assertTrue(mock_handler_call_menu.called)

    @patch(path_of_get_mode)
    @patch(path_of_start_action_with_file)
    def test_change_mode(self, mock_start_action_with_file, mock_get_mode):
        self.app.change_mode()

        self.assertTrue(mock_get_mode.called)
        self.assertTrue(mock_start_action_with_file.called)

    @patch(path_of_start_action_with_file)
    @patch(path_of_get_mode)
    @patch(path_of_get_file_path)
    def test_change_mode_file_path_none(self, mock_get_file_path, *args):
        self.app.file_path = None
        self.app.change_mode()

        self.assertTrue(mock_get_file_path.called)

    @patch(path_of_get_file_path)
    @patch(path_of_start_action_with_file)
    def test_change_file_path(self, mock_start_action_with_file, mock_get_file_path):
        self.app.change_file_path()

        self.assertTrue(mock_get_file_path.called)
        self.assertTrue(mock_start_action_with_file.called)

    @patch(path_of_get_mode)
    @patch(path_of_get_file_path)
    @patch(path_of_start_action_with_file)
    def test_change_mode_and_file_path(self, mock_start_action_with_file, mock_get_file_path, mock_get_mode):
        self.app.change_mode_and_file_path()

        self.assertTrue(mock_get_mode.called)
        self.assertTrue(mock_get_file_path.called)
        self.assertTrue(mock_start_action_with_file.called)

    @patch('builtins.print')
    def test_end_app(self, mock_print):
        self.app.end_app()

        self.assertTrue(self.app.exit)
        mock_print.assert_called_with(print_good_bye)

    @patch(path_of_show_menu)
    def test_handler_call_menu(self, mock_show_menu):
        self.app.handler_call_menu()
        self.assertTrue(mock_show_menu.called)

    @patch(path_of_show_menu)
    def test_false_handler_call_menu(self, mock_show_menu):
        self.app.exit = True
        self.app.handler_call_menu()

        self.assertFalse(mock_show_menu.called)

    @patch('core.menu.Menu.run_menu')
    def test_show_menu(self, mock_run_menu):
        self.app.show_menu()
        self.assertTrue(mock_run_menu.called)


if __name__ == '__main__':
    unittest.main()
