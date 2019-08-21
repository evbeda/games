import unittest
from unittest.mock import patch
from game import GameBattleship
from .player import PlayerCPU, PlayerHuman
from .game import game_states, possible_turn
from .board import Board


class TestBattleship(unittest.TestCase):

    def setUp(self):
        self.game = GameBattleship()
        input_user = [
            '1, 1, 1, vertical',
            '1, 2, 2, vertical',
            '1, 3, 3, vertical',
            '1, 4, 3, vertical',
            '1, 5, 4, vertical',
            '1, 6, 5, vertical',
        ]
        board = Board()
        board_table = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 2, 31, 32, 4, 5, 0, 0, 0],
            [0, 0, 2, 31, 32, 4, 5, 0, 0, 0],
            [0, 0, 0, 31, 32, 4, 5, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 4, 5, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        board.set_board(board_table)
        self.game.play(1, 1, 1, 'vertical')
        self.game.play(1, 2, 2, 'vertical')
        self.game.play(1, 3, 3, 'vertical')
        self.game.play(1, 4, 3, 'vertical')
        self.game.play(1, 5, 4, 'vertical')
        self.game.play(1, 6, 5, 'vertical')
        # for single_input in input_user:
        #     self.game.play(single_input)
        self.game.player_cpu.board_own.set_board(board)

    def test_shoot_water(self):
        board = Board()
        result = board.shoot(3, 3)
        self.assertEqual(result, "water")

    def test_shoot_sunked_1(self):
        board = Board()
        board.set_boat(1, 1, 1, "horizontal")
        result = board.shoot(1, 1)
        self.assertEqual(result, "sunked")

    def test_shoot_sunked_2(self):
        board = Board()
        result = []
        board.set_boat(0, 0, 2, "horizontal")
        for i in range(0, 2):
            result.append(board.shoot(0, i))
        self.assertEqual(result[len(result) - 1], "sunked")

    def test_shoot_sunked_31(self):
        board = Board()
        result = []
        board.set_boat(1, 2, 3, "vertical")
        for i in range(1, 4):
            result.append(board.shoot(i, 2))
        self.assertEqual(result[len(result) - 1], "sunked")

    def test_shoot_sunked_32(self):
        board = Board()
        result = []
        board.set_boat(5, 7, 3, "horizontal")
        for i in range(7, 10):
            result.append(board.shoot(5, i))
        self.assertEqual(result[len(result) - 1], "sunked")

    def test_shoot_sunked_4(self):
        board = Board()
        result = []
        result2 = []
        result3 = []
        board.set_boat(9, 5, 4, "horizontal")
        for i in range(5, 9):
            result.append(board.shoot(9, i))
        board.set_boat(0, 0, 3, "horizontal")
        for i in range(0, 1):
            result2.append(board.shoot(0, i))
        board.set_boat(4, 5, 3, "horizontal")
        for i in range(5, 8):
            result3.append(board.shoot(4, i))
        self.assertEqual(result[len(result) - 1], "sunked")
        self.assertEqual(result2[len(result2) - 1], "hit")
        self.assertEqual(result3[len(result3) - 1], "sunked")

    def test_shoot_sunked_5(self):
        board = Board()
        result = []
        board.set_boat(5, 5, 5, "vertical")
        for i in range(5, 10):
            result.append(board.shoot(i, 5))
        self.assertEqual(result[len(result) - 1], "sunked")

    def test_player_boards(self):
        player = PlayerHuman()
        result = player.get_boards()
        self.assertEqual(len(result), 2)

    def test_game_players(self):
        game = GameBattleship()
        result = game.get_players()
        self.assertEqual(len(result), 2)

    def test_own_board_is_ready_cpu(self):
        p1 = PlayerCPU()
        p1.fill_own_board()
        result = p1.board_own.state
        self.assertEqual(result, 'ready_to_war')

    def test_own_board_false(self):
        p1 = PlayerCPU()
        board = Board()
        p1.board_own = board
        p1.board_own.state = board.board_states[1]
        result = p1.fill_own_board()
        self.assertFalse(result)

    def test_game_state_init(self):
        game = GameBattleship()
        result = game.state
        self.assertEqual(result, 'init')

    def test_game_state_war(self):
        # Ir corriendo cada uno de los inputs del user
        self.game.set_boat('1 1 1 vertical')
        self.game.set_boat('1 2 2 vertical')
        self.game.set_boat('1 3 3 vertical')
        self.game.set_boat('1 4 3 vertical')
        self.game.set_boat('1 5 4 vertical')
        self.game.set_boat('1 6 5 vertical')
        result = self.game.state
        self.assertEqual(result, 'war')

    def test_turn_init_player_boat_not_set_that_position(self):
        game = GameBattleship()
        result = game.set_boat([9, 9, 5, 'vertical'])
        self.assertEqual(result, 'Your boat could not be set in that position')

    def test_turn_init_player_wrong_param_amount_of(self):
        game = GameBattleship()
        result = game.set_boat([1, 1, 1, 'vertical', 'hdgsjhgdashjd'])
        self.assertEqual(result, 'error, mas parametros de los requeridos (4)')

    def test_turn_war_player(self):
        game = GameBattleship()
        result = game.set_boat([1, 2, 1, 'vertical'])
        self.assertTrue(result)

    def test_turn_war_player_wrong_param_letter(self):
        game = GameBattleship()
        result = game.play('A', 'B', 1, 'vertical')
        self.assertEqual(result, 'error')

    def test_turn_war_player_wrong_number(self):
        game = GameBattleship()
        result = game.player_human.put_boat_own_board(
            10,
            1,
            1,
            "vertical",
        )
        self.assertFalse(result)

    def test_game_war_player_can_sunk_boat_player_cpu(self):
        board_cpu = Board()
        board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        board_cpu.set_board(board)
        self.game.state = game_states[1]
        self.game.player_cpu.board_own = board_cpu
        expected = ['Congratulations! You sunk a boat.']
        result = self.game.play(0, 0)
        self.assertEqual(expected, result)

    @patch('battleship.player.PlayerCPU.pick_coordenate')
    def test_game_war_player_can_water_boat_player_cpu(self, mock_pick_coordenate):
        board_cpu = Board()
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        board_cpu.set_board(board)
        self.game.player_cpu.board_own = board_cpu
        self.game.turn = possible_turn[0]
        self.game.state = game_states[1]
        expected = ['You only hit water! CPU turn', 'Water! Now is your turn.']
        mock_pick_coordenate.return_value = [0, 0]
        result = self.game.play(0, 0)
        self.assertEqual(expected, result)

    def test_game_war_player_can_hit_boat_player_cpu(self):
        board_cpu = Board()
        board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        board_cpu.set_board(board)
        self.game.player_cpu.board_own = board_cpu
        expected = ['You hit a boat']
        self.game.state = game_states[1]
        result = self.game.play(2, 2)
        self.assertEqual(expected, result)

    def test_game_dont_change_state(self):
        board_cpu = Board()
        board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        board_cpu.set_board(board)
        self.game.player_cpu.board_own = board_cpu
        expected = self.game.state
        self.game.play(1, 2)
        self.assertEqual(expected, self.game.state)

    @patch('battleship.player.PlayerCPU.pick_coordenate')
    def test_game_check_cpu_sunk(self, mock_pick_coordenate):
        self.game.state = game_states[1]
        self.game.turn = 'cpu'
        self.game.player_human.board_own.sunked.append(2)
        result = self.game.player_human.board_own.shoot(2, 2)
        self.assertEqual('sunked', result)

    @patch('battleship.player.PlayerCPU.pick_coordenate')
    def test_game_check_cpu_hit(self, mock_pick_coordenate):
        self.game.state = game_states[1]
        self.game.turn = 'cpu'
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.game.player_human.board_own.set_board(board)
        mock_pick_coordenate.return_value = [2, 2]
        result = self.game.play()
        self.assertEqual(['Your boat was hit.'], result)

    @patch('battleship.player.PlayerCPU.pick_coordenate')
    def test_game_check_cpu_wins(self, mock_pick_coordenate):
        board_human = Board()
        board_table = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        board_human.set_board(board_table)
        self.game.player_human.board_own = board_human
        self.game_states = game_states[1]
        self.game.turn = 'cpu'
        mock_pick_coordenate.return_value = [0, 0]
        result = self.game.play()
        self.assertEqual(['Your boat was sunk.', 'You lose.'], result)



    @patch('battleship.player.PlayerCPU.pick_coordenate')
    def test_game_check_cpu_water(self, mock_pick_coordenate):
        self.game.state = game_states[1]
        self.game.turn = 'cpu'
        mock_pick_coordenate.return_value = [0, 0]
        result = self.game.player_human.board_own.shoot(0, 0)
        self.assertEqual('water', result)

    def test_player_cpu_pick_coordenate(self):
        cpu_player = PlayerCPU()
        coordenate = cpu_player.pick_coordenate()
        self.assertTrue(0 <= coordenate[0] < 10)
        self.assertTrue(0 <= coordenate[1] < 10)

    def test_doblehit(self):
        board_cpu = Board()
        board_cpu.shoot(0, 1)
        result = board_cpu.shoot(0, 1)
        self.assertEqual(result, 'already shoot')

    @patch('battleship.player.PlayerCPU.pick_coordenate')
    def test_player_cpu_return_messages(self, mock_pick_coordenate):
        self.game.state = game_states[1]
        self.game.turn = 'cpu'
        mock_pick_coordenate.return_value = [1, 1]
        self.game.play('')
        mock_pick_coordenate.return_value = [1, 2]
        self.game.play('')
        mock_pick_coordenate.return_value = [2, 2]
        self.game.play('')
        mock_pick_coordenate.return_value = [9, 9]
        result = self.game.play('')
        expected = ['Your boat was sunk.', 'Your boat was hit.', 'Your boat was sunk.', 'Water! Now is your turn.']
        self.assertEqual(expected, result)

    def test_next_turn_init(self):
        game = GameBattleship()
        result = game.next_turn()
        expected = 'pone el barco (x y boat horizontal/vertical)'
        self.assertEqual(expected, result)

    def test_next_turn_war_start(self):
        self.game.state = game_states[1]
        self.game.turn = 'human'
        result = self.game.next_turn()
        expected = 'shoot (x y)'
        self.assertEqual(expected, result)

    def test_next_turn_cpu_win(self):
        self.game.state = game_states[2]
        result = self.game.next_turn()
        expected = 'gano el cpu'
        self.assertEqual(expected, result)

    def test_next_turn_human_win(self):
        self.game.state = game_states[3]
        result = self.game.next_turn()
        expected = 'ganaste'
        self.assertEqual(expected, result)

    @patch('battleship.player.PlayerCPU.pick_coordenate')
    def test_play_human_water(self, mock_pick_coordenate):
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.game.player_cpu.board_own.set_board(board)
        self.game.state = game_states[1]
        self.game.turn = 'human'
        mock_pick_coordenate.return_value = [1, 1]
        result = self.game.play(0, 0)
        expected = ['You only hit water! CPU turn', 'Your boat was sunk.']
        self.assertEqual(result, expected)

    def test_play_human_wrong_param_amount_of(self):
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.game.player_cpu.board_own.set_board(board)
        self.game.state = game_states[1]
        self.game.turn = 'human'
        result = self.game.war_human([0, 0, 0])
        expected = 'error, mas parametros de los requeridos (2)'
        self.assertEqual(result, expected)

    def test_play_human_already_shoot(self):
        board = [
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 4, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 4, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 4, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 4, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.game.player_cpu.board_own.set_board(board)
        self.game.state = game_states[1]
        self.game.turn = 'human'
        result = self.game.play(0, 0)
        expected = ['You already shoot in this place. Try again']
        self.assertEqual(result, expected)

    def test_play_human_win(self):
        board = [
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
            [0, 0, 0, 0, 0, 9, 0, 0, 0, 9],
            [0, 0, 9, 0, 0, 9, 0, 0, 0, 9],
            [0, 0, 9, 0, 0, 9, 0, 0, 0, 9],
            [0, 0, 9, 0, 0, 2, 2, 0, 0, 0],
            [0, 0, 9, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 9, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 9, 9, 9, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.game.player_cpu.board_own.set_board(board)
        self.game.state = game_states[1]
        self.game.turn = 'human'
        self.game.play(5, 5)
        result = self.game.play(5, 6)
        expected = ['Congratulations! You sunk a boat.', 'You Win']
        self.assertEqual(result, expected)
        self.assertFalse(self.game.player_cpu.board_own.there_are_boats())

    def test_board_shown(self):
        result = self.game.board
        expected = '\n'\
                   'Own Board (Player)\n'\
                   ' y 0 1 2 3 4 5 6 7 8 9\n'\
                   'x  \n'\
                   '0 |0|0|0|0|0|0|0|0|0|0|\n'\
                   '1 |0|1|2|3|3|4|5|0|0|0|\n'\
                   '2 |0|0|2|3|3|4|5|0|0|0|\n'\
                   '3 |0|0|0|3|3|4|5|0|0|0|\n'\
                   '4 |0|0|0|0|0|4|5|0|0|0|\n'\
                   '5 |0|0|0|0|0|0|5|0|0|0|\n'\
                   '6 |0|0|0|0|0|0|0|0|0|0|\n'\
                   '7 |0|0|0|0|0|0|0|0|0|0|\n'\
                   '8 |0|0|0|0|0|0|0|0|0|0|\n'\
                   '9 |0|0|0|0|0|0|0|0|0|0|\n'\
                   '\n'\
                   'Opponent Board (CPU)\n'\
                   ' y 0 1 2 3 4 5 6 7 8 9\n'\
                   'x  \n'\
                   '0 |0|0|0|0|0|0|0|0|0|0|\n'\
                   '1 |0|0|0|0|0|0|0|0|0|0|\n'\
                   '2 |0|0|0|0|0|0|0|0|0|0|\n'\
                   '3 |0|0|0|0|0|0|0|0|0|0|\n'\
                   '4 |0|0|0|0|0|0|0|0|0|0|\n'\
                   '5 |0|0|0|0|0|0|0|0|0|0|\n'\
                   '6 |0|0|0|0|0|0|0|0|0|0|\n'\
                   '7 |0|0|0|0|0|0|0|0|0|0|\n'\
                   '8 |0|0|0|0|0|0|0|0|0|0|\n'\
                   '9 |0|0|0|0|0|0|0|0|0|0|\n'
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
