from division_data_class import *

steps_0 = [
    DivisionStep(
        "x^2",
        [
            "(x^3 + 3x^2)",
            "-(x^3 + 3x^2)",
            "-x^3 - 3x^2"
        ],
        [
            ["0x^3 + 0x^2 -4x - 12"], 
            ["-4x", "- 12"]
        ]
    ),

    DivisionStep(
         "-4",
        [
            "(-4x - 12)",
            "-(-4x - 12)",
            "4x + 12"
        ],
        [
            ["0x - 0"], 
            ["0"]
        ], 
        is_last = True
    )
]

steps_1 = [
    DivisionStep(
        "x^2",
        [
            "(2x^4 - 5x^3 + 2x^2)",
            "-(2x^4 - 5x^3 + 2x^2)",
            "-2x^4 + 5x^3 - 2x^2"
        ],
        [
            ["0x^4 + 14x^2 - 35x + 14"], 
            ["14x^2", "- 35x + 14"]
        ]
    ),
    DivisionStep(
        "+7",
        [
            "(14x^2 - 35x + 14)",
            "-(14x^2 - 35x + 14)",
            "-14x^2 + 35x - 14"
        ],
        [
            ["0x^2 + 0x - 0"], 
            ["0"]
        ], is_last=True
    )
]

polys_to_divide = (
    DivisionData(
        ["(", "x^3", "+ 3x^2 - 4x - 12) :"],
        ["(", "x", "+ 3)"],
        steps_0
    ),

    DivisionData(
        ["(", "2x^4", "- 5x^3 + 16x^2 - 35x + 14) :"],
        ["(", "2x^2", "- 5x + 2)"],
        steps_1
    ),
)
