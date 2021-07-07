'''
Input: a List of integers where every int except one shows up twice
Returns: an integer

create storage for non repeating number
loop  over  range of array
loop over a second time,
if second pass through index equals first this is not the answer;
add  the index value not equal  to storage



'''


# def single_number(arr):
#
#     for i in range(0, len(arr)):
#         counter = 0
#         for j in range(0, len(arr)):
#             if arr[i] == arr[j]:
#                 counter += 1
#         if counter == 1:
#             return arr[i]

def single_number(arr):
    # Your code here
    # set new array to collect single integers
    result = arr[0]
    # loop over array and store
    for i in range(1, len(arr)):
        result ^= arr[i]
    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
