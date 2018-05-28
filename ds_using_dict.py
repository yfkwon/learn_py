# coding = utf8 ~

# 'ab' is short for 'a'ddress'b'ook

ab = { 'Swroop' : 'swroop@swroopch.com',
       'Larry'  : 'larry@wall.org',
       'Matsumto' : 'matz@ruby-lang.org',
       'Spammer' : 'spammer@hotmail.com'
    }

# Deleting a key-value pair
del ab['Spammer']

print '\nThere are {} contacts in the address-book\n'.format(len(ab))

for name, address in ab.items():
    print 'Contact {} at {}'.format(name, address)

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print "\nGuido's address is", ab['Guido']
