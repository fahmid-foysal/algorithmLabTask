import random
import time

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, low, high, comparisons):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparisons[0] += 1
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1

def quick_sort(arr, low, high, comparisons):
    if low < high:
        pi = partition(arr, low, high, comparisons)
        quick_sort(arr, low, pi - 1, comparisons)
        quick_sort(arr, pi + 1, high, comparisons)

def generate_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

def run_experiment(input_sizes):
    for size in input_sizes:
        arr = generate_random_array(size)
        comparisons = [0]

        start_time = time.time()
        quick_sort(arr, 0, size - 1, comparisons)
        end_time = time.time()

        print(f"\nn = {size}")
        print(f"Number of comparisons: {comparisons[0]}")
        print(f"Time taken: {end_time - start_time:.6f} seconds")


# Main block
if __name__ == "__main__":
    input_sizes = list(map(int, input("Enter input sizes separated by space: ").split()))
    run_experiment(input_sizes)
