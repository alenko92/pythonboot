# PIG LATIN
# If a word starts witha  vowel, add 'ay' to the end
# If a word doesn't start with a vowel, put the first letter at the end and add 'ay'
# eg. word --> ordway
# eg. apple --> appleway

def piglatin(aword = 'n/a'):
    if (aword[0] == 'a' or aword[0] == 'e' or aword[0] == 'i' or aword[0] == 'o' or aword[0] =='u'):
        return aword + 'ay'
    else:
        return aword[1:] + aword[0] +'ay'


print(piglatin('word'))
print(piglatin('apple'))