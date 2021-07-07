#!/usr/bin/python

import sys


def making_change(amount, denominations):
    # Your code here
    # loop over the length of denominations and store in new list
    ways_list = [0 for i in range(amount + 1)]
    ways_list[0] = 1  # Base case start the list with the value of 1
    # loop over denominations
    for k in denominations:
        # in list find for each number starting at 1 increment
        for num in range(1, amount + 1):
            # check to see if iteration is less than or equal to each number
            if k <= num:
                # increment the value of the denominatio with a decremented value of the iteration
                ways_list[num] += ways_list[num - k]
    return ways_list[amount]


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
