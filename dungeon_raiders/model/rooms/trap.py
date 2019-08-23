from .room import Room


class Trap(Room):

    def __init__(self, name, effects):
        self.name = name
        self.effects = effects
        self.long_name = name

    def determine_affected_players(self):
        raise NotImplementedError("Can't be called")

    def resolve_room(self, hands):
        raise NotImplementedError("Can't be called")
