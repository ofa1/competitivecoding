N = int(input())
A = [int(x) for x in input().split(" ")]
B = [int(x) for x in input().split(" ")]
for i in zip(A, B):
    print(sum(i), end=" ")