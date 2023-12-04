from day3 import *
def test_parts_1():
    question_text = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    assert parts_1(question_text) == 4361

def test_parts_2():
    question_text = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    assert parts_2(question_text) == 467835