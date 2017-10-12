"""Split astring by splitter and return list of splits.

This should work like that built-in Python .split() method [*].
YOU MAY NOT USE the .split() method in your solution!
YOU MAY NOT USE regular expressions in your solution!

For example:

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

* Note: the actual Python split method has special behavior
  when it is not passed anything for the splitter -- you do
  not need to implemented that.

"""


def split(astring, splitter):
    """Split astring by splitter and return list of splits."""

    # when no more instances of splitter, append rest of str to result
    # return result

    # initialize result lst + starting idx
    # keep track of idx
    result = []
    idx = 0

    # loop until str finished
    while idx <= len(astring):

        # initialize current idx. will use current idx + idx for list slicing.
        curr_idx = idx

        # use .find()
            # e.g. str.find(what you're looking for, start idx, end idx)
            # if found, returns idx
            # if not, returns -1
        idx = astring.find(splitter, idx)

        # when found, append starting idx til idx where you found splitter
        # via list slicing. then, update idx for while loop.
        if idx != -1:
            result.append(astring[curr_idx:idx])
            idx += len(splitter)

        # when splitter no longer found, append remaining str to result
        else:
            result.append(astring[curr_idx:])
            break

    return result


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. FINE SPLITTING!\n"
