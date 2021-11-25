import unittest
from core.mode_handler import ModeHandler
from constants.constants import read_mode, write_mode, mode_one, mode_two


class TestModeHandler(unittest.TestCase):
    def setUp(self):
        self.modeHandler = ModeHandler()

    def test_check_mode(self):
        self.assertEqual(self.modeHandler.check_mode(mode_one), read_mode)
        self.assertEqual(self.modeHandler.check_mode(read_mode), read_mode)
        self.assertEqual(self.modeHandler.check_mode(mode_two), write_mode)
        self.assertEqual(self.modeHandler.check_mode(write_mode), write_mode)
        self.assertNotEqual(self.modeHandler.check_mode(read_mode), write_mode)
        self.assertNotEqual(self.modeHandler.check_mode(mode_two), mode_one)
        # self.assertFalse(self.modeHandler.check_mode('3'))


if __name__ == "__main__":
    unittest.main()
