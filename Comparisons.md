# HW2
Comparison of QuickSort and MergeSort

def partition(lst, begin, end):
    pivot = begin
    for i in range(begin+1,end+1):
        if lst[i] <= lst[begin]:
            pivot += 1
            lst[i], lst[pivot] = lst[pivot], lst[i]
    lst[pivot], lst[begin] = lst[begin], lst[pivot]
    return pivot

def quicksort(lst,begin,end):
    if begin < end:
    pos = partition(lst, begin, end) # partition returns the pivot
    print pos, lst[begin:end]
    quicksort(lst, begin, pos-1) # first part of the list (from beginning until pivot)
    quicksort(lst, pos+1, end) # second part (from pivot to end, pivot excluded)
    return lst
