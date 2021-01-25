
def factorial_recursive(n):
    if n <= 1:
        print('*', 1)
        return 1
    print('*', n)
    return n * factorial_recursive(n - 1)


print(factorial_recursive(5))
