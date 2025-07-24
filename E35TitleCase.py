def getTitleCase(text):

    if text == '':
        return ''

    title_case = ''
    title_case = text[0].upper() 

    for i in range(1,len(text)):
        if text[i-1].isalpha():
            title_case += text[i].lower() 

        else: 
            title_case+= text[i].upper() 

    return title_case




assert getTitleCase('Hello, world!') == 'Hello, World!'

assert getTitleCase('HELLO') == 'Hello'

assert getTitleCase('hello') == 'Hello'

assert getTitleCase('hElLo') == 'Hello'

assert getTitleCase('') == ''

assert getTitleCase('abc123xyz') == 'Abc123Xyz'

assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'

assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'

 

import random

random.seed(42)

chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')

for i in range(1000):

    random.shuffle(chars)

    assert getTitleCase(''.join(chars)) == ''.join(chars).title()


