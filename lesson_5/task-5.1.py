__author__:'Сакаев Александр Самигуллович'
#task 1:
my_file = open('111.txt', 'w')
x = input('Enter string \n')
while True:
    my_file.writelines(x)
    x = input('Enter string \n')
    if x == '':
        break

my_file.close()