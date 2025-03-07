##file = open('sample.txt', 'w')
##file.write('This is a line.')
##file.close()

with open('myfile.txt', 'w') as myFile:
    myFile.write('Line 1: This is a file' '\n')
    myFile.write('Line 2: I am writing this with Python' '\n')

#read() - returns the entire file
#read(length) - returns up to specified character length
#readline() - returns the next line
#readlines() = returns a list of lines 


with open('myfile.txt', 'r') as myFile:
    #print(myFile.read())
    #print(myFile.read(10)) #includes spaces as characters
    #print(myFile.readline())
    print(myFile.readlines()) #more like returns the rest of the lines in the document as a list
