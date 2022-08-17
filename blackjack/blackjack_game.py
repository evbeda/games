from . import cardsDictionary, colorDictionary, cards_colors
from .player import Player
from .deck import Deck
from .hand import Hand
from game_base import GameBase


class BlackJackGame(GameBase):

    name = 'Blackjack'
    input_args = 1
    input_are_ints = False

    messages_who_win = {
        'Dealer': 'Dealer Wins!',
        'Player': 'Player Wins!',
        'T': 'TIE!',
        'C': 'CONTINUE',
    }

    def __init__(self, *args, **kwargs):
        super(BlackJackGame, self).__init__(*args, **kwargs)
        self.min_bet = 0
        self.player = None
        self.dealer_hand = None  # have to be a Hand
        self.pot = 0
        self.is_finished = True
        self.deck = Deck(cardsDictionary, colorDictionary)
        self.bet = 0
        self.bet_time = True
        self.deck_counter = 1
        self.start_game()

    def start_game(self):
        name = 'Player'
        buy_in = 100
        self.min_bet = 5
        self.player = Player(name, buy_in)
        self.reset_round()

    def reset_round(self):
        player_hand = Hand()
        self.dealer_hand = Hand()
        player_deck_card_deal = self.deck.deal(2)
        dealer_deck_card_deal = self.deck.deal(2)
        if (
                player_deck_card_deal == 'Out of cards!' or
                dealer_deck_card_deal == 'Out of cards!'
                ):
            self.deck_counter += 1
            if self.deck_counter < 7:
                self.deck = Deck(cardsDictionary, colorDictionary)
                player_deck_card_deal = self.deck.deal(2)
                dealer_deck_card_deal = self.deck.deal(2)
            else:
                return 'Game Over! No more decks'
        player_hand.deal_card(player_deck_card_deal)
        self.dealer_hand.deal_card(dealer_deck_card_deal)
        self.player.hand = player_hand

    def check_you_can_bet(self):
        if self.player.money >= self.min_bet:
            return True
        else:
            self.finish()
            return False

    def check_bet(self, bet):
        if bet > self.player.money:
            return 'You dont have enough money'
        elif bet < self.min_bet:
            return 'The bet is too low, the min bet is ' + str(self.min_bet)
        else:
            return 'NEW ROUND!'

    def give_money_to_winner(self, who):
        if who == 'Dealer Wins!':
            self.player.money -= self.bet
            if self.player.money == 0:
                self.finish()
        elif who == 'Player Wins!':
            self.player.money += self.bet

    def message_to_win(self, condition):
        return self.messages_who_win[condition]

    def there_is_tie(self) -> bool:

        more_than_17 = self.dealer_hand.value >= 17
        equal_hands = (self.dealer_hand.value == self.player.hand.value)

        first_condition = self.dealer_and_player_equal_hands()
        second_condition = more_than_17 and equal_hands

        return first_condition or second_condition

    def dealer_and_player_equal_hands(self) -> bool:
        return ((self.dealer_hand.value == 21
                and len(self.dealer_hand.cards) == 2) and
                (self.player.hand.value == 21
                and len(self.player.hand.cards) == 2))

    def dealer_wins(self) -> bool:
        first_condition = (self.player.hand.value > 21
                           or self.dealer_hand.value == 21)
        second_condition = self.secod_dealer_condition()
        return first_condition or second_condition

    def secod_dealer_condition(self) -> bool:
        return (self.dealer_hand.value >= 17 and
                not (self.dealer_hand.value > 21
                     or self.player.hand.value == 21)
                and self.dealer_hand.value > self.player.hand.value)

    def player_wins(self):
        cond_1 = self.fisrt_conticion_player()
        cond_2 = (self.dealer_hand.value >= 17 and
                  self.player.hand.value > self.dealer_hand.value)
        return cond_1 or cond_2

    def fisrt_conticion_player(self):
        return ((self.player.hand.value == 21 and
                 len(self.player.hand.cards) == 2) or
                self.dealer_hand.value > 21 or self.player.hand.value == 21)

    def who_wins(self):

        flag_win = 0
        self.is_finished = True

        if self.there_is_tie():
            flag_win = self.message_to_win('T')

        elif self.dealer_wins():
            flag_win = self.message_to_win('Dealer')

        elif self.player_wins():
            flag_win = self.message_to_win('Player')

        else:
            self.is_finished = False
            self._playing = True
            flag_win = self.message_to_win('C')

        return flag_win

    def next_turn(self):
        if self._playing:
            if self.is_finished:
                return 'Enter your bet or q(quit)'
            else:
                return ('Do you want to stop (=) '
                        'or have another card (+)?, q to quit')
        else:
            return 'Game Over'

    def card_encode_function(self, card):
        user_cards = ''
        card_encode = cards_colors[card[1]]
        if(card[0] == 'T'):
            user_cards += '10' + card_encode + ', '
        else:
            user_cards += card[0] + card_encode + ', '
        return user_cards

    @property
    def board(self):
        if not self.bet_time:
            dealer_cards = ''
            player_cards = ''
            for card in self.dealer_hand.cards:
                # print(type(card_encode))
                dealer_cards += self.card_encode_function(card)

            for card in self.player.hand.cards:
                player_cards += self.card_encode_function(card)

            player_cards = player_cards[:-2]
            dealer_cards = dealer_cards[:-2]

            return ('\n\nDealer: {dealer_cards}'
                    '\nPlayer: ' + player_cards + '\n'
                    'Money: {player_money} \n\n').format(
                dealer_cards=dealer_cards,
                player_cards=player_cards,
                player_money=self.player.money,
            )
        else:
            return ''

    def play(self, command):
        message = ""
        if not self.check_you_can_bet():
            self.finish()
            message = 'You dont have money.'
        elif self.is_finished:
            if command == 'q':
                self.bet_time = True
                self.finish()
                message = 'You left the game'
            else:
                try:
                    self.bet_time = True
                    bet = int(command)
                    result = self.check_bet(bet)
                    if result == 'NEW ROUND!':
                        self.reset_round
                        self.bet = bet
                        self.is_finished = False
                        self.bet_time = False
                        if self.reset_round() == 'Game Over! No more decks':
                            self._playing = False
                            return self.reset_round()
                    return result
                except Exception:
                    message = 'Please enter a number or q to quit'
        else:
            if command == '=':
                if self.who_wins() == 'CONTINUE':
                    self.dealer_hand.deal_card(self.deck.deal(1))
                    message = self.play('=')
                else:
                    who_wins = self.who_wins()
                    self.give_money_to_winner(who_wins)
                    message = who_wins
            elif command == '+':
                self.player.hand.deal_card(self.deck.deal(1))
                who_wins = self.who_wins()
                self.give_money_to_winner(who_wins)
                message = who_wins
            elif command == 'q':
                self.finish()
                message = 'You left the game'
            else:
                message = 'Wrong command, please use + or = .'
        return message
