arr = [[1,-2,3],[0,4,-5],[6,0,-7]]
positive = negative = zero = 0
for row in arr:
    for x in row:
        if x > 0: positive += 1
        elif x < 0: negative += 1
        else: zero += 1
print("Positive:", positive, "Negative:", negative, "Zero:", zero)
