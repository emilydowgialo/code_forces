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


# http://codeforces.com/problemset/problem/71/A
def too_long_words(word):
    """ If word is longer than 10 letters return the first and last letters of
    the word with the number of letters between the first and last between those letters

    >>> too_long_words("localization")
    l10n

    >>> too_long_words("word")
    word
    """

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

# c = raw_input()
# count = 0
# while count < int(c):
#     too_long_words(raw_input())
#     count += 1


# http://codeforces.com/problemset/problem/158/A
def next_round(score):
    """ Check if score is higher than what it needs to be """

    if score == 0:
        return False

    if score > int(need_higher_than_this) or score == int(need_higher_than_this):
        return True


# d = raw_input()
d = "4 2"
d = d.split()
print d
num_participants = int(d[0])
need_higher_than_this_person = int(d[1])

going_to_next_round = 0
# scores = raw_input()
scores = "0 0 0 0"
scores_split = scores.split()
need_higher_than_this = scores_split[need_higher_than_this_person - 1]
print need_higher_than_this
print scores_split

for score in scores_split:
    if int(score) <= 0:
        pass
    is_this_more = next_round(int(score))
    if is_this_more is True:
        going_to_next_round += 1

print going_to_next_round


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
