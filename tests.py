import unittest
from unittest.mock import patch

from processors import *


class TestPrintIntegerProcessor(unittest.TestCase):
    def test_always_matches(self):
        processor = PrintIntegerProcessor()
        self.assertTrue(processor.matches(3))

    @patch('builtins.print')
    def test_prints_number(self, mock_print):
        processor = PrintIntegerProcessor()
        processor.execute(3)
        mock_print.assert_called_with(3)


class TestPrintThreeStringProcessor(unittest.TestCase):
    def test_matches_with_three(self):
        processor = PrintStringProcessor('Three', 3)
        self.assertTrue(processor.matches(3))

    @patch('builtins.print')
    def test_prints_three(self, mock_print):
        processor = PrintStringProcessor('Three', 3)
        processor.execute(3)
        mock_print.assert_called_with('Three')


class TestPrintFiveStringProcessor(unittest.TestCase):
    def test_matches_with_three(self):
        processor = PrintStringProcessor('Five', 5)
        self.assertTrue(processor.matches(5))

    @patch('builtins.print')
    def test_prints_three(self, mock_print):
        processor = PrintStringProcessor('Five', 5)
        processor.execute(5)
        mock_print.assert_called_with('Five')


class TestPrintThreeFiveStringProcessor(unittest.TestCase):
    def test_matches_with_three(self):
        processor = PrintStringProcessor('ThreeFive', 3, 5)
        self.assertTrue(processor.matches(15))

    @patch('builtins.print')
    def test_prints_three(self, mock_print):
        processor = PrintStringProcessor('ThreeFive', 3, 5)
        processor.execute(15)
        mock_print.assert_called_with('ThreeFive')


if __name__ == '__main__':
    unittest.main()
