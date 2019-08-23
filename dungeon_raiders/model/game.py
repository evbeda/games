# Modules
import random
from game_base import GameBase
# Model
from .level import Level
from .player import Player
from .exceptions.exceptions import UnplayableCardException, NotANumberException
# Messages
from . import (
    CHARACTER,
    EXIT,
    ROOMS,
    BYE_MESSAGE,
    GAME_OVER,
    LEVEL_FINISHED_MESSAGE,
    LEVEL_CARDS,
    INPUT_NUMBER
    )


class DungeonRaidersGame(GameBase):
    name = 'Dungeon Raiders'
    input_args = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.index_current_level = 0
        self.players = DungeonRaidersGame.create_players()
        self.levels = self.create_levels()
        self.current_level = self.levels[self.index_current_level]

    def create_levels(self):
        deck = ROOMS.copy()
        level_cards = LEVEL_CARDS.copy()
        random.shuffle(deck)
        random.shuffle(level_cards)
        return [
            Level(self.players, i+1, deck, random.choice(level_cards))
            for i in range(5)
        ]

    @staticmethod
    def create_players():
        players = [Player(character=c) for c in random.sample(CHARACTER, k=3)]
        return players

    def resolve_game(self):
        finalists = self.get_finalists()
        winners = DungeonRaidersGame.get_players_with_max_gold(finalists)
        if len(winners) == len(DungeonRaidersGame.get_players_with_max_wounds(winners)):
            return winners
        return [player for player in winners
                if player not in DungeonRaidersGame.get_players_with_max_wounds(winners)]

    def get_finalists(self):
        players_with_max_wound = DungeonRaidersGame.get_players_with_max_wounds(self.players)
        if len(self.players) - len(players_with_max_wound) < 2:
            return self.players
        return [player for player in self.players
                if player not in players_with_max_wound]

    @staticmethod
    def get_players_with_max_wounds(players):
        max_wounds_value = max([player.wounds for player in players])
        return [player for player in players
                if player.wounds == max_wounds_value]

    @staticmethod
    def get_players_with_max_gold(players):
        max_gold_value = max([player.gold for player in players])
        return [player for player in players
                if player.gold == max_gold_value]

    def next_turn(self):
        msg = ''
        if self.is_playing is True:
            msg += f"{self.current_level.actual_room}\n"
            cards_to_play = [str(card) for card in self.current_level.hands[0].cards_to_play]
            msg += f"Playable cards: {', '.join(cards_to_play)}"
        return msg

    def play(self, *command):
        if command[0] == EXIT:
            self.finish()
            return BYE_MESSAGE
        try:
            power_card_played = command[0]
            room_resolved_msg = self.current_level.execute_level(power_card_played)
            if self.current_level.is_last_room():
                self.index_current_level += 1
                self.current_level = self.levels[self.index_current_level]
                return room_resolved_msg + "\n" + LEVEL_FINISHED_MESSAGE
            self.current_level.next_room()
            return room_resolved_msg
        except IndexError:
            self.finish()
            return room_resolved_msg + "\n" + \
                DungeonRaidersGame.separator() + \
                self.show_winners() + "\n" + \
                GAME_OVER + "\n" + \
                DungeonRaidersGame.separator()
        except UnplayableCardException as exception:
            return str(exception)
        except NotANumberException:
            return INPUT_NUMBER

    @property
    def board(self):
        msg = DungeonRaidersGame.separator()
        if self.is_playing is True:
            msg += f"{self.current_level}\n"
            msg += "\nPlayers status:\n"
            msg += '\n'.join([player.status for player in self.players])
        else:
            msg += self.show_winners()
        return msg + "\n"

    def show_winners(self):
        winners = self.resolve_game()
        msg = f'Winners:\n' if len(winners) > 1 else f'Winner:\n'
        msg += '\n'.join([winner.status for winner in winners])
        return msg + "\n"

    @staticmethod
    def separator():
        return "===================================================\n"
