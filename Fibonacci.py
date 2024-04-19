def fib(n):
    if n <= 1:
        return(1)
    else:
        nth = fib(n - 2) + fib(n - 1)
        return(nth)

n = int(input())
nth = fib(n)
print(nth)
