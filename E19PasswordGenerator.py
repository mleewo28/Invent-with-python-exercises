import random 

#set constants 
LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBER = '1234567890'
SPECIAL = '~!@#$%^&*()_+'

def generatePassword(length):
    if length < 12: 
        length = 12 

        password = []
        password.append(LOWERCASE[random.randint(0,25)]) 

        for 

        return password 
    
print(generatePassword(12))



