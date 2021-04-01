from .row import (
    Row,
)


class ReachPenaltyLimit(Exception):
    pass


class ScorePad:
    def __init__(self):
        self.id_player = None
        self.rows = self.create_rows()
        self.penalty = 0

    def create_rows(self):
        return (
            {
                color: Row(color)
                for color in ['red', 'yellow', 'blue', 'green']
            }
        )

    def add_penalty(self):
        self.penalty += 1
        if self.penalty >= 4:
            raise ReachPenaltyLimit()

    def calculate_score(self):
        score = 0
        for row in self.rows.values():
            score += row.calculate_marks()
        penalty = self.penalty * 5
        return score - penalty

    def mark_number_in_row(self, number, color):
        self.rows[color].set_mark(number)
