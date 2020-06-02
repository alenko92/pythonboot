# PIG LATIN
# If a word starts with a  vowel, add 'ay' to the end
# If a word doesn't start with a vowel, put the first letter at the end and add 'ay'
# eg. word --> ordway
# eg. apple --> appleway

def piglatin(aword = 'n/a'):
    '''
    DOCSTRING:  This function returns the inputed string + 'ay' at the end if it begins with a vowel, 
                and puts the first letter at the end and then adds 'ay'
    INPUT: a string
    OUTPUT: string + ay
    '''
    if (aword[0] == 'a' or aword[0] == 'e' or aword[0] == 'i' or aword[0] == 'o' or aword[0] =='u'):
        return aword + 'ay'
    else:
        return aword[1:] + aword[0] +'ay'


print(piglatin('word'))
print(piglatin('apple'))
