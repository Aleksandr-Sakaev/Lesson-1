# task 2:
my_file = open('222.txt', 'r')
text = my_file.read()
print(f'Enter text: \n {text}')

lines = 0
words = 0
symbols = 0

for i in open('222.txt', 'r'):
    lines += 1
    words += len(i.split())
    symbols += len(i)
print()
print(f'Number of lines in the text: {lines}')
print(f'Number of words in the text: {words}')
print(f'Number of symbols in the text: {symbols}')
my_file.close()
