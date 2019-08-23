import unittest
from parameterized import parameterized
from ..model.exceptions.exceptions import (
    UnplayableCardException,
    NotANumberException,
)

from ..model.hand_computer import HandComputer
from ..model.hand_player import HandPlayer
from ..model.player import Player


class TestHandPlayer(unittest.TestCase):
    def test_init_hand(self):
        hand = HandPlayer(Player('A'))
        self.assertEqual(5, len(hand.cards_to_play))

    def test_check_if_player_can_play_card_2(self):
        hand = HandPlayer(Player('A'))
        hand.play('2')
        hand.play('5')
        with self.assertRaises(UnplayableCardException):
            hand.chosen_card = 2
            hand.play('2')

    def test_check_actual_card(self):
        hand = HandPlayer(Player('A'))
        hand.play('2')
        self.assertEqual(2, hand.last_card_played)

    def test_check_if_3_is_in_hand(self):
        hand = HandPlayer(Player('A'))
        hand.chosen_card = 3
        hand.play('3')
        self.assertTrue(3 not in hand.cards_to_play)

    @parameterized.expand([
        (HandComputer(None), [3, 4, 5]),
        (HandComputer(None), [1, 2, 3, 4, 5]),
        (HandComputer(None), []),
    ])
    def test_select_card_hand_computer_valid(self, hand, cards):
        selected_card = hand.select_card(cards)
        if cards:
            self.assertTrue(selected_card in cards)
        else:
            self.assertTrue(selected_card in [1, 2, 3, 4, 5])

    @parameterized.expand([
        ([1, 2, 3, 4, 5], '1'),
        ([1, 2, 3], '4'),
        ([], '5')
    ])
    def test_validate_human_hand_select_card(self, cards, sel_card):
        HandPlayer.cards_to_play = cards
        self.assertTrue(HandPlayer(None).validate(sel_card))

    @parameterized.expand([
        ([1, 2, 3, 4], "5", UnplayableCardException),
        ([1, 2, 3, 4, 5], '%', NotANumberException),
        ([1, 2, 3, 4, 5], '_', NotANumberException),
    ])
    def test_select_card_human_player_not_valid(self, cards, sel_card, exc):
        with self.assertRaises(exc):
            hand_player = HandPlayer(None)
            hand_player.cards_to_play = cards
            hand_player.validate(sel_card)
