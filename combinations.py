def comb(n, k):
    if k < 0 or k > n:
        return 0

    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result

print(comb(10,3))