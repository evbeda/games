from .game import Game

GAME_STATE_CREATE_GAME = 'create_game'
GAME_STATE_INPUT_PLAYERS = 'input_players'
GAME_STATE_PLAY_WORD = 'play_word'
GAME_STATE_CHANGE_LETTERS = 'change_letters'
GAME_STATE_ASK_CHALLENGE = 'ask_challenge'
GAME_STATE_IN_CHALLENGE = 'in_challenge'
GAME_STATE_CHANGE_TURN = 'change_turn'
GAME_STATE_CHANGED_LETTERS = 'changed_letters'
GAME_STATE_SELECT_ACTION = 'select_action'
GAME_STATE_SKIP_TURN = 'skip_turn'


class Scrabble:

    name = 'Scrabble'

    @property
    def is_playing(self):
        return self.game.is_playing if self.game is not None else True

    @property
    def input_args(self):
        game_state_args = {
            GAME_STATE_CREATE_GAME: lambda: 1,
            GAME_STATE_INPUT_PLAYERS: lambda: self.input_player_args,
            GAME_STATE_PLAY_WORD: lambda: 4,
            GAME_STATE_CHANGE_LETTERS: lambda: self.change_letters,
            GAME_STATE_ASK_CHALLENGE: lambda: 1,
            GAME_STATE_IN_CHALLENGE: lambda: 1,
            GAME_STATE_SELECT_ACTION: lambda: 1,
        }
        return game_state_args[self.game_state]()

    @property
    def input_are_ints(self):
        return self.game_state in [
            GAME_STATE_CREATE_GAME,
            GAME_STATE_ASK_CHALLENGE,
        ]

    def __init__(self):
        self.game = None
        self.game_state = GAME_STATE_CREATE_GAME
        self.input_player_args = 0
        self.challenger_player = 0
        self.change_letters = 0

    @property
    def board(self):
        return f'{self.game.print_board()}\n\n{self.game.print_scores()}' if self.game else ''

    def next_turn_state_query(self):
        game_state_next_turn = {
            GAME_STATE_CREATE_GAME: 'Enter number of players\n',
            GAME_STATE_INPUT_PLAYERS: 'Enter player names\n',
            GAME_STATE_CHANGE_LETTERS: 'Which letters do you want to change?\n',
            GAME_STATE_PLAY_WORD: (
                'Enter all in a line:\n'
                '- start position of word (nº of row and nº of column)\n'
                '- direction(h --> horizontal or v --> vertical)\n'
                '- the word\n'
            ),
            GAME_STATE_ASK_CHALLENGE: 'Select the challenger player:\n',
            GAME_STATE_IN_CHALLENGE: (
                'Look up new words in a dictionary. Are they correct?\n'
            ),
            GAME_STATE_SELECT_ACTION: (
                'Enter "play" to play a new word, "pass" to end your turn '
                'or any number to change that amount of tiles\n'
            ),
        }
        return game_state_next_turn[self.game_state]

    def next_turn_show_hand(self):
        return self.game.get_current_player_hand()

    def next_turn(self):
        query = '\n'

        if self.game_state == GAME_STATE_CHANGED_LETTERS:
            query += 'Changed letters:\n'
            query += self.next_turn_show_hand() + '\n'
            query += '- - - - - - - - - - - - - -\n\n'
        elif self.game_state == GAME_STATE_SKIP_TURN:
            self.game.skip_turn()
            self.game_state = GAME_STATE_SELECT_ACTION
        self.change_turn()
        if self.is_playing:
            if self.game is not None:
                query += self.next_turn_show_hand() + '\n\n'
            query += self.next_turn_state_query()
            if self.game_state == GAME_STATE_ASK_CHALLENGE:
                query += self.game.ask_challenge_show_players() + '\n'
        else:
            query += self.game.get_game_results()

        return query

    def change_turn(self):
        if self.game_state in [
            GAME_STATE_CHANGE_TURN,
            GAME_STATE_CHANGED_LETTERS,
            GAME_STATE_SKIP_TURN,
        ]:
            self.game.change_turn()
            self.game_state = GAME_STATE_SELECT_ACTION

    def play_create_game(self, player_count):
        if 2 <= player_count <= 4:
            self.input_player_args = player_count
            self.game_state = GAME_STATE_INPUT_PLAYERS
        else:
            return 'The number of players is wrong, please enter the number again'

    def play_input_players(self, *player_names):
        self.game = Game(player_names)
        self.game_state = GAME_STATE_SELECT_ACTION

    def play_play_word(self, row, col, direction, word):
        row = int(row)
        col = int(col)
        if direction == 'h':
            placed = self.game.place_word(col, row, True, word)
        elif direction == 'v':
            placed = self.game.place_word(col, row, False, word)
        else:
            return 'This is not a valid direction'
        if placed:
            self.game_state = GAME_STATE_ASK_CHALLENGE
        else:
            self.game_state = GAME_STATE_CHANGE_TURN
            return 'Invalid word position'

    def play_change_letters(self, *letters):
        self.game.change_player_tiles(letters)
        self.game_state = GAME_STATE_CHANGED_LETTERS

    def play_ask_challenge(self, challenger):
        if 0 <= challenger <= self.game.player_count:
            self.challenger_player = challenger
            self.game_state = GAME_STATE_IN_CHALLENGE
        elif challenger == 99:
            self.game_state = GAME_STATE_CHANGE_TURN

    def play_in_challenge(self, result):
        self.game.resolve_challenge(result == 'yes', self.challenger_player)
        self.game_state = GAME_STATE_CHANGE_TURN

    def play_select_action(self, action):
        if action.isnumeric() and 1 <= int(action) <= 7:
            self.change_letters = int(action)
            self.game_state = GAME_STATE_CHANGE_LETTERS
        elif action == 'play':
            self.game_state = GAME_STATE_PLAY_WORD
        elif action == 'pass':
            self.game_state = GAME_STATE_SKIP_TURN

    def play(self, *args):
        method_name = f'play_{self.game_state}'
        method = getattr(self, method_name)
        return method(*args) or ''
