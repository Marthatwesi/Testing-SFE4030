def roman_to_integer(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in s[::-1]:
        value = roman_dict[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

# Test the function with various Roman numerals

test_cases = [
    ("I", 1),
    ("V", 5),
    ("X", 10),
    ("L", 50),
    ("C", 100),
    ("D", 500),
    ("M", 1000),
    ("XI", 11),
    ("IV", 4),
    ("XIV", 14),
    ("II", 2),
    ("I", 1),
    ("Z", 0),  # Invalid input should return 0
    ("XIZ", 0),  # Invalid input should return 0
    ("VV", 0),  # Invalid input should return 0
    ("", 0),  # Empty input should return 0
]

for roman_numeral, expected_result in test_cases:
    result = roman_to_integer(roman_numeral)
    print(f"The integer equivalent of {roman_numeral} is {result}. Expected: {expected_result}")
    assert result == expected_result, f"Test failed for {roman_numeral}."