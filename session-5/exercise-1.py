def count_letter(sequence, lett):
    count_let = sequence.count(lett)
    return count_let

def count_bases(seq):
    dictionary = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    count_a = count_letter(seq, 'A')
    dictionary['A'] = count_a
    count_t = count_letter(seq, 'T')
    dictionary['T'] = count_t
    count_g = count_letter(seq, 'G')
    dictionary['G'] = count_g
    count_c = count_letter(seq, 'C')
    dictionary['C'] = count_c
    return dictionary

def percentage(seq):
    tl = len(seq)
    list_percentage = list()
    if tl > 0:
        perc_a = round(100.0 * count_bases(seq)['A'] / tl, 1)
        list_percentage.append(perc_a)
        perc_t = round(100.0 * count_bases(seq)['T'] / tl, 1)
        list_percentage.append(perc_t)
        perc_g = round(100.0 * count_bases(seq)['G'] / tl, 1)
        list_percentage.append(perc_g)
        perc_c = round(100.0 * count_bases(seq)['C'] / tl, 1)
        list_percentage.append(perc_c)
    else:
        perc_0 = 0
        list_percentage.append(perc_0)
    return list_percentage




seq = input('Enter the sequence:')
percentag = percentage(seq)


print('This sequence is',len(seq),'in length.')
print('Base A')
print('Counter:', count_letter(seq, 'A'))
print('Percentage:', percentag[0])
print('Base T')
print('Counter:', count_letter(seq, 'T'))
print('Percentage:', percentag[1])
print('Base G')
print('Counter:', count_letter(seq, 'G'))
print('Percentage:', percentag[2])
print('Base C')
print('Counter:', count_letter(seq, 'C'))
print('Percentage:', percentag[3])

