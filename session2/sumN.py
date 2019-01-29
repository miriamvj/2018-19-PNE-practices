def sumn(n):
    total = 0
    for i in range(n):
        total = total + i + 1
    return total

#Main program
num = int(input('Please introduce a n:'))
total_sum = sumn(num)
print('The total sum is {}'.format(total_sum))