import unittest
from unittest.mock import patch

from core.mode_handler import ModeHandler
from constants.constants import read_mode, write_mode, mode_one, mode_two, print_unknown_method, input_get_mode


class TestModeHandler(unittest.TestCase):
    def setUp(self):
        self.ModeHandler = ModeHandler()

    def test_check_mode(self):
        self.assertEqual(self.ModeHandler.check_mode(mode_one), read_mode)
        self.assertEqual(self.ModeHandler.check_mode(read_mode), read_mode)
        self.assertEqual(self.ModeHandler.check_mode(mode_two), write_mode)
        self.assertEqual(self.ModeHandler.check_mode(write_mode), write_mode)

        self.assertNotEqual(self.ModeHandler.check_mode(read_mode), write_mode)
        self.assertNotEqual(self.ModeHandler.check_mode(mode_two), mode_one)

    @patch('core.mode_handler.ModeHandler.check_mode')
    @patch('builtins.input')
    def test_run_menu(self, mock_input, mock_check_mode):
        self.ModeHandler.get_mode()

        self.assertTrue(mock_check_mode.called)
        mock_input.assert_called_with(input_get_mode)

    @patch('core.mode_handler.ModeHandler.get_mode')
    @patch('builtins.print')
    def test_false_check_mode(self, mock_print, mock_get_mode):

        self.ModeHandler.check_mode('564')
        self.assertTrue(mock_get_mode.called)
        mock_print.assert_called_with(print_unknown_method)


if __name__ == "__main__":
    unittest.main()
