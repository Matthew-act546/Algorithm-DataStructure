from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order 
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list
    
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head == None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted linked list
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        midpoint = linked_list.size() // 2

        mid_node = linked_list.node_at_index(midpoint - 1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(right) and right_index < len(right):
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

def verify_sorted(linked_list):
    n = linked_list.size()
    flag = False
    
    if n == 0 or n == 1:
        return True
    if linked_list[0] == linked_list[1]:
        flag =  True

    return ((linked_list[0] < linked_list[1] or flag) and verify_sorted(linked_list[1:]))





