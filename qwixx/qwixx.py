from .score_pad import (
    ScorePad,
    ReachPenaltyLimit,
)
from .set_dices import SetDices
from .row import Row

QWIXX_STATE_START = 'start_game'
QWIXX_STATE_OPTION = 'select_option'
QWIXX_STATE_PLAY = 'play'

QWIXX_TURN_WHITE = 'white'
QWIXX_TURN_COLOR = 'color'

game_state_next_turn = {
    QWIXX_STATE_START: 'Enter number of players',
    QWIXX_STATE_OPTION: 'Game option:\n1) play \n2) pass',
}
game_state_color_next_turn = {
    QWIXX_TURN_WHITE:
        'Choose in which row you want to mark the common dice\n'
        '1) red\n'
        '2) yellow\n'
        '3) blue\n'
        '4) green\n',
    QWIXX_TURN_COLOR:
        'Choose a white and color die\n'
        '1-2) white die   1-4)color die',
}
OPTION_PLAY = 1
OPTION_PASS = 2

COLOR_ROW = {
    1: 'red',
    2: 'yellow',
    3: 'blue',
    4: 'green',
}

COLOR_DICE = {
    1: 'white_1',
    2: 'white_2'
}


class Qwixx:

    name = 'Qwixx'
    input_are_ints = True

    def __init__(self):
        self.game_state = QWIXX_STATE_START
        self.score_pad = []
        self.current_player = 0
        self.current_color_player = 0
        self.dice_set = SetDices()
        self.is_playing = True
        self.turn_color = QWIXX_TURN_WHITE
        self.previous_turn_color = QWIXX_TURN_WHITE

    def play_start(self, n_players):
        self.create_scored_pad(n_players)
        self.dice_set.roll_dices()
        self.game_state = QWIXX_STATE_OPTION

    def create_scored_pad(self, player_amount):
        if player_amount not in range(1, 5):
            raise Exception
        for indice_Player in range(player_amount):
            self.score_pad.append(ScorePad())
            self.score_pad[indice_Player].id_player = indice_Player

    def next_turn(self):
        if self.game_state == QWIXX_STATE_PLAY:
            return game_state_color_next_turn[self.turn_color]
        else:
            return game_state_next_turn[self.game_state]

    def remove_dice(self, color):
        for index, dice in enumerate(self.dice_set):
            if dice.color == color:
                self.dice_set.pop(index)
                break

    def mark_with_color(self, white_index, color_index):
        color = COLOR_ROW[color_index]
        s_pad = self.score_pad[self.current_player]
        first_die = self.dice_set.get_value_of_die(COLOR_DICE[white_index])
        second_die = self.dice_set.get_value_of_die(color)
        total = first_die + second_die
        try:
            s_pad.mark_number_in_row(total, color)
        except Exception as e:
            return str(e)

        self.set_next_player()

    def mark_with_white(self, color_index):
        color = COLOR_ROW[color_index]
        s_pad = self.score_pad[self.current_player]
        first_die = self.dice_set.get_value_of_die('white_1')
        second_die = self.dice_set.get_value_of_die('white_2')
        total = first_die + second_die
        try:
            s_pad.mark_number_in_row(total, color)
        except Exception as e:
            return str(e)
        self.set_next_player()

    def set_next_player(self):
        self.game_state = QWIXX_STATE_OPTION
        next_player = (self.current_player + 1) % len(self.score_pad)
        if self.turn_color == QWIXX_TURN_COLOR and self.previous_turn_color == QWIXX_TURN_WHITE:
            self.current_color_player = (self.current_color_player + 1) % len(self.score_pad)
            self.turn_color = QWIXX_TURN_WHITE
            self.previous_turn_color = QWIXX_TURN_COLOR
            self.dice_set.roll_dices()
        elif next_player == self.current_color_player:
            self.turn_color = QWIXX_TURN_COLOR
            self.previous_turn_color = QWIXX_TURN_WHITE
        self.current_player = next_player

    def play_option(self, option):
        if option == OPTION_PLAY:
            self.game_state = QWIXX_STATE_PLAY
        elif option == OPTION_PASS:
            if self.turn_color == QWIXX_TURN_COLOR:
                try:
                    self.score_pad[self.current_player].add_penalty()
                except ReachPenaltyLimit:
                    self.is_playing = False
                    return self.show_winners()
            self.set_next_player()
        else:
            return 'Invalid Option'
        return ''

    def play_turn(self, *args):
        if self.turn_color == QWIXX_TURN_WHITE:
            return self.mark_with_white(args[0])
        else:
            return self.mark_with_color(args[0], args[1])

    @property
    def input_args(self):
        return (
            2
            if self.game_state == QWIXX_STATE_PLAY and self.turn_color == QWIXX_TURN_COLOR
            else 1
        )

    def play(self, *args):
        msg = ''
        if self.game_state == QWIXX_STATE_START:
            self.play_start(args[0])
        elif self.game_state == QWIXX_STATE_OPTION:
            msg = self.play_option(args[0])
        elif self.game_state == QWIXX_STATE_PLAY:
            msg = self.play_turn(*args)
        return msg if msg is not None else ''

    @property
    def board(self):
        output = " "
        if self.score_pad:
            output += "\n"
            output += "------------------------------------------------------------\n"
            output += "     BOARD PLAYER: {}     ".format(self.score_pad[self.current_player].id_player)
            output += "TURN: {}    ".format(self.turn_color)
            output += "PENALTY: {}\n".format(str(self.score_pad[self.current_player].penalty))
            output += "------------------------------------------------------------\n"
            output += "\n"
            for row in self.score_pad[self.current_player].rows.values():
                output += self.output_row(row)
            output += "------------------------------------------------------------\n"
            output += "SCORE: {}".format(str(tuple(range(1, 13))))
            output += "\n"
            output += "       (1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 70)\n"
            output += "\n"
            output += "DICES:\n"
            output += "     (1)WHITE: {}  ".format(self.dice_set.get_value_of_die('white_1')).ljust(10)
            output += "(2)WHITE: {}  ".format(self.dice_set.get_value_of_die('white_2')).ljust(10)
            output += "(1)RED: {}  ".format(self.dice_set.get_value_of_die('red')).ljust(10)
            output += "(2)YELLOW: {}  ".format(self.dice_set.get_value_of_die('yellow')).ljust(10)
            output += "(3)BLUE: {}  ".format(self.dice_set.get_value_of_die('blue')).ljust(10)
            output += "(4)GREEN: {}  ".format(self.dice_set.get_value_of_die('green')).ljust(10)
            output += "\n"

        return output

    def is_locked(self, row):
        if row.color in row.blocked_rows:
            return "is locked"
        else:
            return "not locked"

    def output_row(self, row):
        output = ' '
        output += '{}'.format(row.color.upper()).ljust(8)
        output += '|'
        output += '{}'.format(row.numbers)
        output += '| '
        output += '{}'.format(self.is_locked(row)).rjust(10)
        output += "\n"
        output += " ".ljust(9)
        output += '|'
        output += '{}'.format(row.marks).ljust(36)
        output += '| '
        output += "\n\n"
        return output

    @property
    def you_can_play(self):
        if len(Row.blocked_rows) < 2:
            self.is_playing = True
        else:
            self.is_playing = False

    def get_winners(self):
        players = self.score_pad.copy()
        return sorted(players, key=lambda x: x.calculate_score(), reverse=True)

    def show_winners(self):
        rankig_players = self.get_winners()
        msg = ''
        msg += 'WINNERS TABLE \n'
        msg += "------------------------------------------------------------\n"
        for player in rankig_players:
            msg += 'PLAYER {}'.format(player.id_player).ljust(8)
            msg += ' | '
            msg += 'SCORE {}\n'.format(player.calculate_score()).rjust(10)
        msg += "------------------------------------------------------------"
        return msg
