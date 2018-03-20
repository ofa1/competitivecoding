# Quick Sort
def swap(arr, a, b):
    temp = arr[a]
    arr[a] = b
    arr[b] = temp

def quicksort(arr, start, end):
    if start < end and (end - start) > 1:
        pivot = start
        # print ("start", start, "pivot", pivot, "end", end, "arr", arr[start:end])
        # swap(arr, start, pivot)
        ltr = start + 1
        rtl = end
        while ltr < rtl:
            while arr[start] > arr[ltr]:
                ltr += 1
            while arr[start] < arr[rtl]:
                rtl -= 1
            if ltr < rtl:
                swap(arr, ltr, rtl)
                ltr += 1
                rtl -= 1
        # swap(arr, start, rtl)
        quicksort(arr, start, pivot-1)
        quicksort(arr, pivot+1, end)

def sort(arr):
    quicksort(arr, 0, len(arr)-1)
    return arr
inp = [int(x) for x in input().split(' ')]
print(sort(inp))
            
