#task 3:
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Sum of cells - {self.quantity + other}'

    def __sub__(self, other):
        if (self.quantity - other) > 0:
            return f'Cell difference - {self.quantity - other}'
        else:
            print(f'Cell disappeared')

    def __mul__(self, other):
        return f'Cell addition - {self.quantity * other}'

    def __truediv__(self, other):
        return f'Cell division- {self.quantity // other}'

    def make_order(self, quantity_in_row):
        count =''
        for i in range(self.quantity//quantity_in_row):
            count += "*" * quantity_in_row + '\n'
        count += "*" * (self.quantity%quantity_in_row) + '\n'
        return count

cell = Cell(20)
print(cell.make_order(10))
print(cell + 15)
print(cell - 15)
print(cell * 10)
print(cell / 15)