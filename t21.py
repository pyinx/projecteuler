def sumpd(n):
    """Return the d(n)"""
    return sum([x for x in range(1, n) if n % x == 0])
orgamilist = [x for x in range(1, 10001) if sumpd(sumpd(x)) == x]
amilist = [x for x in orgamilist if sumpd(x) != x]
print sum(amilist)
