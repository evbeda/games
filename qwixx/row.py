from sys import settrace


class NotCanMark(Exception):
    def __init__(self):
        super().__init__('You cannot mark that row, the number must be on the right of the last mark!')


class CantBeLocked(Exception):
    def __init__(self):
        super().__init__('You have less than 5 marks!')


class RowIsLocked(Exception):
    def __init__(self):
        super().__init__('It cannot be marked because the row is locked!')


class Row:
    blocked_rows = []

    def __init__(self, color):
        self.color = color
        self.numbers = self.create_row_numbers()
        self.marks = []
        self._is_locked = False

    def create_row_numbers(self):
        return (
            tuple(range(2, 13))
            if self.color in ['red', 'yellow']
            else tuple(reversed(range(2, 13)))
        )

    def lock_Row(self):
        self.blocked_rows.append(self.color)

    @property
    def is_locked(self):
        if self.color in self.blocked_rows:
            raise RowIsLocked
        else:
            return self._is_locked
    
    @is_locked.setter
    def is_locked(self, value):
        self._is_locked = value

    def set_mark(self, number):
        if self.check_row_lock(number):
            return self.marks.append(number)
        else:
            raise NotCanMark

    def check_row_lock(self, number):
        if (
            (self.is_locked is False)
            and (number not in self.marks)
        ):
            return self.can_mark(number)
        else:
            raise NotCanMark()

    def calculate_marks(self):
        set_marks = (
            (0, 0),
            (1, 1),
            (2, 3),
            (3, 6),
            (4, 10),
            (5, 15),
            (6, 21),
            (7, 28),
            (8, 36),
            (9, 45),
            (10, 55),
            (11, 66),
            (12, 70),
        )
        for mark in set_marks:
            if len(self.marks) == mark[0]:
                return mark[1]

    def can_mark(self, number):
        return(
            self.can_mark_last(number)
            if self.is_number_last(number)
            else
            self.can_mark_common(number)
        )

    def can_mark_last(self):
        if len(self.marks) > 5:
            return True
        else:
            raise CantBeLocked()

    def can_mark_common(self, number):
        return(
            self.marks == []
        ) or (
            (
                number > self.marks[-1]
            ) and (
                self.color in ['red', 'yellow']
            )
        ) or (
            (
                number < self.marks[-1]
            ) and (
                self.color in ['blue', 'green']
            )
        )

    def is_number_last(self, number):
        return (
            (
                self.color in ['red', 'yellow'] and number == 12
            )
            or (
                self.color in ['blue', 'green'] and number == 2
            )
        )
