def prints(file):
    archivo = open(file, 'r')
    dear = archivo.read()
    archivo.close()
    return dear
archive = 'CPLX2.TXT'
print (prints(archive))