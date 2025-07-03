def findAndReplace(text, oldText, newText): 
    replacedText = ''
    #Account for oldText being empty string 
    if oldText == '': 
        return text 

    #write code that copies code from text parameter to replacedText variable
    i = 0 
    while i < len(text): 
        #Note, you must strictly use '<' because the indexing is from [0:len(text) - 1]
        #when instance of old text has not been found only append current index 
        if text[i:i +len(oldText)] != oldText: 
            replacedText += text[i] 
            i += 1 
        else: 
            replacedText += newText 
            i += len(oldText)

    return replacedText 

assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'

assert findAndReplace('fox', 'fox', 'dog') == 'dog'

assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'

assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'

assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'