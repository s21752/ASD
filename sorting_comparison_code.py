import time
import sys
import random

def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def get_random_data(elements):
    list = []
    for i in range(0, elements):
        list.append(random.randrange(100))

    return list

def get_sorted_data(elements):
    list = []
    for i in range(0, elements):
        list.append(i)

    return list

def get_inversly_sorted_data(elements):
    list = []
    for i in range(0, elements):
        list.append(elements - i)

    return list

# Bubble sort
def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) - i - 1):
            if (array[j + 1] < array[j]):
                swap(array, j+1, j)
    
# Heap sort
def left(index):
    return 2 * index + 1

def right(index):
    return 2*(index + 1)

def heapify(heap, i, end, shortening = False):
    l = left(i)
    r = right(i)
    
    if l <= len(heap) - 1 - end and heap[l] > heap[i]:
        largest = l
    else:
        largest = i
    if r <= len(heap) - 1 - end and heap[r] > heap[largest]:
        largest = r
    if i != largest:
        swap(heap, largest, i)
        if (shortening) :
            end += 1
        heapify(heap, largest, end, shortening)
        
def build_heap(array):
    middle = (len(array) // 2) - 1
    
    while middle >= 0:
        heapify(array, middle, 0)
        middle -= 1

def heap_sort(array):
    build_heap(array)
    swap(array, 0, len(array) - 1)

    for i in range(1, len(array)):
        heapify(array, 0, i, True)
        swap(array, 0, len(array) - 1 - i)
    
# Quick sort
def partition(list, p, r):
    pivot = list[r]
    smaller = p
    for j in range(p, r):
        if list[j] <= pivot:
            swap(list, smaller, j)
            smaller = smaller + 1
    swap(list, smaller, r)
    return smaller

def quick_sort(list, p, r):
    if (p < r):
        q = partition(list, p, r)
        quick_sort(list, p, q-1)
        quick_sort(list, q+1, r)




    
    
sys.setrecursionlimit(60000)
    
print("Comparison between sorting algorithms: \n\n\n")
    
random1 = get_random_data(30000)
random2 = list(random1)
random3 = list(random1)

sorted1 = get_sorted_data(30000)
sorted2 = list(sorted1)
sorted3 = list(sorted1)

inversely_sorted1 = get_inversly_sorted_data(30000)

inversely_sorted2 = list(inversely_sorted1)
inversely_sorted3 = list(inversely_sorted1)

# # random data
quick_random_start = int(round(time.time() * 1000))
quick_sort(random1, 0, len(random1) - 1)
quick_random_time = int(round(time.time() * 1000)) - quick_random_start

print("Quick sort random data time: " + str(quick_random_time))


bubble_random_start = int(round(time.time() * 1000))
bubble_sort(random2)
bubble_random_time = int(round(time.time() * 1000)) - bubble_random_start

print("Bubble sort random data time: " + str(bubble_random_time))


heap_random_start = int(round(time.time() * 1000))
heap_sort(random3)
heap_random_time = int(round(time.time() * 1000)) - heap_random_start

print("Heap sort random data time: " + str(heap_random_time))


# # sorted data
quick_sorted_start = int(round(time.time() * 1000))
quick_sort(sorted1, 0, len(sorted1) - 1)
quick_sorted_time = int(round(time.time() * 1000)) - quick_sorted_start

print("\nQuick sort sorted data time: " + str(quick_sorted_time))


bubble_sorted_start = int(round(time.time() * 1000))
bubble_sort(sorted2)
bubble_sorted_time = int(round(time.time() * 1000)) - bubble_sorted_start

print("Bubble sort sorted data time: " + str(bubble_sorted_time))



heap_sorted_start = int(round(time.time() * 1000))
heap_sort(sorted3)
heap_sorted_time = int(round(time.time() * 1000)) - heap_sorted_start

print("Heap sort sorted data time: " + str(heap_sorted_time))


# # inversely sorted data
quick_inversely_sorted_start = int(round(time.time() * 1000))
quick_sort(inversely_sorted1, 0, len(inversely_sorted1) - 1)
quick_inversely_sorted_time = int(round(time.time() * 1000)) - quick_inversely_sorted_start

print("\nQuick sort inversely sorted data time: " + str(quick_inversely_sorted_time))



bubble_inversely_sorted_start = int(round(time.time() * 1000))
bubble_sort(inversely_sorted2)
bubble_inversely_sorted_time = int(round(time.time() * 1000)) - bubble_inversely_sorted_start

print("Bubble sort inversely sorted data time: " + str(bubble_inversely_sorted_time))


heap_inversely_sorted_start = int(round(time.time() * 1000))
heap_sort(inversely_sorted3)
heap_inversely_sorted_time = int(round(time.time() * 1000)) - heap_inversely_sorted_start

print("Heap sort inversely sorted data time: " + str(heap_inversely_sorted_time))
