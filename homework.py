
numbers=[3,1,2,4,5]

my_list = []
my_list2 = []

for elem in numbers:
    if elem % 2 == 0:                                      #1
        my_list.append(elem)
    else:
        my_list2.append(elem)
main_list = my_list + my_list2
print(main_list)



numbers=[1,4,1,5,56,-5,7,4,78,-1,-5]
i = 0
for elem in numbers:                                        #2
    i += elem
print('сума всіх чисел\t', i)

numbers=[0,5,15,6,-5,9,-1,5,5]
number = []
number2 = []
for elem in numbers:
    if elem < 0:
        number = elem                                       #3
print('останній відємний елемент\t', number)
for elem in numbers:
    if elem > 0:
        number2 = elem
print('перший додатній елемент\t', number2)