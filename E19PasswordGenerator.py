import random 

#set constants 
LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBER = '1234567890'
SPECIAL = '~!@#$%^&*()_+'
CHARS = LOWERCASE+UPPERCASE+NUMBER+SPECIAL 

def generatePassword(length):
    if length < 12: 
        length = 12 

    password = []
    password.append(LOWERCASE[random.randint(0,25)]) 
    password.append(UPPERCASE[random.randint(0,25)])
    password.append(NUMBER[random.randint(0,9)])
    password.append(SPECIAL[random.randint(0,12)])

    for i in range(length -4): 
        password.append(CHARS[random.randint(0,74)])

    random.shuffle(password)

    return ''.join(password)
    

assert len(generatePassword(8)) == 12

 

pw = generatePassword(14)

assert len(pw) == 14

hasLowercase = False

hasUppercase = False

hasNumber = False

hasSpecial = False

for character in pw:

    if character in LOWERCASE:

        hasLowercase = True

    if character in UPPERCASE:

        hasUppercase = True

    if character in NUMBER:

        hasNumber = True

    if character in SPECIAL:

        hasSpecial = True

assert hasLowercase and hasUppercase and hasNumber and hasSpecial

