class Seq:
    """A class for representing sequences"""
    def __init__(self, strbase):
        self.strbase = strbase

    def len(self):
        return len(self.strbase)

    def complement(self):
        new = ''
        for letter in self.strbase:
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
        for letter in self.strbase:
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

    def count(self, base):
        counting = (self.strbase.count(base))
        return counting

    def percentage(self,base):
        length = len(self.strbase)
        percentage = round(((self.strbase.count(base))/length)*100,1)
        return percentage


