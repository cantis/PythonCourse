def factorial(n):
    #n! can also be defined as n * (n-1)!
    """ Calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(1000))
