import unittest
from unittest.mock import patch
from ..dice import Dice


class TestDice(unittest.TestCase):
    def setUp(self):
        self.t_dice = Dice('white')

    def test_random_dice(self):
        with patch('random.randint', return_value=3) as randint_patched:
            self.t_dice.roll_dice()
            self.assertEqual(self.t_dice.value, 3)
            randint_patched.assert_called_once_with(1, 6)

    def test_has_color(self):
        self.assertEqual(self.t_dice.color, 'white')
