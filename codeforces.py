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
