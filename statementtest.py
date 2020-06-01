# Statements Assessment Test

# First: Use for, .split() and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
splitted = st.split(' ')
for _ in splitted:
    if 's' in _[0] and len(_) > 2:
        print(_)

