# http://codeforces.com/problemset/problem/1/A
def theatre_square(stuff):
    """
    For example::

    >>> theatre_square("50 5 4")
    26

    >>> theatre_square("6 6 4")
    4

    """

    # Split string
    stuff_split = stuff.split()

    # Bind variables
    n = int(stuff_split[0])
    m = int(stuff_split[1])
    a = int(stuff_split[2])

    # Call helper function to get how many tiles per side are needed
    side_m = side_measurer(m, a)
    side_n = side_measurer(n, a)

    # Return num tiles per side multiplied to get the total
    return (side_m * side_n)


def side_measurer(side, a):
    """ Helper function for theatre_square """

    # This gives the number of tiles per side
    num_tiles = (side / a)

    # If there are any remaining, because we can go over the area, we add 1
    if (side % a) > 0:
        num_tiles += 1

    return num_tiles


###############################################################################
# http://codeforces.com/problemset/problem/71/A
def too_long_words(word):
    """ If word is longer than 10 letters return the first and last letters of
    the word with the number of letters between the first and last between those letters

    >>> too_long_words("localization")
    l10n

    >>> too_long_words("word")
    word
    """

    # If work is longer than 10 letters, print the word according to these rules
    if len(word) > 10:
        print word[0] + str(len(word[1:-1])) + word[-1]

    else:
        print word


# def get_words(input):

#     input_split = input.split('\n')
#     print input_split

#     n = int(input_split[0])

#     count = 0
#     while count < n:
#         too_long_words(input_split[count + 1])
#         count += 1

# c is the number of words to get from stdin, so this loops up until that number
# c = raw_input()
# count = 0
# while count < int(c):
#     too_long_words(raw_input())
#     count += 1

###############################################################################
# http://codeforces.com/problemset/problem/158/A
def next_round(score):
    """ Check if score is higher than what it needs to be """

    # If score is 0 we want to return false otherwise this will incorrectly
    # return True
    if score == 0:
        return False

    if score > int(need_higher_than_this) or score == int(need_higher_than_this):
        return True


# d = raw_input()
d = "4 2"

# d includes the number of participants plus the place in the list of scores
# where the score to beat is located
d = d.split()

# Get the number of participants and the score they need to beat
num_participants = int(d[0])
need_higher_than_this_person = int(d[1])

# Initialize the going to next round count at 0
going_to_next_round = 0
# scores = raw_input()
scores = "0 0 0 0"

# Split the scores input to create a list we iterate over
scores_split = scores.split()

# This is the score to beat
need_higher_than_this = scores_split[need_higher_than_this_person - 1]

# Check each score using the next_round function to see if it passes the test
for score in scores_split:
    if int(score) <= 0:
        pass
    is_this_more = next_round(int(score))
    if is_this_more is True:
        going_to_next_round += 1

# Print how many people continue on to the next round
# print going_to_next_round


###############################################################################
# http://codeforces.com/problemset/problem/118/A


# f = raw_input()
f = "aBAcAba"
f = f.lower()
f = list(f)
vowels = ['a', 'o', 'y', 'e', 'u', 'i']

not_a_vowel = []

for letter in f:
    if letter not in vowels:
        not_a_vowel.append(letter)

without_vowels = ""
for letter in not_a_vowel:
    without_vowels = without_vowels + "." + letter

# print without_vowels


###############################################################################
# http://codeforces.com/problemset/problem/4/A
def watermelon(weight):
    """ Check if a watermelon can be divided into 2 even parts

    >>> watermelon(8)
    'YES'

    >>> watermelon(2)
    'NO'

    """

    # 2 is the only even number that does not work
    if weight == 2:
        return "NO"

    if (weight % 2) == 0:
        return "YES"

    else:
        return "NO"

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ROCK!\n"
