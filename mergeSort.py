import time
import random
import matplotlib.pyplot as plt
comparison_count = 0
def merge(arr, start, mid, end):
    global comparison_count
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]

    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        comparison_count += 1
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort(arr, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, start, mid, end)

def read_array_from_file(filename):
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file.readlines()]

def generate_random_file(filename, size):
    with open(filename, "w") as file:
        for _ in range(size):
            file.write(str(random.randint(1, 100000)) + "\n")

def experiment(n):
    global comparison_count
    filename = f"input_{n}.txt"
    generate_random_file(filename, n)
    arr = read_array_from_file(filename)

    comparison_count = 0
    start_time = time.time()
    merge_sort(arr, 0, len(arr) - 1)
    end_time = time.time()

    duration = end_time - start_time
    print(f"\nn = {n}")
    print(f"Number of comparisons: {comparison_count}")
    print(f"Time taken: {duration:.6f} seconds")

    return n, duration

def plot_graph(results):
    sizes = [n for n, _ in results]
    times = [t for _, t in results]

    plt.plot(sizes, times, marker='o')
    plt.title("Merge Sort: Time vs Input Size")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.savefig("merge_sort_graph.png")
    plt.show()

if __name__ == "__main__":

    test_sizes = list(map(int, input("Enter input sizes separated by space: ").split()))

    results = []

    for n in test_sizes:
        result = experiment(n)
        results.append(result)

    plot_graph(results)
