from .trap import Trap


class WoundRoom(Trap):

    def __init__(self, characteristics):
        super().__init__(characteristics[0], characteristics[1])
        self.long_name = self.name + " (Wounds)"

    def __str__(self):
        msg = ''
        for effect in self.effects:
            card = effect[0]
            msg += f'Card: {card} '
            wound = effect[1]
            msg += f'Wound: {wound}\n'
        return f'Room name: {self.name}\n{msg}'

    def determine_affected_players(self, hands):
        affected_players = []
        players = [hand.player for hand in hands]

        wounds_list = [hand.player.wounds for hand in hands]
        min_wounds = min(wounds_list)
        for player in players:
            if player.wounds == min_wounds:
                affected_players.append(player)

        return affected_players

    def resolve_room(self, hands):
        # Determine affected players
        affected_players = self.determine_affected_players(hands)

        # Determine damage
        played_cards = [hand.last_card_played for hand in hands]
        max_card = max(played_cards)
        trap_effect = 0
        for elem in self.effects:
            if elem[0] == max_card:
                trap_effect = elem[1]

        # Apply effect and return
        ret = ''
        for player in affected_players:
            ret += player.character + ' took ' + str(trap_effect) + ' damage. '
            player.wounds += trap_effect
        return ret
