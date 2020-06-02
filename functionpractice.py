# Warmup

def lesser_of_two_evens(a, b):
    if (a + b)%2 != 0:
        if a%2 == 0:
            return a
        else:
            return b
    else: 
        if a > b:
            return a
        else: 
            return b

print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))
