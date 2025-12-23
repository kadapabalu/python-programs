arr=[1,2,3,4]
is_sorted=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        is_sorted=False
        break
print("Sorted" if is_sorted else "Not sorted")
