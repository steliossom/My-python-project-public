import pytest

from app.math_operations import add_numbers

class TestMathOperations:

    def test_add_positive_numbers(self):
        assert add_numbers(1.5, 2.5) == 4.0

    def test_add_negative_numbers(self):
        assert add_numbers(-1.5, -2.5) == -4.0

    def test_add_mixed_numbers(self):
        assert add_numbers(-1.5, 2.5) == 1.0

    def test_add_zero(self):
        assert add_numbers(0, 5) == 5.0
        assert add_numbers(5, 0) == 5.0
        assert add_numbers(0, 0) == 0.0

    def test_add_large_numbers(self):
        assert add_numbers(1e10, 1e10) == 2e10

    def test_add_floats(self):
        assert add_numbers(1.1, 2.2) ==  pytest.approx(3.3)

    def test_add_integers(self):
        assert add_numbers(1, 2) == 3.0

    def test_add_string_input(self):
        with pytest.raises(TypeError):
            add_numbers("1", 2)

    def test_add_none_input(self):
        with pytest.raises(TypeError):
            add_numbers(None, 2)