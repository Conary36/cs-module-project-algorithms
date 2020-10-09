#!/usr/bin/python

import sys


def making_change(amount, denominations):
    # Your code here
    #  check if input is small, or large amount.

    for i in range(0, denominations):
        if amount >= denominations[i]:
            #  denominations are a list of Integers  chosen by user.
            #  return the value from the amount by the denominations
            denominations[i] += denominations[amount - 1]

    return denominations[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations),
                                                                     amount=amount))
    else:
        print("Usage: making_change.py [amount]")
