import unittest
from parameterized import parameterized
from ..model.player import Player


class TestPlayer(unittest.TestCase):

    @parameterized.expand([
        ("Caballero, wounds: 1, gold: 5", ('Caballero', 1, 5)),
        ("Explorador, wounds: 3, gold: 0", ('Explorador', 3, 0)),
        ("Hechicero, wounds: 0, gold: 2", ('Hechicero', 0, 2)),
    ])
    def test_player_status(self, expected, character):
        player = Player(character=character)
        self.assertEqual(player.status, expected)
