# https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/monk-and-modulo-based-sorting/

def merge(output, A, B, mod):
    i = j = m = 0
    while i < len(A) and j < len(B):
        if A[i]%mod <= B[j]%mod:
            output[m] = A[i]; i+=1; m+=1
        else:
            output[m] = B[j]; j+=1; m+=1
    while i < len(A):
        output[m] = A[i]; i+=1; m+=1
    while j < len(B):
        output[m] = B[j]; j+=1; m+=1
    return output

def mergesort(arr, mod):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left, mod)
        mergesort(right, mod)
        return merge(arr, left, right, mod) #only last call will have meaningful return

inp = input().split(" ")
mod = int(inp[1])
arr = [int(x) for x in input().split(" ")]
outp = mergesort(arr, mod)
outp = str(outp).replace(",", "")
print(outp[1:len(outp)-1])