def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solution(a):
    res = a[0]
    for num in a[1:]:
        res = gcd(res, num)
    return res * len(a)