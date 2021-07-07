'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    count = 0
    # Your code here
    # return [no_zero for no_zero in arr if no_zero != 0] + \
    #        [zero for zero in arr if zero == 0]
    for i in range(len(arr)):
        # Check to see if iteration is not 0
        if arr[i] != 0:
            # count is then sent to iteration
            arr[count] = arr[i]
            # then we increment the count by 1
            count += 1
    for i in range(count, len(arr)):
        # Second loop checks for existence of 0
        arr[i] = 0
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
