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

    @patch('builtins.input')
    def test_run_menu(self, mock_input):
        patcher = patch.object(ModeHandler, 'check_mode')
        patched = patcher.start()

        self.ModeHandler.get_mode()
        assert patched.call_count == 1

        patched.assert_called_with(self.ModeHandler.input_mode())
        mock_input.assert_called_with(input_get_mode)

        patcher.stop()

    @patch('builtins.print')
    def test_false_check_mode(self, mock_print):
        patcher = patch.object(ModeHandler, 'get_mode')
        patched = patcher.start()

        self.ModeHandler.check_mode('564')
        assert patched.call_count == 1

        patched.assert_called_with()
        mock_print.assert_called_with(print_unknown_method)

        patcher.stop()


if __name__ == "__main__":
    unittest.main()
