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
    """
    Merges two linked list (left and right), sorting by data in nodes
    Returns a new, merged list.
    """

    # Create a new linked list that contains nodes from
    # Merging left and right.
    merged= LinkedList()

    # Add a fake head that is discarded it later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes from the left and right of the linked list  
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node of either
    while left_head or right_head:
        # If the head node of left is none, were past the tail node
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head 
            # Call next on right to set the loop fucnctions to False 
            right_head = right_head.next_node
        # If the head node of right is None, we're past the tail 
        # Add the tail node from the left to merged linked list.
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set the loop fucnctions to False 
            left_head = left_head.next_node
        else:
            # Nota at either tail node
            # Obtain node data to perform comparison operations 
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # If data on left is greater than right, set current to left node
            else:
                current.next_node = right_head
                # move right to next node
                right_head = right_head.next_node



def verify_sorted(linked_list):
    n = linked_list.size()
    flag = False
    
    if n == 0 or n == 1:
        return True
    if linked_list[0] == linked_list[1]:
        flag =  True

    return ((linked_list[0] < linked_list[1] or flag) and verify_sorted(linked_list[1:]))
