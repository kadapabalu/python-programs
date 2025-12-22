def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = []
        right = []
        for x in arr[:-1]:
            if x <= pivot:
                left.append(x)
            else:
                right.append(x)
        return quick_sort(left) + [pivot] + quick_sort(right)
numbers = [33, 10, 55, 71, 29, 3, 18]
print("Original list:", numbers)
sorted_numbers = quick_sort(numbers)
print("Sorted list:", sorted_numbers)
