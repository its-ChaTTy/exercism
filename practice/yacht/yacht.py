# Score categories.
# Change the values as you see fit.
YACHT = 'YACHT'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):
    if category in (1,2,3,4,5,6):
         return dice.count(category) * category
    elif category == 'FULL_HOUSE':
        if len(set(dice)) == 2 and dice.count(dice[0]) in [2, 3]:
            return sum(dice) or 0
    elif category == 'FOUR_OF_A_KIND':
        if dice[0] == dice[3] or dice[1] == dice[4]:
            return dice[1] * 4 or 0
    elif category == 'LITTLE_STRAIGHT':
        if sorted(dice) == [1, 2, 3, 4, 5]: 
            return 30 or 0
    elif category == 'BIG_STRAIGHT':
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30 or 0
    elif category == 'YACHT':
        if all(num == dice[0] for num in dice):
            return 50
    elif category == 'CHOICE':
        return sum(dice)
    return 0
