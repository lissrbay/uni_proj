import random
random.seed()

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j + 1] < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
    return array

def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        leftside = array[middle:]
        rightside = array[:middle]
        merge_sort(leftside)
        merge_sort(rightside)
        i = j = k = 0
        while i < len(leftside) and j < len(rightside):
            if leftside[i] < rightside[j]:
                array[k] = leftside[i]
                i += 1
            else:
                array[k] = rightside[j]
                j += 1
            k += 1

        while i < len(leftside):
            array[k] = leftside[i]
            i += 1
            k += 1

        while j < len(rightside):
            array[k] = rightside[j]
            j += 1
            k += 1
            
def qsort(array): #wow so simple
    if array: return qsort([x for x in array if x < array[0]]) + [x for x in array if x == array[0]] + qsort([x for x in array if x > array[0]])
    return []

def insertion_sort(array):
    for i in range(len(array)):
        elem = array[i]
        j = i
        while j > 0 and array[j - 1] > elem:
            array[j] = array[j - 1]
            j -= 1
        array[j] = elem            

def selection_sort(array):
    for i in range(len(array) - 1):
        min_element = i
        for j in range(i + 1, len(array)):
            if array[min_element] > array[j]:
                min_element = j
        array[min_element], array[i] = array[i], array[min_element]
        
def quicksort(array, first, last):
    if first < last:
        mid_element = partition(array, first, last)
        quicksort(array, first, mid_element - 1)
        quicksort(array, mid_element + 1, last)

def partition(array, first, last):
    begin = first
    mid_element = array[first]
    first += 1
    while True:
        while first <= last and array[first] <= mid_element:
            first += 1
        while array[last] >= mid_element and last >= first:
            last -= 1
        if last < first:
            break
        else:
            array[first], array[last] = array[last], array[first]
    array[begin], array[last] = array[last], array[begin]
    return last
'''  
a = list()
for i in range(10, 0, -1):
    b = random.randint(0, 100)
    a.append(b)
for i in range(len(a)):
    print(a[i], end = " ")
print()
a = bubble_sort(a)
for i in range(len(a)):
    print(a[i], end = " ")
'''