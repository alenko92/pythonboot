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

# Third: Use a list Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
mylist = [x for x in range(1, 50) if x%3 == 0]
print(mylist)

