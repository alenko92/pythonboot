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
    # Checks if word starts with a vowel
    if (aword[0] in 'aeiou'):
        return aword + 'ay'
    else:
        return aword[1:] + aword[0] +'ay'


print(piglatin('word'))
print(piglatin('apple'))
