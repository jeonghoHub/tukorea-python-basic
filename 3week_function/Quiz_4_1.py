def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def factorial(n):
    result = 1
    for i in range(n):
        result = result * (n - i)
    return result


print(sum(10))
print(factorial(3))


