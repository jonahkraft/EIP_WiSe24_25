# 1a

for i in range(1, 11):
    if i < 10:
        print(i)
    else:
        print('aus')
print()

# 1b

for i in range(1, 5):
    if i != 3:
        print(f'{i}, hier kommt die Sonne')
    else:
        print('3, sie ist der hellste Stern von allen')
print()

# 2

gifts = ['partridge in a pear tree', 'turtle doves', 'French hens', 'calling birds', 'gold rings', 'geese alaying',
         'swans a-swimming', 'maids a-milking', 'ladies dancing', 'lords a-leaping', 'pipers piping', 'drummers drumming']

for i in range(1, 13):
    print(f'On the {i}. day of Christmas my true love sent to me')

    if i == 1:
        print('A partridge in a pear tree.\n')

    if i != 1:
        for j in range(i-1, 0, -1):
            print(f'{j + 1} {gifts[j]},')
        print('And a partridge in a pear tree.\n')
