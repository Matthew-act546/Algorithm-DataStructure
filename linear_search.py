num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target = 6

def linear_search(list, target):
    for i in range(len(list)):
        if num[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print(f"target found at index: {index}")
    else:
        print("Not Found")

result = linear_search(num, target)

verify(result)