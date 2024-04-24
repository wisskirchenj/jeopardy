import unittest
from unittest.mock import patch

from jeopardy.bot import main


class BotTest(unittest.TestCase):

    @patch('builtins.input', return_value='What is the capital of France?')
    @patch('builtins.print')
    def test_main(self, mock_print, mock_input):
        main()
        self.assertIn('Kili', mock_print.call_args_list[0][0][0])
        self.assertEqual(2, mock_print.call_count)
        mock_print.assert_called_with("Let's play!")

