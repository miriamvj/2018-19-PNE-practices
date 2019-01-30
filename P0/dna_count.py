sequence = str(input('Introduce a sequence:'))
sequence = sequence.upper()
countera = 0
counterc = 0
counterg = 0
countert = 0
for letter in sequence:
    if letter == 'A':
        countera += 1
    elif letter =='C':
        counterc += 1
    elif letter == 'T':
        countert += 1
    elif letter == 'G':
        counterg += 1

print('a:',countera)
print('c:',counterg)
print('t:',countert)
print('c:',counterc)
