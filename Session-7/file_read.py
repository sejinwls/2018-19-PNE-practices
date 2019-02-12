# Example of reading a file located
# in our local file system

name = "mynotes.txt"

# Open the file
myfile = open(name, 'r')

print("File opended: {}".format(myfile.name))

contents = myfile.read()

print("The file contents are :{}".format(contents))

myfile.close()

f = open(name, 'a')
f.write("This is a text example of adding to a file")
f.close()
print("The end")
