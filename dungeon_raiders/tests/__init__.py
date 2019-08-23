import unittest
from ..model.player import Player
from ..model.hand_player import HandPlayer
from ..model.rooms.monster_room import MonsterRoom
from ..model.rooms.treasure import Treasure
from ..model.rooms.gold_room import GoldRoom


BOARD_EXAMPLE = '''===================================================
Level: 1
Rooms:
 * Esqueleto (❤️ 11, 🗡️️ 3) <--
 * Treasure (💰 4, 💰 2)
 * Hidden
 * Dragon (❤️ 14, 🗡️️ 3)
 * Hidden

Players status:
Caballero, wounds: 1, gold: 1
Exploradora, wounds: 3, gold: 2
Guerrero, wounds: 2, gold: 0
'''

BOARD_EXAMPLE_WINNER = '''Winner:
Caballero, wounds: 1, gold: 1
'''

BOARD_EXAMPLE_TWO_WINNERS = '''Winners:
Caballero, wounds: 1, gold: 5
Exploradora, wounds: 1, gold: 5
'''

NEXT_TURN_WOUNDROOM_EXAMPLE = '''Room name: Trampa de pinchos
Card: 5 Wound: 2
Card: 4 Wound: 2
Card: 3 Wound: 1

Playable cards: 1, 2, 3, 4, 5'''

NEXT_TURN_TREASURE_EXAMPLE = '''Room name: Treasure
First winner: 4
Second winner: 2

Playable cards: 1, 2, 3, 4, 5'''

NEXT_TURN_GOLDROOM_EXAMPLE = '''Room name: Caldero de lava
Max played: 5 Gold: 3
Max played: 4 Gold: 2
Max played: 3 Gold: 1

Playable cards: 1, 2, 3, 4, 5'''

NEXT_TURN_MONSTERROOM_EXAMPLE = '''Room name: Esqueleto
Life: 11
Damage: 3

Playable cards: 1, 2, 3, 4, 5'''

ROOMS_EXAMPLE = [
    MonsterRoom((11, 3, 'Esqueleto')),
    Treasure((4, 2)),
    GoldRoom(['Caldero de lava', [(5, 3), (4, 2), (3, 1)]]),
    MonsterRoom((14, 3, 'Dragon')),
    Treasure((3, 2)),
]

PLAYERS_EXAMPLE = [
    Player(character=['Caballero', 1, 1]),
    Player(character=['Exploradora', 3, 2]),
    Player(character=['Guerrero', 2, 0]),
]

PLAYERS_EXAMPLE_TWO_WINNERS = [
    Player(character=['Caballero', 1, 5]),
    Player(character=['Exploradora', 1, 5]),
    Player(character=['Guerrero', 2, 0]),
]


class RoomHelper(unittest.TestCase):

    @staticmethod
    def _get_players_example():
        return[
            Player(character=['Caballero', 1, 1]),
            Player(character=['Exploradora', 3, 2]),
            Player(character=['Guerrero', 2, 0]),
        ]

    @staticmethod
    def _get_hands():
        player_a, player_b, player_c = RoomHelper._get_players_example()
        player_a.gold = 5
        player_a.wounds = 5
        player_b.gold = 3
        player_b.wounds = 3
        player_c.gold = 0
        player_c.wounds = 0

        return HandPlayer(player_a), HandPlayer(player_b), \
            HandPlayer(player_c)

    @staticmethod
    def _play_cards_against_room(room, plays):
        hands = RoomHelper._get_hands()

        for hand in hands:
            hand.play(str(plays[hands.index(hand)]))
        return hands, RoomHelper._play(room, hands)

    @staticmethod
    def _play(room, hands):
        return room.resolve_room(hands)
