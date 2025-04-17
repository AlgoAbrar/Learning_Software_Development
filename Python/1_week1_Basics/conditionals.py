# in, not, not in, is, is not 
# >, <, >=, <=, ==, !==
# and, or

a = 1
boss = False
if a > 5:
    print( 'Greater Than 5')
    print('My name is Abrar')
elif a > 3:
    print('Little bit greater than 3')
elif a == 2:
    print('Equal')
else:
    print('Mr. Bombastic')

if boss is not True:
    print('lunch er pore asen')
else: 
    print('come now')

coin = 'head'
# nested conditions
if boss == True:
    print('boss you are joss')
    if coin == 'tail':
        print('batting')
    else:
        print('bowling')
        if 5 > 2 or boss != True:
            print('do  something')
            if 8%2 == 0 and 5%2==1:
                print('even 8 is an even number')
else:
    print('you are loss not a boss')