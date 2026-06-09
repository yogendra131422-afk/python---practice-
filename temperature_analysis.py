temp_list = [30,32,28,35,31]

sum = 0

count = 0

for x in temp_list:
    sum = sum + x

print("sum =", sum)

average = sum / len(temp_list)

print("average =", average)

for x in temp_list:
    if x > average:
        count = count + 1

print("count =", count)
