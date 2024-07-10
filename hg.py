


'''a = 'vegetables are useful'
z = 0
b = input('enter letter\t')

for index in a:
    if index == b:
        z += 1
    else:
        print('error')
        break
print(z)'''
import random

'''b = "a"
a ="asd hasi gdukas dhasidh aukg sdukyasgd "
print(a)
for index in a:
    if index == b:
       a = a.replace("a", "b")

print(a)

'''


'''user = input('enter line\t')
a = 
I love
my dog
and my mum
'''


'''user = input('enter line\t')
sum = 0
for index in user:
    sum += 1
print(sum)
'''
'''import random
import string
user = int(input('введіть довжину\t'))
parol = ''
a = string.digits
b = string.punctuation
c = string.ascii_letters
abc = a + b + c
for i in range(0, user):
    rand = random.choice(abc)
    parol += rand

print(parol)
'''
'''
import random
import string

user = int(input('Задайте довжину пароля: \t'))

password = ''

stro = string.ascii_letters + string.digits + string.punctuation
for index in range(0, user):
    rand = random.choice(stro)
    password += rand
print(password)
'''
'''while True:
    user = input('введіть слово\t')
    b = (user[::-1])

    if user == b:
        print('є паліндромом')
    else:
        print('не є паліндромом')
'''

'''user = input('введіть рядок\t')
user_1 = input('введіть символ, який хочете замінити\t')
user_2 = input('введіть новий символ\t')
for i in user:
    a = user.replace(user_1, user_2)
print(a)

'''

'''user = str(input('введіть перший рядок\t'))
user_1 = input('введіть другий рядок\t')
if len(user.split()) < 2:
    print('ви ввели меньше двух слів')
else:
    b = user[6:11]
    c = user[0:5]
    bc = b + c
    print(bc)
if len(user_1.split()) < 2:
    print('ви ввели меньше двух слів')
else:
    print(user_1[::-1])

'''






'''user = input('enter elem\t')

my_list = ['name1', 'name2', 'name3']
print(my_list)

my_list[2] = user
print(my_list)

'''
'''my_list = ['hello1', 'hello', 'hello3', -3, 60, 0]
user = str(input('enter elem\t'))

for i in my_list:
    if user == i:
        print('ok')
        break'''

'''my_list = ['hello1', 'hello', 'hello3', -3, 60, 0]

user = str(input('enter elem\t'))

for index, elem in enumerate(my_list):
    if str(elem) == user:
        print(index)
'''
my_list = ['hello1', 'hello', 'hello3', -3, 60, 0]

for index, elem in enumerate(my_list):
    print(f'elem: {elem}, index: {index}')











