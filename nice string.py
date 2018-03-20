# nice strings

n = int(input())
inputs = []
for i in range(0,n):
    inp = input()
    counter = 0
    for j in inputs:
        if j < inp:
            counter += 1
    inputs.append(inp)
    print (counter)

