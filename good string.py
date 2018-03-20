# https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/little-monk-and-good-string/
good = {
    "a":"a",
    "e":'e',
    'i':'i',
    'o':'o',
    'u':'u'
}
s = input()
goodCount = 0
streak = 0
for c in s:
    if c in good:
        streak += 1
    else:
        goodCount = streak if streak > goodCount else goodCount
        streak = 0
goodCount = streak if streak > goodCount else goodCount
print (goodCount)
