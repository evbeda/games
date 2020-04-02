import unittest

from .token import Token
from .tower import Tower
from .tower import InvalidMovement
from .tower import EmptyTower
from .hanoi_towers import HanoiTowers
from .hanoi_towers import SameTowerException
from .hanoi_towers import NotValidTowerIndexException


class TestHanoiTower(unittest.TestCase):

    def setUp(self):
        self.hanoi_towers = HanoiTowers(4)

    def test_init_game(self):
        self.assertEqual(len(self.hanoi_towers.towers[0].tokens), 4)
        self.assertEqual(len(self.hanoi_towers.towers[1].tokens), 0)
        self.assertEqual(len(self.hanoi_towers.towers[2].tokens), 0)
        self.assertTrue(self.hanoi_towers.is_playing)

    def test_next_turn_win(self):
        token1 = Token(1)
        token2 = Token(2)
        token3 = Token(3)
        token4 = Token(4)
        self.hanoi_towers.is_playing = False
        self.hanoi_towers.towers[2].insert_token(token4)
        self.hanoi_towers.towers[2].insert_token(token3)
        self.hanoi_towers.towers[2].insert_token(token2)
        self.hanoi_towers.towers[2].insert_token(token1)
        self.assertEqual(self.hanoi_towers.next_turn(), "You won")

    def test_play_and_win(self):
        token2 = Token(2)
        token3 = Token(3)
        token4 = Token(4)
        self.hanoi_towers.towers[2].insert_token(token4)
        self.hanoi_towers.towers[2].insert_token(token3)
        self.hanoi_towers.towers[2].insert_token(token2)
        result = self.hanoi_towers.play(0, 2)
        self.assertEqual(result, "You won")
        self.assertFalse(self.hanoi_towers.is_playing)

    def test_next_turn_still_playing(self):
        self.assertEqual(self.hanoi_towers.next_turn(), "Enter the numbers of source and target towers")
        self.assertTrue(self.hanoi_towers.is_playing)

    def test_play_right_move(self):
        self.hanoi_towers.play(0, 1)
        self.assertEqual(len(self.hanoi_towers.towers[0].tokens), 3)
        self.assertEqual(len(self.hanoi_towers.towers[1].tokens), 1)
        self.assertEqual(len(self.hanoi_towers.towers[2].tokens), 0)

    def test_play_invalid_move(self):
        self.hanoi_towers.play(0, 1)
        self.assertEqual(self.hanoi_towers.play(0, 1), "Invalid move")

    def test_play_invalid_move_tokens(self):
        self.hanoi_towers.play(0, 1)
        self.hanoi_towers.play(0, 1)
        self.assertEqual(len(self.hanoi_towers.towers[0].tokens), 3)
        self.assertEqual(len(self.hanoi_towers.towers[1].tokens), 1)

    def test_play_empty_tower(self):
        self.assertEqual(self.hanoi_towers.play(1, 2), "Empty tower")

    def test_play_empty_tower_tokens(self):
        self.hanoi_towers.play(1, 2)
        self.assertEqual(len(self.hanoi_towers.towers[1].tokens), 0)
        self.assertEqual(len(self.hanoi_towers.towers[2].tokens), 0)

    def test_board_display(self):
        expected_board = \
            "                  - | -                                      |                                        |                    \n" \
            "                - - | - -                                    |                                        |                    \n" \
            "              - - - | - - -                                  |                                        |                    \n" \
            "            - - - - | - - - -                                |                                        |                    \n" \

        self.assertEqual(self.hanoi_towers.board, expected_board)

    def test_board_display_after_play(self):
        self.hanoi_towers.play(0, 1)
        expected_board = \
            "                    |                                        |                                        |                    \n" \
            "                - - | - -                                    |                                        |                    \n" \
            "              - - - | - - -                                  |                                        |                    \n" \
            "            - - - - | - - - -                              - | -                                      |                    \n" \

        self.assertEqual(self.hanoi_towers.board, expected_board)

    def test_play_same_2_towers(self):
        result_text = self.hanoi_towers.play(0, 0)
        self.assertEqual(result_text, "Error: the towers must be different")

    def test_validate_non_integer_input(self):
        result = self.hanoi_towers.play("A", 3)
        self.assertEqual(result, "Error: enter only integers")

    def test_validate_input_different_towers(self):
        result = self.hanoi_towers.validate_input(0, 1)
        self.assertEqual(result, True)

    def test_validate_input_same_both_towers(self):
        with self.assertRaises(SameTowerException):
            self.hanoi_towers.validate_input(1, 1)

    def test_validate_input_towers_out_index(self):
        with self.assertRaises(NotValidTowerIndexException):
            self.hanoi_towers.validate_input(5, 1)

    def test_play_towers_out_index(self):
        result = self.hanoi_towers.play(0, 7)
        self.assertEqual(result, "Error: enter numbers between 0 and 2")


class TestToken(unittest.TestCase):

    def test_token_basic_info(self):
        token = Token(5)
        self.assertEqual(token.size, 5)


class TestTower(unittest.TestCase):

    def setUp(self):
        self.token_1 = Token(1)
        self.token_4 = Token(4)
        self.tower = Tower()
        self.tower4 = Tower(4)

    def test_tower_basic_info(self):
        self.assertEqual(len(self.tower.tokens), 0)

    def test_tower_with_tokens(self):
        self.assertEqual(self.tower4.tokens[0].size, 4)
        self.assertEqual(self.tower4.tokens[1].size, 3)
        self.assertEqual(self.tower4.tokens[2].size, 2)
        self.assertEqual(self.tower4.tokens[3].size, 1)
        self.assertEqual(len(self.tower4.tokens), 4)

    def test_validate_insert_token_empty_tokens(self):
        self.assertTrue(self.tower.validate_insert_token(self.token_1))

    def test_validate_insert_token_valid_tokens(self):
        self.tower.tokens.append(self.token_4)
        self.assertTrue(self.tower.validate_insert_token(self.token_1))

    def test_validate_insert_token_invalid_tokens(self):
        self.tower.tokens.append(self.token_1)
        self.assertFalse(self.tower.validate_insert_token(self.token_4))

    def test_tower_insert_token_to_empty_tower(self):
        self.tower.insert_token(self.token_1)
        self.assertEqual(len(self.tower.tokens), 1)

    def test_tower_insert_token_to_valid_tower(self):
        self.tower.tokens.append(Token(3))
        self.tower.insert_token(self.token_1)
        self.assertEqual(len(self.tower.tokens), 2)

    def test_tower_insert_token_to_invalid_tower(self):
        self.tower.tokens.append(Token(2))
        with self.assertRaises(InvalidMovement):
            self.tower.insert_token(self.token_4)
        self.assertEqual(len(self.tower.tokens), 1)

    def test_remove_token(self):
        self.assertEqual(self.tower4.tokens[-1], self.tower4.remove_token())
        self.assertEqual(len(self.tower4.tokens), 3)

    def test_remove_token_empty_tower(self):
        with self.assertRaises(EmptyTower):
            self.tower.remove_token()
