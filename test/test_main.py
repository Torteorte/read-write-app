import unittest
from unittest.mock import patch

from core.app import App
from main import start_app, init_app
from test.constants.constatns import path_of_init_properties, path_of_start_action_with_file, \
    path_of_init_app


class TestMain(unittest.TestCase):

    @patch(path_of_init_properties)
    def test_init_app(self, *args):
        init_app()
        self.assertIsInstance(init_app(), type(App()))

    @patch(path_of_init_properties)
    @patch(path_of_start_action_with_file)
    def test_start_action_with_file(self, mock_start_action_with_file, *args):
        start_app()
        self.assertTrue(mock_start_action_with_file.called)

    @patch(path_of_init_app)
    def test_start_app(self, mock_init_app):
        start_app()
        self.assertTrue(mock_init_app.called)


if __name__ == '__main__':
    unittest.main()
