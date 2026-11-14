# Experiment 9: Statistical Measures

import numpy as np


def without_numpy(data):
    n = len(data)

    # Mean
    mean = sum(data) / n

    # Median
    sorted_data = sorted(data)

    if n % 2 == 0:
        median = (
            sorted_data[n // 2 - 1] +
            sorted_data[n // 2]
        ) / 2
    else:
        median = sorted_data[n // 2]

    # Standard Deviation
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5

    minimum = min(data)
    maximum = max(data)

    return mean, median, std_dev, minimum, maximum


def with_numpy(data):
    arr = np.array(data)

    mean = np.mean(arr)
    median = np.median(arr)
    std_dev = np.std(arr)
    minimum = np.min(arr)
    maximum = np.max(arr)

    return mean, median, std_dev, minimum, maximum


# Take input for all three datasets
marks = list(map(float, input(
    "Enter student marks separated by spaces: "
).split()))

temperatures = list(map(float, input(
    "Enter temperatures separated by spaces: "
).split()))

sales = list(map(float, input(
    "Enter sales values separated by spaces: "
).split()))


datasets = {
    "Student Marks": marks,
    "Temperatures": temperatures,
    "Sales": sales
}


for name, data in datasets.items():

    if len(data) == 0:
        print("\n", name, ": No data entered.")
        continue

    print("\n==========", name, "==========")

    # Without NumPy
    result1 = without_numpy(data)

    print("\nWithout NumPy")
    print("Mean:", result1[0])
    print("Median:", result1[1])
    print("Standard Deviation:", result1[2])
    print("Minimum:", result1[3])
    print("Maximum:", result1[4])

    # With NumPy
    result2 = with_numpy(data)

    print("\nWith NumPy")
    print("Mean:", result2[0])
    print("Median:", result2[1])
    print("Standard Deviation:", result2[2])
    print("Minimum:", result2[3])
    print("Maximum:", result2[4])