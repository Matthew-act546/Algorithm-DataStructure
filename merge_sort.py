from random import randint

def merge_sort(list):
    """
    Sorts a list in ascending order 
    returns a new sorted list.

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Runs overall O(n log n)
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Takes overall O(log n) runtime
    """
    midpoint = len(list)//2
    left = list[:midpoint]
    right = list[midpoint:]

    return left, right

def merge(left, right):
    """
    Merges two lists, sorting them in the process
    returns a new merged list

    Runs in overall O(n)    
    """

    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result

def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    

    return ((list[0] < list[1] or list[0] == list[1]) and verify_sorted(list[1:]))

numbers = [45, 65, 78, 33, 12 , 83, 90]

print(verify_sorted(merge_sort(numbers)))
print(verify_sorted(numbers))


##### Idea #####
amount = 100
alist = []
for i in range(amount):
    i = randint(1, 100)
    alist.append(i)

sorted_alist = merge_sort(alist)
print(alist)
print(verify_sorted(alist))
print()
print(sorted_alist)
print(verify_sorted(sorted_alist))