arr1 = [3, 1, 5]
arr2 = [4, 2, 6]
merged = arr1 + arr2
for i in range(len(merged)):
    for j in range(i + 1, len(merged)):
        if merged[i] > merged[j]:
            merged[i], merged[j] = merged[j], merged[i]
print("Merged & Sorted Array:", merged)
