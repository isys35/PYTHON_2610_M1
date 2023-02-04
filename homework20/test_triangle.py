from contextlib import nullcontext as does_not_raise
from decimal import Decimal

import pytest

from homework8.task3 import is_triangle


@pytest.mark.parametrize("side_a, side_b, side_c, expected_result", [
    (Decimal("5"), Decimal("6"), Decimal("8"), True),
    (Decimal("1"), Decimal("2"), Decimal("3"), False),
    (Decimal("1.1"), Decimal("5.2"), Decimal("6.3"), False)
])
def test_is_triangle(side_a, side_b, side_c, expected_result):
    assert is_triangle(side_a, side_b, side_c) == expected_result


@pytest.mark.parametrize("side_a, side_b, side_c, expectation", [
    (Decimal("0"), Decimal("2"), Decimal("4"), pytest.raises(ValueError, match="Сторона треугольника не может быть "
                                                                               "меньше или равна 0.")),
    (Decimal("2"), Decimal("5"), Decimal("6"), does_not_raise())
])
def test_exception(side_a, side_b, side_c, expectation):
    with expectation:
        assert is_triangle(side_a, side_b, side_c) is not None
