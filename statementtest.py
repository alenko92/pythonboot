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
