def count_letter(sequence, lett):
    count_let = sequence.count(lett)
    return count_let

from Bases import count_bases

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



list_seq = list()
seq1 = input('Enter the sequence  1:')
list_seq.append(seq1)
percentag1 = percentage(seq1)
seq2 = input('Enter the sequence 2:')
list_seq.append(seq2)
percentag2 = percentage(seq2)






print('Sequence 1 is',len(seq1),'in length.')
print('Base A')
print('Counter:', count_letter(list_seq[0], 'A'))
print('Percentage:', percentag1[0])
print('Base T')
print('Counter:', count_letter(list_seq[0], 'T'))
print('Percentage:', percentag1[1])
print('Base G')
print('Counter:', count_letter(list_seq[0], 'G'))
print('Percentage:', percentag1[2])
print('Base C')
print('Counter:', count_letter(list_seq[0], 'C'))
print('Percentage:', percentag1[3])
print(' ')


print('Sequence 2 is',len(seq2),'in length.')
print('Base A')
print('Counter:', count_letter(list_seq[1], 'A'))
print('Percentage:', percentag2[0])
print('Base T')
print('Counter:', count_letter(list_seq[1], 'T'))
print('Percentage:', percentag2[1])
print('Base G')
print('Counter:', count_letter(list_seq[1], 'G'))
print('Percentage:', percentag2[2])
print('Base C')
print('Counter:', count_letter(list_seq[1], 'C'))
print('Percentage:', percentag2[3])
