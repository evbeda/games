from .room import Room


class MonsterRoom(Room):

    def __init__(self, characteristics):
        self.name = characteristics[2]
        self.life = characteristics[0]
        self.damage = characteristics[1]
        self.long_name = self.name + f" (❤️ {characteristics[0]}, 🗡️️ {characteristics[1]})"

    def __str__(self):
        msg = f'Life: {self.life}\nDamage: {self.damage}\n'
        return f'Room name: {self.name}\n{msg}'

    def resolve_room(self, hands):
        # Determine played cards
        played_cards = [hand.last_card_played for hand in hands]

        # Determine damage
        total_damage = sum(played_cards)

        ret = ""
        # If necessary, apply damage
        if total_damage < self.life:
            ret += f"{self.name} attacks. "
            min_card = min(played_cards)
            players_damaged = []
            for hand in hands:
                if hand.last_card_played == min_card:
                    players_damaged.append(hand.player.character)
                    hand.player.add_wounds(self.damage)
            if len(players_damaged) == 1:
                ret += f"{players_damaged[0]} "
            elif len(players_damaged) == 2:
                ret += f"{players_damaged[0]} and {players_damaged[1]} "
            else:
                ret += ", ".join(players_damaged[:-2])
                ret += f", {players_damaged[-2]} and {players_damaged[-1]} "
            ret += f"took {self.damage} damage."
        else:
            ret += f"{self.name} was beaten. No one took damage."
        return ret
