import unittest
import copy
from ..model.level import Level
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
Guerrero, wounds: 0, gold: 2
'''

BOARD_EXAMPLE_WINNER = '''Winner:
Guerrero, wounds: 0, gold: 2
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
    Treasure((3, 2))
]

PLAYERS_EXAMPLE = [
    Player(character=['Caballero', 1, 1]),
    Player(character=['Exploradora', 3, 2]),
    Player(character=['Guerrero', 0, 2]),
]

PLAYERS_EXAMPLE_INTEGRATION = [
    Player(character=['Caballero', 1, 1]),
    Player(character=['Exploradora', 3, 2]),
    Player(character=['Guerrero', 0, 2]),
]

PLAYERS_EXAMPLE_TWO_WINNERS = [
    Player(character=['Caballero', 1, 5]),
    Player(character=['Exploradora', 1, 5]),
    Player(character=['Guerrero', 2, 0]),
]

FIRST_LEVEL_EXAMPLE = [
    Level(
        copy.deepcopy(PLAYERS_EXAMPLE),
        1,
        copy.deepcopy(ROOMS_EXAMPLE[::-1]),
        (True, True, False, True, False)
    ),
    None,
    None,
    None,
    None
]

LAST_LEVEL_EXAMPLE_INTEGRATION = [
    None,
    None,
    None,
    None,
    Level(
        PLAYERS_EXAMPLE_INTEGRATION,
        5,
        copy.deepcopy(ROOMS_EXAMPLE),
        (True, False, False, False, True)
    )
]

INTEGRATION_TEST_OUTPUT = [
    '''===================================================
Level: 5
Rooms:
 * Treasure (💰 3, 💰 2) <--
 * Hidden
 * Hidden
 * Hidden
 * Esqueleto (❤️ 11, 🗡️️ 3)

Players status:
Caballero, wounds: 1, gold: 1
Exploradora, wounds: 3, gold: 2
Guerrero, wounds: 0, gold: 2
''',
    '''
Caballero played 1, Exploradora played 1, Guerrero played 2
Guerrero earnt 3 gold. Caballero and Exploradora earnt 1 gold.''',
    '''===================================================
Level: 5
Rooms:
 * Treasure (💰 3, 💰 2)
 * Dragon (❤️ 14, 🗡️️ 3) <--
 * Hidden
 * Hidden
 * Esqueleto (❤️ 11, 🗡️️ 3)

Players status:
Caballero, wounds: 1, gold: 2
Exploradora, wounds: 3, gold: 3
Guerrero, wounds: 0, gold: 5
''',
    '''
Caballero played 2, Exploradora played 3, Guerrero played 4
Dragon attacks. Caballero took 3 damage.''',
    '''===================================================
Level: 5
Rooms:
 * Treasure (💰 3, 💰 2)
 * Dragon (❤️ 14, 🗡️️ 3)
 * Caldero de lava (Gold) <--
 * Hidden
 * Esqueleto (❤️ 11, 🗡️️ 3)

Players status:
Caballero, wounds: 4, gold: 2
Exploradora, wounds: 3, gold: 3
Guerrero, wounds: 0, gold: 5
''',
    '''
Caballero played 3, Exploradora played 5, Guerrero played 1
Guerrero lost 3 gold. ''',
    '''===================================================
Level: 5
Rooms:
 * Treasure (💰 3, 💰 2)
 * Dragon (❤️ 14, 🗡️️ 3)
 * Caldero de lava (Gold)
 * Treasure (💰 4, 💰 2) <--
 * Esqueleto (❤️ 11, 🗡️️ 3)

Players status:
Caballero, wounds: 4, gold: 2
Exploradora, wounds: 3, gold: 3
Guerrero, wounds: 0, gold: 2
''',
    '''
Caballero played 4, Exploradora played 2, Guerrero played 3
Caballero earnt 4 gold. Guerrero earnt 2 gold.''',
    '''===================================================
Level: 5
Rooms:
 * Treasure (💰 3, 💰 2)
 * Dragon (❤️ 14, 🗡️️ 3)
 * Caldero de lava (Gold)
 * Treasure (💰 4, 💰 2)
 * Esqueleto (❤️ 11, 🗡️️ 3) <--

Players status:
Caballero, wounds: 4, gold: 6
Exploradora, wounds: 3, gold: 3
Guerrero, wounds: 0, gold: 4
''',
    '''
Caballero played 5, Exploradora played 4, Guerrero played 5
Esqueleto was beaten. No one took damage.
===================================================
Winner:
Guerrero, wounds: 0, gold: 4

Game over
===================================================
''',
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
