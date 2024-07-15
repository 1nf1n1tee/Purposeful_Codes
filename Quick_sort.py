def quick_div(arr):
    pivot = arr[-1]
    p = -1
    i = 0
    while i < len(arr):
        if arr[i] >= pivot:
            arr[i],arr[p] = arr[p],arr[i]
            p = i
        i += 1
    return arr

array = [7,9,1,0,6]
print(quick_div(array))

