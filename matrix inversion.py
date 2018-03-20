# https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/monk-and-inversions-arrays-strings/
T = int(input())
for t in range(0,T):
    N = int(input())
    arr = []
    counter = 0
    for n in range(0,N):
        arr.append([int(x) for x in input().split(" ")])
    for i in range(0,N):
        for j in range(0,N):
            for m in range(i, N):
                for n in range(j, N):
                    if arr[i][j] > arr[m][n]:
                        counter += 1
    print (counter)
                
