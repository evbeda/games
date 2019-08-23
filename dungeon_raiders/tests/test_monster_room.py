from parameterized import parameterized
from . import RoomHelper
from ..model.rooms.monster_room import MonsterRoom


class TestMonsterRoom(RoomHelper):
    """ -------------------- MonsterRoom card --------------------"""
    @parameterized.expand([
        # expected   , room against                   , cards played
        ([5, 3, 3], MonsterRoom([14, 3, 'La Cosa']), [5, 3, 1]),
        ([5, 3, 0], MonsterRoom([14, 3, 'sad']), [5, 5, 4]),
        ([5, 6, 3], MonsterRoom([14, 3, 'gre']), [3, 2, 2]),
    ])
    def test_play_check_wounds_against_monster_room(self, players_wounds,
                                                    monster, plays):
        hands, result = RoomHelper._play_cards_against_room(monster, plays)
        self.assertEqual(players_wounds, [hand.player.wounds for hand in hands])

    @parameterized.expand([
        ("La Cosa attacks. Guerrero took 1 damage.",
         MonsterRoom([14, 1, 'La Cosa']), [5, 3, 1]),
        ("sad was beaten. No one took damage.",
         MonsterRoom([14, 3, 'sad']), [5, 5, 4]),
        ("Troll attacks. Caballero and Exploradora took 2 damage.",
         MonsterRoom([14, 2, 'Troll']), [2, 2, 3]),
        ("gre attacks. Exploradora and Guerrero took 3 damage.",
         MonsterRoom([14, 3, 'gre']), [3, 2, 2]),
        ("Dragon attacks. Caballero, Exploradora and Guerrero took 3 damage.",
         MonsterRoom([14, 3, 'Dragon']), [2, 2, 2])
    ])
    def test_return_resolve_room(self, expected, monster, plays):
        _, result = RoomHelper._play_cards_against_room(monster, plays)
        self.assertEqual(expected, result)
