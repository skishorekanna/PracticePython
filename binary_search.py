"""
Implement a simple binary search on a list for element
"""

def binary_search(array, element):
    low = 0
    high = len(array) -1
    flag = False
    while(low<=high):
        mid = int((low+high)/2)
        if array[mid]==element:
            flag = True
            print("Element found at {}".format(mid))
            break
        elif element < array[mid]:
            high = mid-1
        elif element > array[mid]:
            low = mid + 1
    if not flag:
        print("Element is not found")
