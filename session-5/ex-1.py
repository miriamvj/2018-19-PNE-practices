def count_a(seq):
    """Counting the number of A's in the sequence."""

    # Counter for the A's
    result = 0
    for b in seq:
        if b == 'A':
            result += 1
    # Return the result.
    return result

# Main program


s = input('Please, introduce a sequence:')
count_a(s)
na = count_a(s)
print('The number of As is:{}'.format(na))

# Calculate the total sequence length
tl = len(s)

# Calculate the  percentage of A's in the sequence
if tl>0:
    perc = round(100.0 * na/tl, 1)
else:
    perc = 0



print('The total length is:{}'.format(tl))
print('The percentage of As is {}%'.format(perc))
