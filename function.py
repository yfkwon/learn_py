# coding = utf8 ~

def say_hello():
    # block belonging to the function
    print 'hello world'
# end of func


say_hello()
say_hello()


def print_max(a, b):
    if a > b:
        print a, 'is maxium'
    elif a == b:
        print a, 'is equl to ', b
    else:
        print b, 'is maximum'

print_max(3, 4)

x = 5
y = 7

print_max(x, y)




