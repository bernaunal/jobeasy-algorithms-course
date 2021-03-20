def ZNH_rec(n):
    if n == 0:
        return 0
    if n % 10 == 0:
        return ZNH_rec(n // 10)
    return n


print(ZNH_rec(80000))