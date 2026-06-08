# Program to find maximum and minimum in a list

a = [12, 7, 18, 5, 20, 9]

# Find maximum
maximum = a[0]

for x in a:
    if x > maximum:
        maximum = x

print("Maximum number =", maximum)

# Find minimum
minimum = a[0]

for x in a:
    if x < minimum:
        minimum = x

print("Minimum number =", minimum)
