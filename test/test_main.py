import unittest
from unittest.mock import patch

from main import start_app, init_app


class TestMain(unittest.TestCase):
    def setUp(self):
        pass

    @patch('main.init_app')
    def test_start_app(self, mock_init_function):
        start_app()
        self.assertTrue(mock_init_function.called)

    @patch('core.app.App.init_properties')
    def test_init_app(self, mock_init_properties):
        init_app()
        self.assertTrue(mock_init_properties.called)


if __name__ == '__main__':
    unittest.main()
