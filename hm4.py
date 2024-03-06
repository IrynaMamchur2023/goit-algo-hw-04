import timeit
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def test_sorting_algorithms():
    arr = [random.randint(1, 1000) for _ in range(1000)]

    merge_sort_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)

    insertion_sort_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)

    timsort_time = timeit.timeit(lambda: sorted(arr.copy()), number=1)

    print("Merge Sort Time:", merge_sort_time)
    print("Insertion Sort Time:", insertion_sort_time)
    print("Timsort Time:", timsort_time)

if __name__ == "__main__":
    test_sorting_algorithms()