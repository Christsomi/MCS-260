import time
import random

def selection_sort(L):
    n = len(L)
    for c in range(n-1):
        m = L[c]
        index = c
        for i in range(c, n):
            if L[i] < m:
                m = L[i]
                index = i 
        L[c], L[index] = L[index], L[c]

def test_random_lists():
    for _ in range(5):
        random_list = [random.randint(0, 100) for _ in range(10)]  
        print("Original random list:", random_list)
        selection_sort(random_list)
        print("Sorted random list:", random_list)
        print()

def test_large_list():
    large_random_list = [random.randint(0, 100000) for _ in range(10000)]
    start_time = time.perf_counter()
    selection_sort(large_random_list)
    end_time = time.perf_counter()
    print("Time taken to sort a large list:", end_time - start_time, "seconds")

def test_string_list():
    string_list = ["green", "red", "orange", "blue", "yellow"]
    print("Original string list:", string_list)
    selection_sort(string_list)
    print("Sorted string list:", string_list)

def time_different_sizes():
    sizes = [10, 100, 1000, 10000]
    for size in sizes:
        test_list = [random.randint(0, 100) for _ in range(size)]
        start_time = time.perf_counter()
        selection_sort(test_list)
        end_time = time.perf_counter()
        print(f"Time taken to sort a list of size {size}: {end_time - start_time} seconds")

def test_sorted_vs_random():
    sorted_list = list(range(1000))
    random.shuffle(sorted_list)  
    start_time_sorted = time.perf_counter()
    selection_sort(sorted_list)
    end_time_sorted = time.perf_counter()
    print("Time taken to sort an already sorted list:", end_time_sorted - start_time_sorted, "seconds")

    random_list = [random.randint(0, 1000) for _ in range(1000)]
    start_time_random = time.perf_counter()
    selection_sort(random_list)
    end_time_random = time.perf_counter()
    print("Time taken to sort a random list:", end_time_random - start_time_random, "seconds")

test_random_lists()
test_large_list()
test_string_list()
time_different_sizes()
test_sorted_vs_random()
