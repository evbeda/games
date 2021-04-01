from .game import Game

GAME_STATE_START_GAME = 'start_game'
GAME_STATE_PLAYERS_INPUT = 'players_input'
GAME_STATE_SELECT_OPTION = 'select_option'
GAME_STATE_NEW_SET_Q = 'new_set_q'
GAME_STATE_NEW_SET_TILES = 'new_set_tiles'
GAME_STATE_PUT_A_TILE = 'put_a_tile'
GAME_STATE_GET_A_TILE = 'get_a_tile'
GAME_STATE_END_TURN = 'end_turn'
GAME_STATE_END_GAME = 'end_game'
GAME_STATE_MAKE_MOVE = 'make_move'
GAME_STATE_INPUT_VERIFICATION = 'input_verification'

game_state_next_turn = {
    GAME_STATE_START_GAME: 'Enter number of players',
    GAME_STATE_PLAYERS_INPUT: 'Enter player names',
    GAME_STATE_SELECT_OPTION: (
        'Game Options:\n1)Enter a complete new set'
        '\n2)Put a tile from hand in a existing set'
        '\n3)Take a tile from a set\n4)End turn'
    ),
    GAME_STATE_NEW_SET_Q: 'How many tiles will have the set?',
    GAME_STATE_NEW_SET_TILES: (
        'Put the index of tiles to play in the correct order'
    ),
    GAME_STATE_PUT_A_TILE: (
        'Puting a tile: Select a tile, select the set,'
        ' select the index in the chosen set'
    ),
    GAME_STATE_GET_A_TILE: (
        'Taking a tile: Select the set, select the index in the chosen set'
    ),
    GAME_STATE_END_TURN: 'Turn Ended',
    GAME_STATE_MAKE_MOVE: 'Confirm: y/n',
    GAME_STATE_END_GAME: 'WE HAVE A WINNER! Congratulations ',
}


class RummyAndBurakko():
    name = 'Rummy and Burakko'

    @property
    def input_args(self):
        game_state_args = {
            GAME_STATE_START_GAME: 1,
            GAME_STATE_PLAYERS_INPUT: self.input_player_args,
            GAME_STATE_SELECT_OPTION: 1,
            GAME_STATE_NEW_SET_Q: 1,
            GAME_STATE_NEW_SET_TILES: self.input_q_tiles,
            GAME_STATE_PUT_A_TILE: 3,
            GAME_STATE_GET_A_TILE: 2,
            GAME_STATE_MAKE_MOVE: 1,
        }
        return game_state_args[self.game_state]

    @property
    def board(self):
        message = '\n\n*************************************************************\n'
        if self.game is None:
            return message + "Starting..."
        return message + self.game.show_game()

    def __init__(self):
        self.game = None
        self.game_state = GAME_STATE_START_GAME
        self.is_playing = True
        self.input_player_args = 0
        self.input_q_tiles = 0
        self.option = 0
        self.input_are_ints = True
        self.move = None

    # game creation
    def play_start_game(self, players_q):
        if 2 <= players_q <= 4:
            self.input_player_args, self.game_state = players_q, GAME_STATE_PLAYERS_INPUT
            self.input_are_ints = False
            return f'Game created with {players_q} players'
        else:
            return 'Wrong input, choose between 2 and 4 players'

    def play_players_input(self, *player_names):
        self.game = Game(player_names)
        self.game.distribute_tiles()
        self.game.random_order()
        self.game_state = GAME_STATE_SELECT_OPTION
        self.input_are_ints = True
        self.game.next_turn()
        return 'Names taken'

    def next_turn(self):
        message = '\n'
        winner_name = ''
        if self.game_state == GAME_STATE_END_TURN:
            self.game.end_turn()
            self.is_playing = self.game.check_is_game_alive()
            if self.is_playing:
                self.game.next_turn()
                message = '\n\n*************************************************************\n'
                message += self.game.show_game()
                self.game_state = GAME_STATE_SELECT_OPTION
            else:
                winner_name = self.game.get_current_player()
                self.game_state = GAME_STATE_END_GAME

        message += game_state_next_turn[self.game_state]
        message += winner_name
        return message

    # play
    def play_select_option(self, option):
        if 1 <= option <= 4:
            options = {
                1: GAME_STATE_NEW_SET_Q,
                2: GAME_STATE_PUT_A_TILE,
                3: GAME_STATE_GET_A_TILE,
                4: GAME_STATE_END_TURN,
            }
            self.option = option
            self.game_state = options[option]
            return f'\nSelected option {option}'

    def play_new_set_q(self, quantity):
        hand = self.game.quantity_of_tiles()
        loose_tiles = len(self.game.board.reused_tiles)
        limit = hand + loose_tiles
        if 3 <= quantity <= limit:
            self.input_q_tiles = quantity
            self.game_state = GAME_STATE_NEW_SET_TILES
            message = f'Creating a set with {quantity} tiles'
        else:
            message = '\nWrong input'
            message += f'Have to play between 3 and {limit} tiles for a new set\n'
            return message

    def play_input_verification(self, *moves):
        message = self.game.move_verification(self.option, moves)
        if message == '':
            self.game_state = GAME_STATE_MAKE_MOVE
            self.move = moves
            self.input_are_ints = False
            return 'Input is valid'
        else:
            self.game_state = GAME_STATE_SELECT_OPTION
            return message

    def play_make_move(self, confirm):
        self.game_state = GAME_STATE_SELECT_OPTION
        self.input_are_ints = True
        if confirm == "y":
            self.game.make_play(self.option, self.move)
            return 'Movement made'
        else:
            return 'Discarded movement, select a new one'

    def play(self, *args):
        if (self.game_state in [
            GAME_STATE_NEW_SET_TILES,
            GAME_STATE_PUT_A_TILE,
            GAME_STATE_GET_A_TILE,
        ]):
            self.game_state = GAME_STATE_INPUT_VERIFICATION

        method = getattr(self, 'play_' + self.game_state)
        return method(*args)
