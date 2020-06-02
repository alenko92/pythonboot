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
    return splitted[0][0] == splitted[1][0]


def makes_twenty(n1, n2):
    '''
    DOCSTRING:  This function return True if the sum of the integers inputed or one of the integers
                is 20 and False if not
    INPUT: Two integers 'n1' and 'n2'
    OUTPUT: 'True' or 'False'a
    '''
    if n1 is 20 or n2 is 20:
        return True
    else: 
        return n1 + n2 is 20
    

# Level 1
def old_macdonald(name):
    '''
    DOCSTRING:  This function capitalizes the first and fourth letters of a name
    INPUT: string 'name'
    OUTPUT: string 'NamE'
    '''
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:]

print(old_macdonald('macdonald'))