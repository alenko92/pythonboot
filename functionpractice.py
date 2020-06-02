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


def master_yoda(text):
    '''
    DOCSTRING:  This function returns a sentece with the words reversed
    INPUT: string 'I am home'
    OUTPUT: string 'home am I'
    '''
    newsentence = []
    for _ in text.split(' ')[::-1]:
        newsentence.append(_)
    return newsentence


def almost_there(n):
    '''
    DOCSTRING:  This function returns True if n is within 10 of either 100 or 200
    INPUT: integer 'n'
    OUTPUT: 'True' or 'False'
    '''
    res = 100 - n
    res2 = 200 - n
    if abs(res) < 11 or abs(res2) < 11:
        return True
    else:
        return False


# Level2

def has_33(nums):
    '''
    DOCSTRING:  This function returns True if the array contains a 3 next to a 3 somewhere
    INPUT: array of numbers
    OUTPUT: 'True' or 'False'
    '''
    for n in range(len(nums) -1):
        if(nums[n] == nums[n+1]):
            return True
    return False


def paper_doll(text):
    '''
    DOCSTRING:  This function returns a string where for every character in the original there are three characters
    INPUT: string 'hello'
    OUTPUT: string 'hhheeellllllooo'
    '''
    newtext = ''
    for i in text:
        newtext += i*3
    return newtext


def blackjack(a, b, c):
    '''
    DOCSTRING:  This function returns the sum of the three integers given if its less or equal than 21, but if
                it exceeds 21 and there is an 11, returns the total sum minus 10. If the sum exceeds 21, the 
                function should return 'BUST'
    INPUT: Three integers 'a', 'b' and 'c'
    OUTPUT: Sum of the three integers or 'BUST'
    '''
    result = a + b + c
    if result > 21:
        if a == 11 or b == 11 or c == 11:
            return result - 10
        else: 
            return 'BUST'
    return result
    

def summer_69(arr):
    '''
    DOCSTRING:  This function returns the sum of the numbers in the array, except ignoring sections of 
                the array that are between a 6 and a 9
    INPUT: Array of numbers
    OUTPUT: Sum of the array
    '''
    sumof = 0
    stack = []
    for i in arr:
        stack.append(i)
        print(stack)
        sumof += i
    return sumof

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
