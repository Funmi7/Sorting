# STRETCH: implement Linear Search
def linear_search(arr, target):

  # TO-DO: add missing code

    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    while low <= high:
        middle = (low + high) // 2
        if target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1
        else:
            return middle

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    # if target == arr[middle]:
    #     
    if target < arr[middle]:
        binary_search_recursive(arr, low, middle - 1, target)
    elif target > arr[middle]:
        binary_search_recursive(arr, middle + 1, high,  target)
    else:
        return middle

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search_recursive(arr1, -8, 0, len(arr1)-1))