# fibonacci

def fib(n):
    if (n == 1 or n == 0):
        return n
    return fib(n-1)+fib(n-2)

assert fib(0) == 0
assert fib(1) == 1
assert fib(5) == 5
assert fib(6) == 8