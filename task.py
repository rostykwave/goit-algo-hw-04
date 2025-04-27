import random
import timeit
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Callable

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Implementation of insertion sort algorithm
    """
    arr = arr.copy()  # Create a copy to avoid modifying the original array
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted arrays
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr: List[int]) -> List[int]:
    """
    Implementation of merge sort algorithm
    """
    arr = arr.copy()  # Create a copy to avoid modifying the original array
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def timsort(arr: List[int]) -> List[int]:
    """
    Python's built-in Timsort
    """
    return sorted(arr)

def measure_time(sorting_func: Callable, arr: List[int], number: int = 10) -> float:
    """
    Measure the average execution time of a sorting function
    """
    # Create a copy of the array for each test to ensure fairness
    return timeit.timeit(lambda: sorting_func(arr.copy()), number=number) / number

def generate_random_array(size: int) -> List[int]:
    """
    Generate a random array of integers
    """
    return [random.randint(0, 10000) for _ in range(size)]

def generate_sorted_array(size: int) -> List[int]:
    """
    Generate an already sorted array
    """
    return list(range(size))

def generate_reversed_array(size: int) -> List[int]:
    """
    Generate a reverse-sorted array
    """
    return list(range(size, 0, -1))

def generate_partially_sorted_array(size: int) -> List[int]:
    """
    Generate a partially sorted array (first half sorted, second half random)
    """
    sorted_part = list(range(size // 2))
    random_part = [random.randint(0, 10000) for _ in range(size - size // 2)]
    return sorted_part + random_part

def run_benchmarks():
    # Array sizes to test
    sizes = [100, 500, 1000, 2000, 5000]
    
    # Configure number of repetitions for timing
    num_tests = 5  # reduce for larger arrays
    
    # Results dictionaries
    random_results = {
        "Insertion Sort": [],
        "Merge Sort": [],
        "Timsort": []
    }
    
    sorted_results = {
        "Insertion Sort": [],
        "Merge Sort": [],
        "Timsort": []
    }
    
    reversed_results = {
        "Insertion Sort": [],
        "Merge Sort": [],
        "Timsort": []
    }
    
    partially_sorted_results = {
        "Insertion Sort": [],
        "Merge Sort": [],
        "Timsort": []
    }
    
    # For each size, generate arrays and measure sorting times
    for size in sizes:
        print(f"Testing with array size: {size}")
        
        # Generate different types of arrays
        random_array = generate_random_array(size)
        sorted_array = generate_sorted_array(size)
        reversed_array = generate_reversed_array(size)
        partially_sorted_array = generate_partially_sorted_array(size)
        
        # Measure sorting times for random array
        insertion_time = measure_time(insertion_sort, random_array, num_tests)
        merge_time = measure_time(merge_sort, random_array, num_tests)
        timsort_time = measure_time(timsort, random_array, num_tests)
        
        random_results["Insertion Sort"].append(insertion_time)
        random_results["Merge Sort"].append(merge_time)
        random_results["Timsort"].append(timsort_time)
        
        # Measure sorting times for sorted array
        insertion_time = measure_time(insertion_sort, sorted_array, num_tests)
        merge_time = measure_time(merge_sort, sorted_array, num_tests)
        timsort_time = measure_time(timsort, sorted_array, num_tests)
        
        sorted_results["Insertion Sort"].append(insertion_time)
        sorted_results["Merge Sort"].append(merge_time)
        sorted_results["Timsort"].append(timsort_time)
        
        # Measure sorting times for reversed array
        insertion_time = measure_time(insertion_sort, reversed_array, num_tests)
        merge_time = measure_time(merge_sort, reversed_array, num_tests)
        timsort_time = measure_time(timsort, reversed_array, num_tests)
        
        reversed_results["Insertion Sort"].append(insertion_time)
        reversed_results["Merge Sort"].append(merge_time)
        reversed_results["Timsort"].append(timsort_time)
        
        # Measure sorting times for partially sorted array
        insertion_time = measure_time(insertion_sort, partially_sorted_array, num_tests)
        merge_time = measure_time(merge_sort, partially_sorted_array, num_tests)
        timsort_time = measure_time(timsort, partially_sorted_array, num_tests)
        
        partially_sorted_results["Insertion Sort"].append(insertion_time)
        partially_sorted_results["Merge Sort"].append(merge_time)
        partially_sorted_results["Timsort"].append(timsort_time)
    
    # Plot the results
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    
    # Plot for random arrays
    plot_results(axs[0, 0], sizes, random_results, "Random Arrays")
    
    # Plot for sorted arrays
    plot_results(axs[0, 1], sizes, sorted_results, "Sorted Arrays")
    
    # Plot for reversed arrays
    plot_results(axs[1, 0], sizes, reversed_results, "Reversed Arrays")
    
    # Plot for partially sorted arrays
    plot_results(axs[1, 1], sizes, partially_sorted_results, "Partially Sorted Arrays")
    
    plt.tight_layout()
    plt.savefig('sorting_comparison.png')
    plt.show()
    
    # Print numerical results
    print("\nRandom Arrays Results:")
    print_results(sizes, random_results)
    
    print("\nSorted Arrays Results:")
    print_results(sizes, sorted_results)
    
    print("\nReversed Arrays Results:")
    print_results(sizes, reversed_results)
    
    print("\nPartially Sorted Arrays Results:")
    print_results(sizes, partially_sorted_results)

def plot_results(ax, sizes, results, title):
    """
    Helper function to plot results
    """
    for algo, times in results.items():
        ax.plot(sizes, times, marker='o', label=algo)
    
    ax.set_xlabel('Array Size')
    ax.set_ylabel('Time (seconds)')
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

def print_results(sizes, results):
    """
    Helper function to print numerical results
    """
    # Print header
    print(f"{'Size':<10}", end="")
    for algo in results.keys():
        print(f"{algo:<20}", end="")
    print()
    
    # Print data
    for i, size in enumerate(sizes):
        print(f"{size:<10}", end="")
        for algo in results.keys():
            print(f"{results[algo][i]:.6f}s{'':<13}", end="")
        print()

if __name__ == "__main__":
    run_benchmarks()
