
# Example of reading a file located in our local filesystem
name = "mynotes.txt"

# open the file
myfile = open(name, 'r')

print("File opened: {}".format(myfile.name))

contents = myfile.read()

print('The file contents are: {}'.format(contents))

myfile.close()

f = open(name, 'a')
f.write('This is an example for adding to my file.')
f.close()
print('The end')
