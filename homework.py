
numbers = [1, -2, 3, -4, 0, 6, 337, -108, 49, 0]
for i in numbers:                                      #1
    if i % 2 == 0:
        print(i, end = '  ' )



for i in numbers:
    if i > numbers[8]:                                 #2
        print('\n максимальне число:', i )
