from .hand_player import HandPlayer
from .hand_computer import HandComputer


class Level:
    def __init__(self, players, number_level, deck, level_card):
        self.index_actual_room = 0
        self.number_level = number_level
        self.rooms = self.select_rooms(deck)
        self.actual_room = self.rooms[self.index_actual_room]
        self.hands = self.create_hands_for_level(players)
        self.level_card = level_card

    def __str__(self):
        msg = '\n * '
        rooms = []
        for index, room in enumerate(self.rooms):
            if index == self.index_actual_room:
                rooms.append(room.long_name + " <--")
            elif index < self.index_actual_room or self.level_card[index]:
                rooms.append(room.long_name)
            else:
                rooms.append('Hidden')
        return f'Level: {self.number_level}\nRooms:\n * {msg.join(rooms)}'

    def create_hands_for_level(self, players):
        return [
            HandPlayer(players[0]),
            HandComputer(players[1]),
            HandComputer(players[2])
            ]

    def select_rooms(self, deck):
        return [deck.pop() for i in range(5)]

    def next_room(self):
        self.index_actual_room += 1
        self.actual_room = self.rooms[self.index_actual_room]

    def is_last_room(self):
        return self.index_actual_room == 4

    def execute_level(self, human_power_cards_played):
        ret = "\n"
        [hand.play(human_power_cards_played)
            for index, hand in enumerate(self.hands)]
        players_played_str = [
            hand.player.character + " played " + str(hand.last_card_played)
            for hand in self.hands
        ]
        ret += ', '.join(players_played_str) + "\n"
        ret += self.actual_room.resolve_room(self.hands)
        return ret
