def add(x, y):
    return x + y


print(add(2, 4))


def multiply(x, y):
    result = 0
    for i in range(x):
        result = add(result, y)
    return result


print(multiply(6, 8))


def power(x, n):
    result = 1
    for i in range(n):
        result = multiply(result, x)
    return result


print(power(3, 4))


def factorial(x):
    result = 1
    for i in range(x):
        result = multiply(result, add(i, 1))
    return result


print(factorial(4))


def fibonacci(n):
    sequence = [0, 1]
    for i in range(add(n, -2)):
        sequence.append(add(sequence[-1], sequence[-2]))
    return sequence[-1]


print(fibonacci(8))
