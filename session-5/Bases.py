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