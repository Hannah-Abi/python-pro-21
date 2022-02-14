import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.absolute_value'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

@points('1.absolute_value')
class AbsolutevalueTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_miinus_8(self):
        with patch('builtins.input', return_value = '-8'):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue('The absolute value of this number is 8' in output, "with input -8 your program should print out\nThe absolute value of this number is 8\nyour program printed out\n"+ output)

    def test_additional_tests(self):
        testset = ['-99', '4', '435634', '-234', '6', '0']
        for number in testset:
            with patch('builtins.input', return_value = number):
                reload_module(self.module)
                result = number[1:-1] if int(number)<0 else number
                self.assertTrue(result in get_stdout(), 'Your program works incorrectly with input ' + number + '. Answer should be ' + result)

if __name__ == '__main__':
    unittest.main()
