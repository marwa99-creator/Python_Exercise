# def comb(n, k):
#     if k < 0 or k > n:
#         return 0

#     result = 1
#     for i in range(1, k + 1):
#         result = result * (n - i + 1) // i
#     return result

def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact(n) // (fact(k) * fact(n - k))

print(comb(10,3))