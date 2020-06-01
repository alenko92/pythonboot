# Statements Assessment Test

# First: Use for, .split() and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
splitted = st.split(' ')
for _ in splitted:
    if 's' in _[0] and len(_) > 2:
        print(_)

# Second: Use range() to print all the even numbers from 0 to 10 
for _ in range(0, 10):
    if _%2 == 0:
        print(_)
'''Or '''
print(list(range(0, 11, 2)))

# Third: Use a list Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
mylist = [x for x in range(1, 50) if x%3 == 0]
print(mylist)

# Fourth: Go through the string below and if the length of a word is even print "even"
st = 'Print every word in this sentence that has an even number of letters'
splitted = st.split(' ')
for _ in splitted: 
    if len(_)% 2 == 0:
        print(_)

# Fifth: Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz"
#       instead of the number and for the multiples of five print "Buzz". For numbers which are multiples 
#       of both three and five print "FizzBuzz"
for _ in range(1, 100):
    if _ % 3 == 0 and _ % 5 == 0:
        print('FizzBuzz')
    elif _ % 3 == 0:
        print('Fizz')
    elif _ % 5 == 0:
        print('Buzz')
    else:
        print(_)

# Sixth: Use List Comprehension to create a list of the first letters of every word in the string below
st = 'Create a list of the first letters of eevery word in this string'
splitted = [x[0] for x in st.split(' ')] 
print(splitted)
