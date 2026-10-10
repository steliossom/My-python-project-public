import pytest

from app.determine_letter_grade import determine_letter_grade

class TestDetermineLetterGrade:

    def test_grade_A(self):
        assert determine_letter_grade(90) == 'A'
        assert determine_letter_grade(100) == 'A'

    def test_grade_B(self):
        assert determine_letter_grade(80) == 'B'
        assert determine_letter_grade(89) == 'B'

    def test_grade_C(self):
        assert determine_letter_grade(70) == 'C'
        assert determine_letter_grade(79) == 'C'

    def test_grade_D(self):
        assert determine_letter_grade(60) == 'D'
        assert determine_letter_grade(69) == 'D'

    def test_grade_F(self):
        assert determine_letter_grade(0) == 'F'
        assert determine_letter_grade(59) == 'F'

    def test_negative_grade(self):
        with pytest.raises(ValueError, match="Number grade cannot be negative"):
            determine_letter_grade(-1)

    def test_over_hundred_grade(self):
        with pytest.raises(ValueError, match="Number grade cannot be over 100"):
            determine_letter_grade(101)