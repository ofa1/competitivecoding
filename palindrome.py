def isPalindrome(s):
    if len(s) == 1:
        return True
    else:
        a = s[:len(s)//2]
        b = reversed(s[len(s)//2:])
        for i in zip(a,b):
            if i[0] != i[1]:
                return False
        return True

N = int(input())
for i in range(0,N):
    x = input()
    if isPalindrome(x):
        print ("YES " + ("EVEN" if len(x) % 2 == 0 else "ODD"))
    else:
        print ("NO")

