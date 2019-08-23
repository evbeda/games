# Modules
import unittest
from unittest.mock import patch
from parameterized import parameterized
# Model
from ..model.game import DungeonRaidersGame
from ..model.rooms.wound_room import WoundRoom
from ..model.rooms.treasure import Treasure
from ..model.rooms.gold_room import GoldRoom
from ..model.rooms.monster_room import MonsterRoom
from ..model.rooms.room import Room
# Messages
from ..model import BYE_MESSAGE, EXIT, GAME_OVER, LEVEL_FINISHED_MESSAGE, INPUT_NUMBER
from . import BOARD_EXAMPLE
from . import BOARD_EXAMPLE_TWO_WINNERS
from . import BOARD_EXAMPLE_WINNER
from . import FIRST_LEVEL_EXAMPLE
from . import NEXT_TURN_WOUNDROOM_EXAMPLE
from . import NEXT_TURN_TREASURE_EXAMPLE
from . import NEXT_TURN_GOLDROOM_EXAMPLE
from . import NEXT_TURN_MONSTERROOM_EXAMPLE
from . import PLAYERS_EXAMPLE
from . import PLAYERS_EXAMPLE_TWO_WINNERS


class TestDungeon(unittest.TestCase):
    # """ -------------------- Game tests -------------------- """
    def test_check_if_game_has_5_levels(self):
        game = DungeonRaidersGame()
        self.assertEqual(5, len(game.create_levels()))

    def test_check_if_game_has_3_players(self):
        game = DungeonRaidersGame()
        self.assertEqual(3, len(game.create_players()))

    @parameterized.expand([
        ([50, 10], [40, 20], [60, 20], [1, 2], [0, 1, 2], [2]),
        ([60, 10], [40, 20], [60, 20], [1, 2], [0, 1, 2], [0]),
        ([60, 10], [40, 20], [60, 10], [1], [0, 2], [0, 2]),
        ([60, 10], [60, 10], [60, 10], [0, 1, 2], [0, 1, 2], [0, 1, 2]),
    ])
    def test_check_resolve_game(self, player1, player2, player3,
                                max_wound, finalists, winner):
        game = DungeonRaidersGame()
        game.players[0].gold = player1[0]
        game.players[0].wounds = player1[1]
        game.players[1].gold = player2[0]
        game.players[1].wounds = player2[1]
        game.players[2].gold = player3[0]
        game.players[2].wounds = player3[1]
        expected_max_wound = [player for player in game.players
                              if game.players.index(player) in max_wound]
        expected_finalists = [player for player in game.players
                              if game.players.index(player) in finalists]
        expected_winners = [player for player in game.players
                            if game.players.index(player) in winner]
        # players_with_max_wounds
        players_max_wound = game.get_players_with_max_wounds(game.players)
        self.assertEqual(players_max_wound, expected_max_wound)
        # finalists
        finalists = game.get_finalists()
        self.assertEqual(finalists, expected_finalists)
        # winner/winner
        winners = game.resolve_game()
        self.assertEqual(winners, expected_winners)

    @patch(
        'dungeon_raiders.model.game.DungeonRaidersGame.create_levels',
        return_value=FIRST_LEVEL_EXAMPLE
        )
    @patch(
        'dungeon_raiders.model.game.DungeonRaidersGame.create_players',
        return_value=PLAYERS_EXAMPLE
    )
    def test_board(self, _, _a):
        game = DungeonRaidersGame()
        self.assertEqual(BOARD_EXAMPLE, game.board)

    @patch(
        'dungeon_raiders.model.game.DungeonRaidersGame.create_players',
        return_value=PLAYERS_EXAMPLE
        )
    def test_board_is_game_over(self, _):
        game = DungeonRaidersGame()
        game.finish()
        self.assertIn(BOARD_EXAMPLE_WINNER, game.board)

    @patch(
        'dungeon_raiders.model.game.DungeonRaidersGame.create_players',
        return_value=PLAYERS_EXAMPLE_TWO_WINNERS
        )
    def test_board_is_game_over_two_winners(self, _):
        game = DungeonRaidersGame()
        game.finish()
        self.assertIn(BOARD_EXAMPLE_TWO_WINNERS, game.board)

    def test_next_turn_monster_room(self):
        game = DungeonRaidersGame()
        game.current_level.actual_room = MonsterRoom((11, 3, 'Esqueleto'))
        self.assertEqual(NEXT_TURN_MONSTERROOM_EXAMPLE, game.next_turn())

    @parameterized.expand([
        (NEXT_TURN_MONSTERROOM_EXAMPLE, MonsterRoom((11, 3, 'Esqueleto'))),
        (NEXT_TURN_GOLDROOM_EXAMPLE, GoldRoom(
            ['Caldero de lava', [(5, 3), (4, 2), (3, 1)]])),
        (NEXT_TURN_WOUNDROOM_EXAMPLE, WoundRoom(
            ['Trampa de pinchos', [(5, 2), (4, 2), (3, 1)]])),
        (NEXT_TURN_TREASURE_EXAMPLE, Treasure((4, 2))),
        ])
    def test_next_turn_gold_room(self, example, room):
        game = DungeonRaidersGame()
        game.current_level.actual_room = room
        self.assertEqual(example, game.next_turn())

    # Test for play method
    def test_command_exit(self):
        game = DungeonRaidersGame()
        self.assertEqual(BYE_MESSAGE, game.play(EXIT))

    def test_you_cant_play_2_again(self):
        game = DungeonRaidersGame()
        game.play(2)
        self.assertEqual('You can\'t play a 2 again', game.play(2))

    @parameterized.expand([
        ("",),
        ("a",),
    ])
    def test_not_a_number(self, number):
        game = DungeonRaidersGame()
        self.assertEqual(INPUT_NUMBER, game.play(number))

    def test_game_over(self):
        game = DungeonRaidersGame()
        game.index_current_level = 4
        game.current_level.index_actual_room = 4
        self.assertIn(GAME_OVER, game.play(3))

    def test_game_is_playing(self):
        game = DungeonRaidersGame()
        self.assertTrue(game.is_playing)
        game.play(EXIT)
        self.assertFalse(game.is_playing)

    def test_level_finished(self):
        game = DungeonRaidersGame()
        # play 4 cards
        for card in range(1, 5):
            game.play(card)
        self.assertIn(LEVEL_FINISHED_MESSAGE, game.play(5))

    # Test for Room
    def test_not_possible_to_resolve_room_in_room(self):
        room = Room()
        with self.assertRaises(NotImplementedError):
            room.resolve_room([])
