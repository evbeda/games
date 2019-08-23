import unittest
from .test_dungeon import TestDungeon
from .test_monster_room import TestMonsterRoom
from .test_trap_room import TestTrapRoom
from .test_treasure import TestTreasure
from .test_level import TestLevel
from .test_hand_player import TestHandPlayer
from .test_player import TestPlayer


def suite():
    test_suite = unittest.TestSuite()
    # DUNGEON RAIDERS
    test_suite.addTest(unittest.makeSuite(TestDungeon))
    test_suite.addTest(unittest.makeSuite(TestMonsterRoom))
    test_suite.addTest(unittest.makeSuite(TestTrapRoom))
    test_suite.addTest(unittest.makeSuite(TestTreasure))
    test_suite.addTest(unittest.makeSuite(TestLevel))
    test_suite.addTest(unittest.makeSuite(TestHandPlayer))
    test_suite.addTest(unittest.makeSuite(TestPlayer))
    return test_suite
