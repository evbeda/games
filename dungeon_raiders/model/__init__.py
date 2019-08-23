from .rooms.monster_room import MonsterRoom
from .rooms.treasure import Treasure
from .rooms.gold_room import GoldRoom
from .rooms.wound_room import WoundRoom

EXIT = 'EXIT'
BYE_MESSAGE = 'Bye'
GAME_OVER = 'Game over'
LEVEL_FINISHED_MESSAGE = 'Level finished succesfully'
INPUT_NUMBER = 'Input EXIT or a number'

MONSTER_ROOM = 0
TREASURE_ROOM = 1
GOLD_TRAP_ROOM = 2
WOUND_TRAP_ROOM = 3

MONSTERS = [
    (14, 1, 'La Cosa'),
    (11, 3, 'Esqueleto'),
    (8, 3, 'Serpiente'),
    (11, 1, 'Zombi'),
    (11, 1, 'Zombi'),
    (11, 2, 'Goblin'),
    (11, 2, 'Goblin'),
    (14, 2, 'Troll'),
    (14, 2, 'Troll'),
    (14, 3, 'Dragon'),
    (14, 3, 'Dragon'),
]

TREASURES = [
    (4, 2), (4, 2), (4, 0), (3, 2), (3, 2),
    (3, 0), (2, 1), (2, 1), (2, 0), (1, 0),
]

GOLDS = [
    ('Caldero de lava', [(5, 3), (4, 2), (3, 1)]),
    ('Atrapa monedas', [(5, 2), (4, 2), (3, 1), (2, 1)]),
]

WOUNDS = [
    ('Trampa de pinchos', [(5, 2), (4, 2), (3, 1)]),
    ('Roca gigante', [(5, 2), (4, 1), (3, 1), (2, 1)]),
]

CHARACTER = [
    ('Hechicero', 1, 1),
    ('Exploradora', 3, 2),
    ('Guerrero', 2, 0),
    ('Ladrona', 2, 2),
    ('Caballero', 1, 1),
    ]

ROOMS = [MonsterRoom(monster) for monster in MONSTERS] \
        + [Treasure(treasure) for treasure in TREASURES] \
        + [GoldRoom(gold) for gold in GOLDS] \
        + [WoundRoom(wound) for wound in WOUNDS]

LEVEL_CARDS = [
    (True, False, True, False, False),
    (True, False, False, True, False),
    (True, True, True, True, False),
    (True, True, False, False, True),
    (True, True, False, False, False),
    (True, True, False, True, False),
    (True, False, False, False, True),
]
