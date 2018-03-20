# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-rotation-3/
T = int(input())
for t in range(0,T):
    ip = input().split(" ")
    N = int(ip[0])
    K = int(ip[1])
    arr = [int(x) for x in input().split(" ")]
    if K > N: K = K%N
    rotated = arr[(N-K):] + arr[:(N-K)]
    for e in rotated:
        print(e, end=' ')
    print()