def count(filename):
    with open (filename, 'r') as f:
        acounter = 0
        gcounter = 0
        tcounter = 0
        ccounter = 0
        for line in f:
            if '>' in line:
                line = line.replace(line, ' ')
            else:
                for elem in line:
                    if elem == 'A':
                        acounter += 1
                    elif elem == 'C':
                        ccounter += 1
                    elif elem == 'T':
                        tcounter += 1
                    elif elem == 'G':
                        gcounter += 1
    return acounter, gcounter, tcounter, ccounter
print('The order for the counting is: A, G, T, C:',count('CPLX2.TXT'))


