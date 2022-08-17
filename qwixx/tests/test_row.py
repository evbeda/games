import unittest
from parameterized import parameterized
from ..row import (
    NotCanMark,
    Row,
    CantBeLocked,
    RowIsLocked,
)
from unittest.mock import patch


class TestRow(unittest.TestCase):
    def test_lock_row(self):
        # color_row = "red"
        r = Row('yellow')
        r.blocked_rows = []
        self.assertEqual(r.blocked_rows, [])
        r.lock_Row()
        self.assertEqual(r.blocked_rows, [r.color])

    @parameterized.expand([
        ('red', tuple(range(2, 13))),
        ('yellow', tuple(range(2, 13))),
        ('blue', tuple(reversed(range(2, 13)))),
        ('green', tuple(reversed(range(2, 13)))),
    ])
    def test_correct_row_generation(self, color_row, expected):
        row_example = Row(color_row)
        self.assertEqual(row_example.numbers, expected)

    def test_can_mark_last_more_5(self):
        row_example = Row('red')
        row_example.marks = [2, 3, 4, 5, 6, 6]
        row_example.can_mark_last()

    def test_cant_mark_last_less_5(self):
        with self.assertRaises(CantBeLocked):
            row_example = Row('blue')
            row_example.marks.clear()
            self.assertTrue(row_example.can_mark_last())

    @parameterized.expand([
        (0, 'rojo', RowIsLocked),
        (6, 'green', RowIsLocked),
    ])
    def test_check_row_lock_exception(self, number, color, exception_NotCanMark):
        r = Row(color)
        r.blocked_rows.append(color)
        with self.assertRaises(exception_NotCanMark):
            r.check_row_lock(number)
    
    @parameterized.expand([
        (6, 'rojo', NotCanMark),
    ])
    def test_check_row_lock_exception(self, number, color, exception_NotCanMark):
        r = Row(color)
        r.is_locked = True

        with self.assertRaises(exception_NotCanMark):
            r.check_row_lock(number)

    @parameterized.expand([
        ('red', 0, True),
    ])
    @patch.object(Row, 'can_mark')
    def test_check_row_lock(self, color, call_count_mock, expected,
                            mock_can_mark):
        r = Row(color)
        r.blocked_rows.append('green')
        r.check_row_lock(5)
        mock_can_mark.assert_called()

    @patch.object(Row, 'can_mark_last')
    @patch.object(Row, 'is_number_last', return_value=True)
    def test_can_mark_can_mark_last(self, mock_is_number_last, mock_can_mark_last):
        r = Row('red')
        r.can_mark(12)
        mock_is_number_last.assert_called_once_with(12)

    @patch.object(Row, 'can_mark_common')
    @patch.object(Row, 'is_number_last', return_value=False)
    def test_can_mark_can_mark_common(self, mock_is_number_common, mock_can_mark_common):
        r = Row('red')
        r.can_mark(4)
        mock_is_number_common.assert_called_once_with(4)

    @parameterized.expand([
        ('red', [2, 3, 6], 7, True),
        ('red', [2, 4, 6], 3, False),
        ('yellow', [3, 4, 6], 2, False),
        ('blue', [6, 5, 4], 3, True),
        ('blue', [6, 5, 4], 7, False),
        ('green', [7, 5, 4], 6, False),
        ('green', [], 6, True),
        ('red', [], 7, True),
    ])
    def test_can_mark_common(self, color, marks, number, expected):
        r = Row(color)
        r.marks = marks

        self.assertEqual(r.can_mark_common(number), expected)

    @parameterized.expand([
        ('red', [2, 3, 6], 6),
    ])
    def test_calculate_marks(self, color, marks, expected):
        r = Row(color)
        r.marks = marks
        self.assertEqual(r.calculate_marks(), expected)

    @parameterized.expand([
        ('yellow', [2], 7, [2, 7]),
    ])
    def test_set_mark(self, color, marks, number, expected):
        r = Row(color)
        r.marks = marks
        r.set_mark(number)
        self.assertEqual((r.marks), expected)

    @parameterized.expand([
        ('green', [2], 7, RowIsLocked),
    ])
    def test_set_mark_not_can_mark(self, color, marks, number, mock_check_row_lock):
        r = Row(color)
        r.marks = marks
        with self.assertRaises(mock_check_row_lock):
            r.set_mark(number)

    @parameterized.expand([
        ('red', 12),
        ('yellow', 12),
        ('blue', 2),
        ('green', 2),
    ])
    def test_is_number_last(self, color, number):
        r = Row(color)
        self.assertEqual(r.is_number_last(number), True)

    @parameterized.expand([
        ('red', 'red'),
        ('green', 'green'),
    ])
    def test_is_locked(self, row, rows):
        with self.assertRaises(RowIsLocked):
            row = Row(row)
            row.blocked_rows.clear()
            row.blocked_rows.append(rows)
            row.is_locked
