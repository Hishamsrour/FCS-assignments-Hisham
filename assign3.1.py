def binary_search (list1, num, end, start):
    if start >= end:
        mid = (start + end) // 2
        
        if list1[mid] == num:
            return mid
        elif list1[mid] > num:
            return binary_search(list1, num, end, mid - 1)
        else:
            return binary_search(list1, num, mid + 1, start)
    else:
        return -1

#example
list1 = [1, 3, 5, 7, 9, 11, 13]
num = 7
result = binary_search(list1, num, 0, len(list1) - 1)
print(f"Element {num} is at index: {result}")