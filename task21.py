def factorial(n):

    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_sequence(n):

    factorial_n = factorial(n)

    result_list = []

    for i in range(factorial_n, 0, -1):
        result_list.append(factorial(i))

    return result_list

print(factorial_sequence(3))