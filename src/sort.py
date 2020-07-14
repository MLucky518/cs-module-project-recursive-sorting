# import time


# def partition(nums):
#     # this func breaksnumsinto a left pivot and right

    
#     left = []
#     pivot = numbers[0]
#     right = []

#     for num in nums[1:]:
#         if num <= pivot:
#             left.append(num)
#         else:
#             right.append(num)

#     return left,pivot,right



# def quick_sort(nums):
#     # base case
#     # what is the easiest array to sort
#     # Conquer
#     if len(nums) <= 1:
#         return numbers

#     # divide 
#     # figure out how to properly split the data

#     left,pivot,right = partition(nums)

#     pivot = [pivot]

#     sorted_array = quicksort(left) + pivot + quicksort(right)

#     return sorted_array