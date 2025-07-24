def reverseString(text): 
    #convert string to a list 
    text = list(text)

    for i in range (len(text)//2):
        text[i], text[len(text)-1 - i] = text[len(text)-1-i], text[i] 

    return ''.join(text)


assert reverseString('Hello') == 'olleH'

assert reverseString('') == ''

assert reverseString('aaazzz') == 'zzzaaa'

assert reverseString('xxxx') == 'xxxx'