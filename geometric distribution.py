def geodist(n, p):
    return pow((1-p), (n-1)) * p
def cumulate(start, end, p):
    cum = 0.0
    for r in range(start, end+1):
        cum += geodist(r, p)
    return cum
print('{:.3f}'.format(cumulate(0, 5, 1/3)))