# coding = utf8 ~

def print_max(x, y):
    '''Print the maxium of tow numbers.

    The two values must bo integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

print max(3, 5)
print print_max.__doc__
