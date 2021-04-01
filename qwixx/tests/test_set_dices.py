import unittest
from unittest.mock import patch
from ..set_dices import SetDices
from ..dice import Dice


class TestSetDices(unittest.TestCase):
    def setUp(self):
        self.t_set_dices = SetDices()

    @patch('random.randint', return_value=3)
    def test_roll_dices(self, random_mock):
        # data
        values_test = {
            'white_1': 3,
            'white_2': 3,
            'red': 3,
            'yellow': 3,
            'blue': 3,
            'green': 3
        }
        # process
        values = {}
        self.t_set_dices.roll_dices()
        for die in self.t_set_dices.dices:
            values[die.color] = die.value
        # assert
        self.assertEqual(random_mock.call_count, 6)
        self.assertEqual(len(values), 6)
        self.assertEqual(values, values_test)

    def test_get_value_of_die(self):
        self.t_set_dices.dices = [
            Dice('white_1'),
            Dice('white_2'),
            Dice('red'),
        ]
        self.t_set_dices.dices[0].value = 5
        result = self.t_set_dices.get_value_of_die('white_1')
        self.assertEqual(result, 5)
