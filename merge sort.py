# merge sort

def merge(output, A, B):
    i = j = m = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            output[m] = A[i]; i+=1; m+=1
        else:
            output[m] = B[j]; j+=1; m+=1
    while i < len(A):
        output[m] = A[i]; i+=1; m+=1
    while j < len(B):
        output[m] = B[j]; j+=1; m+=1
    return output

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        return merge(arr, left, right) #only last call will have meaningful return

print (mergesort([14, 23, 22, 1, 7, 8, 10, 2, 3, 4]))
print (mergesort(['z','x','y','b','c','a'])) #just because Python <3