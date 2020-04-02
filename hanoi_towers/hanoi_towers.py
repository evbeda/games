from .tower import Tower
from .tower import InvalidMovement
from .tower import EmptyTower


class HanoiTowers:

    name = "Hanoi Towers"
    input_args = 2
    input_are_ints = True
    def __init__(self, cant_tokens=4):

        self.cant_tokens = cant_tokens
        self.towers = [Tower(cant_tokens), Tower(), Tower()]
        self.is_playing = True

    def next_turn(self):

        if not self.is_playing:
            return "You won"
        else:
            return "Enter the numbers of source and target towers"

    def play(self, source, target):

        try:
            source = int(source)
            target = int(target)
            self.validate_input(source, target)
            my_token = self.towers[source].remove_token()
            self.towers[target].insert_token(my_token)
            if (len(self.towers[2].tokens) == self.cant_tokens) or (len(self.towers[1].tokens) == self.cant_tokens):
                self.is_playing = False
                return "You won"
            return "Token moved successfully"
        except InvalidMovement:
            self.towers[source].insert_token(my_token)
            return "Invalid move"
        except EmptyTower:
            return "Empty tower"
        except ValueError:
            return "Error: enter only integers"
        except SameTowerException:
            return "Error: the towers must be different"
        except NotValidTowerIndexException:
            return f"Error: enter numbers between 0 and {len(self.towers)-1}"

    def validate_input(self, source, target):
        if source == target:
            raise SameTowerException
        try:
            self.towers[source]
            self.towers[target]
        except IndexError:
            raise NotValidTowerIndexException
        return True

    @property
    def board(self):
        tower_print = ""
        for index in range(self.cant_tokens - 1, -1, -1):
            for tower in self.towers:
                if len(tower.tokens) > index:
                    tower_print += " " * (20 - tower.tokens[index].size * 2)
                    tower_print += "- " * tower.tokens[index].size
                    tower_print += "|"
                    tower_print += " -" * tower.tokens[index].size
                    tower_print += " " * (20 - tower.tokens[index].size * 2)
                else:
                    tower_print += " " * (20)
                    tower_print += "|"
                    tower_print += " " * (20)
            tower_print += "\n"
        return tower_print


class SameTowerException(Exception):
    pass


class NotValidTowerIndexException(Exception):
    pass
