def rot13(text): 
    encrypted_text = '' 

    for char in text: 
        if char.isalpha(): 
            if char.islower():
                if ord(char) <= 109: 
                    encrypted_text += chr(ord(char) +13) 
                else: 
                    encrypted_text += chr(ord(char) - 13)
            else: 
                #the character is uppercase 
                if ord(char) <= 77:
                    encrypted_text += chr(ord(char) +13)
                else: 
                    encrypted_text += chr(ord(char) -13)
        else: 
            encrypted_text += char


assert rot13('Hello, world!') == 'Uryyb, jbeyq!'

assert rot13('Uryyb, jbeyq!') == 'Hello, world!'

assert rot13(rot13('Hello, world!')) == 'Hello, world!'

assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'

assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'



