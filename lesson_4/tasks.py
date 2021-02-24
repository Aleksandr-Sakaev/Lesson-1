__author__: 'Сакаев Александр Самигуллович'

# task 1:
from sys import argv


def salary(pay_rate, time_worked, bonus):
    wage = (pay_rate * time_worked) + bonus
    print(wage)


tasks, a, b, c = argv

salary(float(a), float(b), float(c))

# task 2:
a = list(map(int, input('Enter numbers: ').split()))
result = [numbers for i, numbers in enumerate(a) if i > 0 and a[i] > a[i - 1]]
print(result)

# task 3:
result = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
print(result)

# task 4:
a = list(input('Enter numbers: ').split())
result = [i for i in a if a.count(i) == 1]
print(result)

# task 5:
from functools import reduce


def funk(a, b):
    return a * b


result = [i for i in range(99, 1001) if i % 2 == 0]
print(reduce(funk, result))

# task 6:
from itertools import count

for element in count(3):
    if element > 10:
        break
    else:
        print(element)

from itertools import cycle

l = ['a', 'b', 'c', 'd']
x = 0
for i in cycle(l):
    x += 1
    if x > 10:
        break
    else:
        print(i)


# task 7:
def fact(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
        yield x


n = int(input('Enter number: '))
for i in fact(n):
    print(i)
