# Warmup

def lesser_of_two_evens(a, b):
    '''
    DOCSTRING:  This function returns the greater even number
    INPUT: integers 'a' and 'b'
    OUTPUT: 'a' or 'b' or 'same number' if both numbers are equal
    '''
    if a == b:
        return 'same number'
    elif (a + b)%2 != 0:
        if a%2 == 0:
            return a
        else:
            return b
    else: 
        if a > b:
            return a
        else: 
            return b


def animal_crackers(text):
    '''
    DOCSTRING:  This function returns True if both words begin with the same letter
    INPUT: any two word string
    OUTPUT: 'True' or 'False'
    '''
    splitted = text.split(' ')
    if splitted[0][0] == splitted[1][0]:
        return True
    else: 
        return False


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))