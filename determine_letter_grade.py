def determine_letter_grade(number_grade: int) -> str:
    if number_grade < 0:
        raise ValueError("Number grade cannot be negative")
    elif number_grade < 60:
        return 'F'
    elif number_grade < 70:
        return 'D'
    elif number_grade < 80:
        return 'C'
    elif number_grade < 90:
        return 'B'
    elif number_grade <=100:
        return 'A'
    else:
        raise ValueError("Number grade cannot be over 100")
