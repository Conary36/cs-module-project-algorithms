'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here
    # Store the products of the other numbers in a variable
    product = 1
    # All the values of the products stored in a list
    list_of_products = []
    for i in range(0, len(arr)):  # loop through the array
        for k in arr:  # for each number in array
            if k != arr[i]:  # number not equal to iteration in array
                product *= k  # multiply the product
        list_of_products.append(product) # add product to new list
        product = 1
    return list_of_products


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8,
           5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
