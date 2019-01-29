def fib(n):
    a, b = 0 , 1
    while a < n:
        print(a, end=',')
        a,b = b, a+b
    return()
m = int(input('Please, introuce a valid integer number:'))
fib(m)


#def sum_fibonacci():
    #sum = 0
    #for element in fib(n):
      #  sum = sum + 1
    #return sum
#print(sum)

sum = 0
for i in range(1, m):
    sum=sum+i
print('\n',sum)
