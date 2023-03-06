import math
from statistics import median, mean

# Ask user to enter 10 float numbers separated by a comma and split to create a list
numbers = input("Please enter ten float numbers separated by a comma: ").split(",")

# Cast to a float list
num_list = list(map(float, numbers))

# Calculate and print the sum of the numbers
sum_num_list = math.fsum(num_list)
print(sum_num_list)

# Find the largest number, find it's index and print it
max_value = max(num_list)
index = num_list.index(max_value)
print(index)

# Find the smallest number, find it's index and print it
min_value = min(num_list)
index = num_list.index(min_value)
print(index)

# Calculate the average of the numbers, print this rounding to 2 decimal points
average = mean(num_list)
print(round(average, 2))

# Calculate the median number and print
median_value = median(num_list)
print(median_value)
