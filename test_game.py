from mock import patch
import unittest
from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

        class OutputCollector(object):
            def __init__(self, *args, **kwargs):
                self.output_collector = []

            def __call__(self, output):
                self.output_collector.append(output)

        self.output_collector = OutputCollector()

    def tearDown(self):
        pass

    @patch('game.Game.get_input', return_value='9')
    def test_quit_game(self, mock_input):
        with patch('game.Game.output', side_effect=self.output_collector):
            self.game.play()

        self.assertEquals(
            self.output_collector.output_collector,
            [],
        )

    def test_game_selection(self):
        self.assertEquals(
            self.game.game_inputs(),
            'Select Game\n'
            '0: Guess Number Game\n'
            '1: Tateti\n'
            '2: Buscaminas\n'
            '3: Cuatro en linea\n'
            '4: Damas\n'
            '5: Reversi\n'
            '9: to quit\n'
        )

    # def test_play_reversi(self):

    #     class ControlInputValues(object):
    #         def __init__(self, *args, **kwargs):
    #             self.played = False
    #             self.play_count = 0

    #         def __call__(self, console_output):
    #             if 'Select Game' in console_output:
    #                 if self.played:
    #                     return '9'
    #                 self.played = True
    #                 return '4'
    #             if '' in console_output:
    #                 game_turns = (
    #                     '0 0',
    #                     '1 0',
    #                     '0 1',
    #                     '1 1',
    #                     '0 2',
    #                 )
    #                 play = game_turns[self.play_count]
    #                 self.play_count += 1
    #                 return play

    #     with \
    #             patch('game.Game.get_input', side_effect=ControlInputValues()), \
    #             patch('game.Game.output', side_effect=self.output_collector):
    #         self.game.play()

    #     self.assertEquals(
    #         self.output_collector.output_collector,
    #         ['[]', 'you win'],
    #     )

    def test_play_guess_number_game(self):

        class ControlInputValues(object):
            def __init__(self, *args, **kwargs):
                self.played = False
                self.play_count = 0

            def __call__(self, console_output):
                if 'Select Game' in console_output:
                    if self.played:
                        return '9'
                    self.played = True
                    return '0'
                if 'Give me a number from 0 to 100' in console_output:
                    return '50'

        with \
                patch('game.Game.get_input', side_effect=ControlInputValues()), \
                patch('game.Game.output', side_effect=self.output_collector), \
                patch('guess_number_game.guess_number_game.randint', return_value=50):
            self.game.play()

        self.assertEquals(
            self.output_collector.output_collector,
            ['[]', 'you win'],
        )

    def test_play_tateti(self):

        class ControlInputValues(object):
            def __init__(self, *args, **kwargs):
                self.played = False
                self.play_count = 0

            def __call__(self, console_output):
                if 'Select Game' in console_output:
                    if self.played:
                        return '9'
                    self.played = True
                    return '1'
                if '' in console_output:
                    game_turns = (
                        '0 0',
                        '1 0',
                        '0 1',
                        '1 1',
                        '0 2',
                    )
                    play = game_turns[self.play_count]
                    self.play_count += 1
                    return play

        with \
            patch('game.Game.get_input', side_effect=ControlInputValues()), \
            patch('game.Game.get_input', side_effect=ControlInputValues()), \
                patch('game.Game.output', side_effect=self.output_collector):
            self.game.play()

        self.assertEquals(
            self.output_collector.output_collector,
            [
                '\n000\n000\n000\n',
                '',
                '\nX00\n000\n000\n',
                '',
                '\nX00\nO00\n000\n',
                '',
                '\nXX0\nO00\n000\n',
                '',
                '\nXX0\nOO0\n000\n',
                'X wins',
            ],
        )

    def test_play_damas(self):

        class ControlInputValues(object):
            def __init__(self, *args, **kwargs):
                self.played = False
                self.play_count = 0

            def __call__(self, console_output):
                if 'Select Game' in console_output:
                    if self.played:
                        return '9'
                    self.played = True
                    return '4'
                if '' in console_output:
                    game_turns = (
                        '5 1 4 2',
                        '2 2 3 3',
                        '5 3 4 4',
                        '3 3 5 0',
                        '4 4 3 3',
                        '2 4 4 2',
                        '5 5 4 4',
                        '4 2 5 3',
                        '6 4 4 2',
                        '2 6 3 5',
                        '4 4 2 7',
                        '1 1 2 2',
                        '4 2 3 3',
                        '2 2 4 4',
                        '6 2 5 3',
                        '4 4 6 1',
                        '5 7 4 6',
                        '2 0 3 1',
                        '4 6 3 5',
                        '3 1 4 2',
                        '3 5 2 4',
                        '4 2 5 3',
                        '6 0 5 1',
                        '5 3 6 4',
                        '7 5 5 2',
                        '6 1 7 2',
                        '7 1 6 2',
                        '1 3 3 5',
                        '6 6 5 5',
                        '1 5 2 4',
                        '2 7 1 6',
                        '5 0 6 1',
                        '5 5 4 4',
                        '2 4 3 3',
                        '7 7 6 6',
                        '3 3 5 6',
                        '6 6 5 5',
                        '5 6 6 5',
                        '6 2 5 3',
                        '6 5 7 4',
                        '5 5 4 4',
                        '0 0 1 1',
                        '5 3 4 2',
                        '3 5 5 3',
                        '4 2 3 3',
                        '1 1 2 2',
                        '5 1 4 2',
                        '2 2 4 4',
                        '4 2 3 3',
                        '4 4 5 5',
                        '3 3 2 4',
                        '7 2 6 3',
                        '2 4 1 3',
                        '0 2 2 4',
                        '5 2 4 1',
                        '5 3 4 2',
                        '7 3 6 4',
                        '5 5 4 6',
                        '4 1 5 2',
                        '6 1 7 2',
                        '5 2 6 1',
                        '7 4 6 5',
                        '1 6 0 7',
                        '6 3 5 4',
                        '0 7 1 6',
                        '4 2 5 1',
                        '6 4 5 5',
                        '4 6 6 4',
                        '6 1 5 2',
                        '2 4 3 3',
                        '1 6 2 5',
                        '0 4 1 3',
                        '5 2 4 3',
                        '5 4 4 5',
                        '2 5 3 6',
                        '1 3 2 4',
                        '4 3 5 4',
                        '1 7 2 6',
                        '3 6 2 7',
                        '4 5 6 3',
                        '2 7 3 6',
                        '3 3 4 4',
                        '3 6 4 5',
                        '6 5 5 6',
                        '4 5 5 4',
                        '5 6 4 5',
                        '5 4 6 5',
                        '5 1 4 2',
                        '6 5 5 4',
                        '6 3 5 2',
                        '5 4 6 5',
                        '7 2 6 1',
                        '6 5 5 4',
                        '4 5 6 3',
                    )
                    play = game_turns[self.play_count]
                    self.play_count += 1
                    return play

        with \
            patch('game.Game.get_input', side_effect=ControlInputValues()), \
                patch('game.Game.output', side_effect=self.output_collector):
            self.game.play()

        self.assertEquals(
            self.output_collector.output_collector[-2],
            ' 01234567\n0      b \n1        \n2    b b \n3        \n4  b bB  \n5  B W   \n6 B  b   \n7        \n',
        )


    def test_play_buscaminas(self):

        class ControlInputValues(object):
            def __init__(self, *args, **kwargs):
                self.played = False
                self.play_count = 0

            def __call__(self, console_output):
                if 'Select Game' in console_output:
                    if self.played:
                        return '9'
                    self.played = True
                    return '2'
                if 'Play (expecting 2 numbers separated with spaces)' in console_output:
                    game_turns = (
                        '1 1',
                    )
                    play = game_turns[self.play_count]
                    self.play_count += 1
                    return play

        class BombsValues(object):
            def __init__(self, *args, **kwargs):
                self.random_count = 0

            def __call__(self, console_output, *args, **kwargs):
                random_values = (
                    1, 1,
                    2, 4,
                    1, 2,
                    3, 4,
                    4, 3,
                    2, 1,
                    5, 3,
                    3, 5,
                    6, 1,
                    7, 2,
                )
                return_value = random_values[self.random_count]
                self.random_count += 1
                return return_value

        with \
                patch('game.Game.get_input', side_effect=ControlInputValues()), \
                patch('game.Game.output', side_effect=self.output_collector), \
                patch('buscaminas.buscaminas.randint', side_effect=BombsValues()):
            self.game.play()

        self.assertEqual(
            "------------- You Lose -------------------",
            self.output_collector.output_collector[1]
        )

    def test_play_cuatro_en_linea(self):

        class ControlInputValues(object):
            def __init__(self, *args, **kwargs):
                self.played = False
                self.play_count = 0

            def __call__(self, console_output):
                if 'Select Game' in console_output:
                    if self.played:
                        return '9'
                    self.played = True
                    return '3'
                if '' in console_output:
                    game_turns = (
                        '0',
                        '1',
                        '0',
                        '1',
                        '0',
                        '1',
                        '0',
                    )
                    play = game_turns[self.play_count]
                    self.play_count += 1
                    return play

        with \
            patch('game.Game.get_input', side_effect=ControlInputValues()), \
            patch('game.Game.output', side_effect=self.output_collector):
            self.game.play()


        self.assertEquals(
            self.output_collector.output_collector,
            [
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n',
                'Keep playing',
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n'
                'WEEEEEE\n',
                'Keep playing',
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n'
                'WBEEEEE\n',
                'Keep playing',
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n'
                'WEEEEEE\n'
                'WBEEEEE\n',
                'Keep playing',
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n'
                'WBEEEEE\n'
                'WBEEEEE\n',
                'Keep playing',
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n'
                'WEEEEEE\n'
                'WBEEEEE\n'
                'WBEEEEE\n',
                'Keep playing',
                'EEEEEEE\n'
                'EEEEEEE\n'
                'EEEEEEE\n'
                'WBEEEEE\n'
                'WBEEEEE\n'
                'WBEEEEE\n',
                'You win',
            ],
        )


if __name__ == "__main__":
    unittest.main()
