# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def sortString(str):
    return ''.join(sorted(str))

test = 'what up'
print(sortString(test))