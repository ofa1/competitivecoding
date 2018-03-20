# https://www.hackerearth.com/problem/algorithm/monk-being-monitor/
from collections import Counter
t = int(input())
for i in range(0,t):
    n = int(input())
    inp = input().split(" ")
    cnt = Counter()
    for j in inp:
        cnt[int(j)] += 1
    most = cnt.most_common()[0][0]
    mostcnt = cnt.most_common()[0][1]
    least = cnt.most_common()[len(cnt)-1][0]
    leastcnt = cnt.most_common()[len(cnt)-1][1]
    diff = mostcnt - leastcnt
    if (mostcnt - leastcnt) > 0:
        print(diff)
    elif n == 1:
        print("-1")
    else:
        print ("1")
    cnt.clear()