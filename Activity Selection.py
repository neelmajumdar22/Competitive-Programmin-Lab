start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
print("Selected Activities:")
last = 0
count = 0
for i in range(6):
    if start[i] >= last:
        print("A", i + 1)
        last = finish[i]
        count += 1
print("Maximum Activities:", count)
