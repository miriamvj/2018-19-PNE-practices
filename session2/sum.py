print('sum of the first 100 integer numbers')
original_sum = 0
number = 1
while number <= 100:
    original_sum += number
    number += 1
print(original_sum)

original_sum2 = 0
for i in range(100):
    original_sum2 = original_sum2 + i +1
print(original_sum2)