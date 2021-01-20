__author__: 'Сакаев Александр Самигуллович'
# task 1:

a = 'variable - a'
b = 'variable - b'
c, d = map(int, input('enter two numbers:').split())
y, z = map(str, input('enter two string: ').split())
print(a, ',', b, ',', c, ',', d, ',', y, ',', z)


# task 2:
time = int(input('enter second: '))
hour = ((time // 3600)) % 24
minute = (time // 60) % 60
second = time%60
print(hour, ':', minute, ':', second)


# task 3:
n = input('enter number: ')
x = n + n
y = n + n + n
print(int(n)+int(x)+int(y))


# task 4:
x = int(input('enter integer number: '))
ls = []
while x > 10:
    ls.append(x % 10)
    x //= 10
r = max(ls)
print(r)

# task 5:
revenue = float(input('inter revenue: '))
costs = float(input('enter costs: '))

if revenue > costs:
    ratio = revenue - costs
    print('Company has a profit. Profitability: ', ratio)
    count = int(input('enter number of employees: '))
    profit_workers = ratio / count
    print('Profit per employees: ', profit_workers)
elif revenue == costs:
    print('break-even point')
else:
    print('Company has losses')


# task 6:
a = int(input())
b = int(input())
days = 1
while a < b:
    a = a + (a * 0.1)
    days += 1
    print(days)
