from Seq import Seq
s1 = Seq(input('Introduce a first valid sequence:'))
s2 = Seq(input('Introduce a second valid sequence:'))
s3 = Seq(s1.complement())
s4 = Seq(s3.reverse())

print('Sequence 1:',s1.strbases,'\nLength:', len(s1.strbases), '\nBases count in order A, C, T, G:',s1.count(),'\nBases percentage in order A, C, G, T:', s1.percentage())
print('Sequence 2:',s2.strbases,'\nLength:', len(s2.strbases), '\nBases count in order A, C, T, G:',s2.count(),'\nBases percentage in order A, C, G, T:', s2.percentage())
print('Sequence 3:',s3.strbases,'\nLength:', len(s3.strbases), '\nBases count in order A, C, T, G:',s3.count(),'\nBases percentage in order A, C, G, T:', s3.percentage())
print('Sequence 4:',s4.strbases,'\nLength:', len(s4.strbases), '\nBases count in order A, C, T, G:',s4.count(),'\nBases percentage in order A, C, G, T:', s4.percentage())

