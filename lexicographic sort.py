# https://www.hackerearth.com/problem/algorithm/monk-and-suffix-sort/

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

inp = input().split(" ")
k = int(inp[1])
inp = inp[0]
arr = []
for i in range(len(inp),0, -1):
    arr.append(inp[i-1:])
print (mergesort(arr)[k-1])