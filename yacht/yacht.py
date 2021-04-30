"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.


def fn_score_choice(dice):
    return sum(dice)


def fn_score_one(number):
    def score_one_wrapped(dice):
        counts = count_dices(dice)
        return number * counts.get(number, 0)
    return score_one_wrapped


def fn_score_four(dice):
    counts = count_dices(dice)
    number_four_times_or_more = [key for key, value in counts.items() if value >= 4]
    if not number_four_times_or_more:
        return 0
    return number_four_times_or_more[0] * 4


def fn_score_yacht(dice):
    counts = count_dices(dice)
    if len(set(counts)) == 1:
        return 50
    return 0


def fn_score_full_house(dice):
    counts = count_dices(dice)
    different_numbers = list(set(dice))
    if len(different_numbers) != 2:
        return 0
    number_one = different_numbers[0]
    number_two = different_numbers[1]
    counts_one = counts[number_one]
    counts_two = counts[number_two]
    if counts_one != 2 and counts_one != 3:
        return 0
    return number_one * counts_one + number_two * counts_two


def fn_score_sequence(start, end):
    def fn_score_sequence_wrapped(dice):
        if len(set(dice)) < 5:
            return 0
        sequence = list(range(start, end + 1))
        if sequence != sorted(dice):
            return 0
        return 30
    return fn_score_sequence_wrapped


YACHT = fn_score_yacht
ONES = fn_score_one(1)
TWOS = fn_score_one(2)
THREES = fn_score_one(3)
FOURS = fn_score_one(4)
FIVES = fn_score_one(5)
SIXES = fn_score_one(6)
FULL_HOUSE = fn_score_full_house
FOUR_OF_A_KIND = fn_score_four
LITTLE_STRAIGHT = fn_score_sequence(1, 5)
BIG_STRAIGHT = fn_score_sequence(2, 6)
CHOICE = fn_score_choice


def score(dice, category):
    return category(dice)


def count_dices(dice):
    counts = {}
    for number in dice:
        if number not in counts:
            counts[number] = 1
        else:
            counts[number] += 1
    return counts
