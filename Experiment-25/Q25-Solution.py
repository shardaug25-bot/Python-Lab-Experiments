# Experiment 25: Monthly Sales Visualization

import matplotlib.pyplot as plt

# Months
months = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"
]

sales = []

# Take sales input
for month in months:
    amount = float(input(
        f"Enter sales for {month}: "
    ))
    sales.append(amount)


# Find highest and lowest sales
highest = max(sales)
lowest = min(sales)

highest_month = months[sales.index(highest)]
lowest_month = months[sales.index(lowest)]

print("\nHighest Sales:")
print("Month:", highest_month)
print("Amount:", highest)

print("\nLowest Sales:")
print("Month:", lowest_month)
print("Amount:", lowest)


# Line chart
plt.figure(figsize=(10, 5))

plt.plot(months, sales, marker="o")

plt.xlabel("Months")
plt.ylabel("Sales Revenue")
plt.title("Monthly Retail Sales - Line Chart")

plt.grid()
plt.show()


# Bar chart
plt.figure(figsize=(10, 5))

plt.bar(months, sales)

plt.xlabel("Months")
plt.ylabel("Sales Revenue")
plt.title("Monthly Retail Sales - Bar Chart")

plt.show()