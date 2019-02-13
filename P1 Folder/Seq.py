class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        new = ''
        for letter in self.strbases:
            letter = letter.upper()

            if letter == 'A':
                new += 'T'
            elif letter == 'T':
                new += 'A'
            elif letter == 'G':
                new += 'C'
            else:
                new += 'G'
        return new

    def reverse(self):
        new = ''
        for letter in self.strbases:
            letter = letter.upper()

            if letter == 'A':
                new += 'T'
            elif letter == 'T':
                new += 'A'
            elif letter == 'G':
                new += 'C'
            else:
                new += 'G'
        return new[::-1]

    def count(self):
        acounter = 0
        gcounter = 0
        tcounter = 0
        ccounter = 0
        for elem in self.strbases:
            if elem == 'A':
                acounter += 1
            elif elem == 'C':
                ccounter += 1
            elif elem == 'T':
                tcounter += 1
            elif elem == 'G':
                gcounter += 1
        return acounter, tcounter, gcounter, ccounter

    def percentage(self):
        sequence = self.strbases
        tl = len(sequence)
        list_percentage = list()
        if tl > 0:
            perc_a = round(100.0 * sequence.count('A') / tl, 1)
            list_percentage.append(perc_a)
            perc_t = round(100.0 * sequence.count('T') / tl, 1)
            list_percentage.append(perc_t)
            perc_g = round(100.0 * sequence.count('G') / tl, 1)
            list_percentage.append(perc_g)
            perc_c = round(100.0 * sequence.count('C') / tl, 1)
            list_percentage.append(perc_c)
        else:
            perc_0 = 0
            list_percentage.append(perc_0)
        return list_percentage


