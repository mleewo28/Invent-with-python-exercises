
def writeToFile(filename, text): 
    #open the file in write mode using open function 
    with open(filename,'w') as fileObj:
        #write text to the file 
        fileObj.write(text)

def appendToFile(filename, text):
    #open file to append 
    with open (filename, 'a') as fileObj:
        #write text to the end of the file 
        fileObj.write(text)

def readFromFile(filename): 
    #open the file in read mode 
    with open(filename) as fileObj:
        #Read all of the text in the file and return as single string 
        return fileObj.read() 
    
writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'