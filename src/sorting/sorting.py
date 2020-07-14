# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    elements = len(left) + len(right)
    merged_arr = [0] * elements

    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged_arr[left_cursor+right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged_arr[left_cursor+right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
            merged_arr[left_cursor+right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
            merged_arr[left_cursor+right_cursor] = right[right_cursor]

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left, right = merge_sort(arr[:middle]), merge_sort(arr[middle:])

    return merge(left, right)

test = [2,1,7,6,9]

merge_sort(test)
# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass
