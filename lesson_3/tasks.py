__author__: 'Сакаев Александр Самигуллович'
# task 1:
<<<<<<< HEAD

if __name__=="__main__":
    def func(*args):
        z = 1
        for i in args:
            z /= i
        print(z)
    func(5, 1)
=======
def func(*args):
    try:
        arg1 = int(input('enter number: '))
        arg2 = int(input('enter number: '))
        result = arg1 / arg2

    except ZeroDivisionError:
        return 'Error. Division by zero'
    except ValueError:
        return 'Value error'

    return result


print(func())


# task 2:
def my_func(**kwargs):
    print(kwargs)


my_func(name='Alex', surname='San', b_day='25.08.2000', city='New York', email='qwerty@gmail.com',
    telephone='+7809011111')


# task 3:
def my_func(a,b,c):
    lst = [a,b,c]
    lst.remove(min(a,b,c))
    return sum(lst)

print(my_func(2,5,3))


# task 4:
def my_func(x,y):
    z = x ** abs(y)
    return z
print(my_func(2,-3))

def my_func1(a,b):
    num = 1
    for i in range(abs(b)):
        num = num*a
    return num
print(my_func1(5,-4))


# task 5:
def my_func():
    sum_result = 0
    while True:
        valeu = input('enter number or q to exit: ').split()
        for i in valeu:
            try:
                if i == 'q' or i == 'Q':
                    print(f'sum is {sum_result}. Exit')
                else:
                    sum_result += int(i)
            except ValueError:
                print(f'enter number or q')
        print(f'sum is {sum_result}')
my_func()


# task 6:
string = input().split()
lst = []
for i in string:
    lst.append(i.capitalize())
print(' '.join(lst))
>>>>>>> origin/lesson-3
