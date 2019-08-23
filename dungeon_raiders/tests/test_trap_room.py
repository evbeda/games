from parameterized import parameterized
from ..model import GOLDS, WOUNDS
from . import RoomHelper
from ..model.rooms.gold_room import GoldRoom
from ..model.rooms.wound_room import WoundRoom
from ..model.rooms.trap import Trap

WOUND_SCENARIOS = [
    ([5, 3, 0], WoundRoom(WOUNDS[0]), [1, 1, 1]),
    ([5, 3, 0], WoundRoom(WOUNDS[0]), [2, 1, 1]),
    ([5, 3, 1], WoundRoom(WOUNDS[0]), [3, 1, 1]),
    ([5, 3, 2], WoundRoom(WOUNDS[0]), [4, 1, 2]),
    ([5, 3, 2], WoundRoom(WOUNDS[0]), [5, 2, 3]),
    ([5, 3, 0], WoundRoom(WOUNDS[1]), [1, 1, 1]),
    ([5, 3, 1], WoundRoom(WOUNDS[1]), [2, 1, 1]),
    ([5, 3, 1], WoundRoom(WOUNDS[1]), [3, 1, 2]),
    ([5, 3, 1], WoundRoom(WOUNDS[1]), [4, 1, 2]),
    ([5, 3, 2], WoundRoom(WOUNDS[1]), [5, 2, 3]),
]

GOLD_SCENARIOS = [
    ([5, 3, 0], GoldRoom(GOLDS[0]), [1, 1, 1]),
    ([5, 3, 0], GoldRoom(GOLDS[0]), [2, 1, 1]),
    ([4, 3, 0], GoldRoom(GOLDS[0]), [3, 1, 2]),
    ([3, 3, 0], GoldRoom(GOLDS[0]), [4, 1, 2]),
    ([2, 3, 0], GoldRoom(GOLDS[0]), [5, 2, 3]),
    ([5, 3, 0], GoldRoom(GOLDS[1]), [1, 1, 1]),
    ([4, 3, 0], GoldRoom(GOLDS[1]), [2, 1, 2]),
    ([4, 3, 0], GoldRoom(GOLDS[1]), [3, 2, 1]),
    ([3, 3, 0], GoldRoom(GOLDS[1]), [4, 1, 3]),
    ([3, 3, 0], GoldRoom(GOLDS[1]), [5, 5, 4]),
]

ALL_SCENARIOS = [
        ("Caballero lost 1 gold. ", GoldRoom(GOLDS[0]), [3, 1, 3]),
        ("Caballero lost 2 gold. ", GoldRoom(GOLDS[0]), [4, 1, 2]),
        ("Guerrero took 2 damage. ", WoundRoom(WOUNDS[0]), [4, 1, 2]),
        ("Guerrero took 1 damage. ", WoundRoom(WOUNDS[1]), [2, 1, 1]),
]


class TestTrapRoom(RoomHelper):
    def setUp(self):
        self.trap = Trap('', '')

    @parameterized.expand(ALL_SCENARIOS)
    def test_return_resolve_room(self, expected, room, plays):
        _, result = RoomHelper._play_cards_against_room(room, plays)
        self.assertEqual(expected, result)

    # """ -------------------- GoldRoom card --------------------"""
    @parameterized.expand(GOLD_SCENARIOS)
    def test_play_cards_against_gold_room(self, gold_values, room, plays):
        hands, _ = RoomHelper._play_cards_against_room(room, plays)
        self.assertEqual(gold_values, [hand.player.gold for hand in hands])

    # """ -------------------- WoundRoom card -------------------- """
    @parameterized.expand(WOUND_SCENARIOS)
    def test_play_cards_against_wound_room(self, wound_values, room, plays):
        hands, _ = RoomHelper._play_cards_against_room(room, plays)
        self.assertEqual(wound_values, [hand.player.wounds for hand in hands])

    def test_not_possible_to_resolve_room_in_trap(self):
        with self.assertRaises(NotImplementedError):
            self.trap.resolve_room([])

    def test_not_possible_to_determine_affected_players_in_trap(self):
        with self.assertRaises(NotImplementedError):
            self.trap.determine_affected_players()
