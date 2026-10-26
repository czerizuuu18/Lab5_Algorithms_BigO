# Exercise 3 - E-Commerce Order Processing

import random
import time

LAST_NAME = "Bautista"
STUDENT_ID = "TUPM-26-1271"
SEED_DIGIT = 1
ID_SUM = 19

FAVORITE_ARTIST = input("enter your favorite artist:")

NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)

# Generate the original set of orders
ORDER_COUNT = 20

random.seed(ID_SUM + ARTIST_LENGTH)

orders = []

for i in range(ORDER_COUNT):
    order_id = random.randint(1000, 9999)
    orders.append(order_id)

# Create the three required input arrangements
sorted_orders = sorted(orders)
reverse_orders = sorted(orders, reverse=True)

random_orders = orders.copy()
random.shuffle(random_orders)

print("\n---E-COMMERCE ORDER DATA ---")
print("Original Orders:", orders)
print("Sorted Orders:", reverse_orders)
print("Reverse-Sorted Orders:", reverse_orders)
print("Random Orders:", random_orders)

# --------------------
# SELECTION SORT
# --------------------

def selection_sort(data):
    arr = data.copy()
    comparisons = 0 
    movements = 0

    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            comparisons += 1

            if arr[j] < arr[minimum]:
                minimum = j

        if minimum != i:
            arr[i], arr[minimum] = arr[minimum], arr[i]
            movements += 1

    return arr, comparisons, movements

# --------------------
# BUBBLE SORT
# --------------------

def bubble_sort(data):
    arr = data.copy()
    comparisons = 0
    movements = 0

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                movements += 1

    return arr, comparisons, movements


def test_sorting_algorithm(name, sorting_function, data):
    start_time = time.perf_counter()
    sorted_data, comparisons, movements = sorting_function(data)
    elapsed_time = time.perf_counter() - start_time

    print(name)
    print("Sorted output:", sorted_data)
    print("Comparisons:", comparisons)
    print("Movements:", movements)
    print("Execution time:", elapsed_time, "seconds")

# --------------------
# INSERTION SORT
# --------------------

def insertion_sort(data):
    arr = data.copy()
    comparisons = 0
    movements = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                movements += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    return arr, comparisons, movements

# --------------------
# RUN ALL TESTS
# --------------------

datasets = {
    "Sorted": sorted_orders,
    "Reverse-Sorted": reverse_orders,
    "Randon": random_orders
}

for dataset_name, dataset in datasets.items():

    print("\n==============================")
    print(dataset_name, "INPUT")
    print("==============================")

    test_sorting_algorithm(
        "Bubble Sort",
        bubble_sort,
        dataset
    )

    test_sorting_algorithm(
        "Selection Sort",
        selection_sort,
        dataset
    )

    test_sorting_algorithm(
        "Insertion sORT",
        insertion_sort,
        dataset
    )