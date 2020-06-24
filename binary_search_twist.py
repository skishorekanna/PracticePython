"""
Implement a binary search in a sorted and rotated array
"""

def binary_search(array, element):
    low = 0
    high = len(array)-1
    while(low<=high):
        mid = int((low+high)/2)
        if(array[mid]==element):
            return mid
        elif(element>array[mid]):
            low=mid+1
        else:
            high=mid-1


def find_pivot(array):
    low = 0
    high = len(array)-1
    while(low<=high):
        mid = int((low+high)/2)
        if mid+1>len(array)-1:
            return -1
        if(array[mid+1]<array[mid]):
            return mid
        elif(array[low]>array[mid]):
            high=mid-1
        else:
            low=mid+1

def binary_search_twist(array, element):
    pivot = find_pivot(array)
    if pivot == -1:
        return binary_search(array,element)
    else:
        # We have split the series
        # 0 to pivot and pivot to end
        low = 0
        high = len(array)-1
        print("element is {}".format(element))
        if element>=array[pivot+1] and element<=array[high]:
            print("searching in {}".format(array[pivot+1:]))
            return binary_search(array[pivot+1:high],element)
        elif element>=array[low]and element<=array[pivot]:
            print("searching in {}".format(array[low:pivot+1]))
            return binary_search(array[low:pivot+1],element)

