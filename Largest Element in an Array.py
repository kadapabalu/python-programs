arr = [10, 20, 5, 8, 25, 15]
largest = second = float('-inf')
for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second Largest:", second)
