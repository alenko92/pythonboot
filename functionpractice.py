# WARMUP

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
    

# LEVEL 1

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


# LEVEL 2

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
    marker = 'add'
    stack = []
    for i in arr:
        if int(i) == 6:
            marker = 'remove'
        if marker == 'add':
            stack.append(i)
            sumof += i
        if int(i) == 9:
            marker = 'add'
    return sumof

# CHALLENGING

def spy_game(nums):
    '''
    DOCSTRING:  This function returns True if a list of integers contains 007 in order
    INPUT: List of integers
    OUTPUT: 'True' or 'False'
    '''
    bond = []
    for i in nums:
        if int(i) == 0:
            bond.append(i)
        if 0 in bond and int(i) == 7:
            bond.append(i)
    print(bond)
    return bond == [0, 0, 7]

def count_primes(num):
    '''
    DOCSTRING:  This function returns the number of prime numbers that exist up to and including a given int
    INPUT: Integer
    OUTPUT: Count of prime numbers
    '''
    count = 2   # Taking into account that by convention 0 and 1 are not prime and 2 and 3 are already prime
    for i in range(5, num + 1):
        for n in range(2, i):
            if (i % n) == 0:
                break
        else: 
            count += 1
    return count


def print_big(letter):
    '''
    DOCSTRING:  This function returns a 5 x 5 representation of a letter that has been inputed
    INPUT: A character such as 'a'
    OUTPUT: 5 x 5 representation of of the letter such as:    *
                                                            *   *
                                                            *****
                                                            *   *
                                                            *   *
    '''
    pattern_dictionary = {0: ' * * ', 1: '  *  ', 2: '*   *', 3: '**** ', 4: '*****', 5: '    *', 
                        6: '*    ', 7: ' *   ', 8: '   * ', 9: '*  **', 10: '*  * ', 11: '** **', 
                        12: '* * *', 13: '**  *'}
    alphabet = {'A': [1, 2, 4, 2, 2], 'B': [3, 2, 3, 2, 3], 'C': [4, 6, 6, 6, 4], 'D': [3, 2, 2, 2, 3], 
                'E': [4, 6, 4, 6, 4], 'F': [4, 6, 3, 6, 6], 'G': [4, 6, 9, 2, 4], 'H': [2, 2, 4, 2, 2], 
                'I': [4, 1, 1, 1, 4], 'J': [4, 8, 8, 10, 3], 'K': [2, 10, 6, 10, 2], 'L': [6, 6, 6, 6, 4],
                'M': [2, 11, 12, 2, 2], 'N': [2, 13, 12, 9, 2], 'O': [4, 2, 2, 2, 4], 'P': [4, 2, 4, 6, 6], 
                'Q': [4, 2, 12, 9, 4], 'R': [4, 2, 12, 10, 2], 'S': [4, 6, 4, 5, 4], 'T': [4, 1, 1, 1, 1], 
                'U': [2, 2, 2, 2, 4], 'V': [2, 2, 2, 0, 1], 'W': [2, 2, 12, 0, 0], 'X': [2, 0, 1, 0, 2], 
                'Y': [2, 2, 4, 5, 4], 'Z': [4, 8, 1, 7, 4]}
    for i in alphabet[letter.upper()]:
        print(pattern_dictionary[i])
    return ''

def myfunc(string):
    '''
    DOCSTRING:  This function returns a string with its odd indexes value in lowercase and even 
                indexes value in uppercase
    INPUT: 'String'
    OUTPUT: 'sTrInG'
    '''
    allcaps = ''
    for i in range(len(string)):
        if i % 2 == 0:
            allcaps += (string[i].lower())
        else:
            allcaps += (string[i].upper())
    return allcaps


