"""Mergesort is a classic divide and conquer
sorting algorithm that runs in nlogn time. The
basic idea is to recursively partition until you
get to one element lists, which are already sorted,
and then combine back up by way of a helper
function, merge.
"""
def mergeSort(arr):
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    mergeSort(left)
    mergeSort(right)

    return merge(left, right)

def merge(left, right):
    lenleft = len(left)
    lenright = len(right)
    lpointer = 0
    rpointer = 0
    returnList = []

    while lpointer < lenleft and rpointer < lenright:
        if left[lpointer] <= right[rpointer]:
            returnList.append(left[lpointer])
            lpointer += 1
        else:
            returnList.append(right[rpointer])
            rpointer += 1

    while lpointer < lenleft:
        returnList.append(left[lpointer])
        lpointer += 1

    while rpointer < lenright:
        returnList.append(right[rpointer])
        rpointer += 1

    return returnList

"""QuickSort is basically the fastest sorting algorithm
out there. It, like mergeSort, is a divide and conquer
algorithm. The difference is that we partition instead of
dividing in half, relying on a partition helper function.
"""
def quickSort(arr):
    p = partition(arr)


def partition(arr):
    i = 0
    pivot = arr[len(arr) - 1]
    for j in range(len(arr)):
        if pivot => arr[j]:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
