def fib(n):
    a, b = 0 , 1
    while a < n:
        print(a, end=',')
        a,b = b, a+b
    return()
m = int(input('Please, introuce a valid integer number:'))
fib(m)