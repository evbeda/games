from game_base import GameBase
import requests


class IsNotAlphaException(Exception):
    pass


class IsNotOneCharacter(Exception):
    pass


class Ahorcado(GameBase):
    name = "Ahorcado"
    input_args = 1
    input_are_ints = False

    def __init__(self, force_word=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.word = force_word if force_word else self.get_word_from_api()
        self.lifes = 6
        self.used_letters = []

    def next_turn(self):
        if not self.is_playing and self.lifes > 0:
            return "The player already won"
        elif not self.is_playing and self.lifes <= 0:
            return "The player already lost"
        else:
            return "Please input a letter from A-Z"

    def play(self, letter):
        letter = letter.upper()
        try:
            self.validate_letter(letter)
        except IsNotAlphaException:
            return "{} is not a character, use a letter".format(letter)
        except IsNotOneCharacter:
            return "{} is not a single word, put one letter!".format(letter)

        if self.check_input_used_letters(letter):
            return "Already tried that Letter! Try again"

        elif not self.check_input_word(letter):
            self.lifes = self.lifes - 1
            self.set_used_letters(letter)
            return "Wrong letter, you lose one life"

        elif self.check_input_word(letter) and self.is_playing:
            self.set_used_letters(letter)
            if not self.is_playing:
                return "Game Finished"
            return "Correct letter! Choose another"

    def get_lifes(self):
        return "Lifes: {}".format(self.lifes)

    def get_word_from_api(self):
        url = "http://random-word-api.herokuapp.com/word?number=1"
        api_word = requests.get(url)
        return api_word.json()[0].upper()

    def set_used_letters(self, letter):
        if letter not in self.used_letters:
            self.used_letters.append(letter)
        else:
            pass

    def check_input_used_letters(self, letter):
        if letter in self.used_letters:
            return True
        else:
            return False

    def check_input_word(self, letter):
        if letter in self.word:
            return True
        else:
            return False

    @property
    def is_playing(self):
        if self.lifes <= 0:
            return False
        if self.lifes > 0 and "_" not in self.hidden_letters_message():
            return False
        if self.lifes > 0:
            return True

    def hidden_letters_message(self):
        new_hidden_letters = []
        for character in self.word:
            if character in self.used_letters:
                new_hidden_letters.append(character)
            elif character not in self.used_letters:
                new_hidden_letters.append("_")
        return " ".join(new_hidden_letters)

    def validate_letter(self, letter):
        if len(letter) > 1:
            raise IsNotOneCharacter("Only one letter is expected, you are introducing {} character".format(len(letter)))
        if not letter.isalpha():
            raise IsNotAlphaException("The value {} is not a letter".format(letter))

    @property
    def board(self):
        return self.hidden_letters_message() + '\n' + " ".join(self.used_letters) + '\n' + self.get_lifes()
