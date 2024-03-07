class HornerExercise:
    def __init__(self, 
        dividend,
        factors,
        results,
        divider,
        calculations,
        result_text,
        is_shorten = False
    ) -> None:
        
        self.dividend = dividend
        self.factors = factors
        self.results = results
        self.divider = divider
        self.calculations = calculations
        self.result_text = result_text
        self.is_shorten = is_shorten

exercises = [
    HornerExercise(
        dividend = ("x^3", "- 4x^2", "+ x", "+ 6"),
        factors = [1, -4, 1, 6],
        results = [1, -2, -3, 0],
        divider = 2,
        calculations = [
            "1 * 2 + (-4)",
            "(-2) * 2 + 1",
            "(-3) * 2 + 6"
        ],
        result_text = ("1x^2", "-2x^1", "-3x^0"),
    ),
    HornerExercise(
        dividend = ("x^4", "+ 4x^3", "- 7x^2", "- 22x", "+ 24"),
        factors = [1, 4, -7, -22, 24],
        results = [1, 1, -10, 8, 0],
        divider = -3,
        calculations = [
            "1 * (-3) + 4",
            "1 * (-3) + (-7)",
            "(-10) * (-3) + (-22)",
            "8 * (-3) + 24"
        ],
        result_text = ("1x^3", "+ 1x^2", "- 10x", "+ 8"),
    ),
    HornerExercise(
        dividend = ("x^3", "-1"),
        factors = [1, 0, 0, -1],
        results = [1, 1, 1, 0],
        divider = 1,
        calculations = [
            "1 * 1 + 0",
            "1 * 1 + 0",
            "1 * 1 + (-1)",
        ],
        result_text = ("x^2", "+ x", "+ 1"),
        is_shorten = True
    ),
]