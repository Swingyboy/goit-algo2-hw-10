import random
import time
import pandas as pd
import matplotlib.pyplot as plt

from deterministic_qs import deterministic_quick_sort
from randomized_qs import randomized_quick_sort

# Test parameters
sizes = [10_000, 50_000, 100_000, 500_000]
repeats = 5
results = []

for size in sizes:
    array = [random.randint(0, 1_000_000) for _ in range(size)]

    det_times = []
    for _ in range(repeats):
        arr_copy = array[:]
        start_time = time.time()
        deterministic_quick_sort(arr_copy)
        det_times.append(time.time() - start_time)

    rand_times = []
    for _ in range(repeats):
        arr_copy = array[:]
        start_time = time.time()
        randomized_quick_sort(arr_copy)
        rand_times.append(time.time() - start_time)

    results.append({
        "Size": size,
        "Deterministic Average Time": sum(det_times) / repeats,
        "Randomized Average Time": sum(rand_times) / repeats,
    })

df_results = pd.DataFrame(results)

plt.figure(figsize=(10, 6))
plt.plot(df_results["Size"], df_results["Deterministic Average Time"], marker='o', label="Deterministic QuickSort")
plt.plot(df_results["Size"], df_results["Randomized Average Time"], marker='o', label="Randomized QuickSort")
plt.xlabel("Array Size")
plt.ylabel("Average Execution Time (seconds)")
plt.title("QuickSort Performance Comparison")
plt.legend()
plt.grid(True)
plt.show()

for res in results:
    print(f"Розмір масиву: {res.get('Size')}")
    print(f"   Рандомізований QuickSort: {res.get('Randomized Average Time'):.4f} секунд")
    print(f"   Детермінований QuickSort: {res.get('Deterministic Average Time'):.4f} секунд\n")
