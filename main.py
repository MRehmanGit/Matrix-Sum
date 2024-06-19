# Initializing a 2D array with the given numbers
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]

# Initializing a variable to hold the total sum of all elements
total = 0

# Iterate through each row in the 2D array
for rows in numbers:
    # Iterate through each element in the current row
    for cols in rows:
        # Add the current element to the total sum
        total += cols

# Print the total sum of all elements in the 2D array
print("Sum of 2D Array is :", total)
