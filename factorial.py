def factorial(num):
    if num > 1:
        return num * factorial(num-1)
    return 1

def ncr(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

def binomialDist(x, n, p):
    return ncr(n,x) * pow(p, x) * pow((1-p), (n-x))

def cumulativeDist(start, end, n, p):
    cumulative = 0.0
    for r in range(start,end+1):
        cumulative += binomialDist(r, n, p)
    if cumulative < 0: cumulative = cumulative * -1
    return cumulative

pDefect = 0.12
numberOfTrials = 10
print('{:.3f}'.format(cumulativeDist(0, 2, numberOfTrials, pDefect)))
print('{:.3f}'.format(cumulativeDist(2, numberOfTrials, numberOfTrials, pDefect)))