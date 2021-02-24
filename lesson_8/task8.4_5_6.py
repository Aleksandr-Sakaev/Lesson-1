# task 4, 5, 6:
class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.name, []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, model, year, count):
        self.name = name
        self.model = model
        self.year = year
        self.count = count
        self.items = {'Name': self.name, 'Model': self.model, 'Year of production': self.year, 'Amount': self.count}

    def __str__(self):
        return f'{self.model}-{self.year}-{self.count}'

    def income(self):
        try:
            name = input(f'Enter name: ')
            model = input(f'Enter model: ')
            year = int(input(f'Enter year: '))
            count = int(input(f'Enter amount: '))
            item = {'Name ': name, 'Model': model, 'Year of production': year, 'Amount': count}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Error')


class Printer(Equipment):
    def __init__(self, name, model, year, count):
        super().__init__(name, model, year, count)

    def action(self):
        return 'Print'


class Scaner(Equipment):
    def __init__(self, name, model, year, count):
        super().__init__(name, model, year, count)

    def action(self):
        return 'Scan'


class Xerox(Equipment):
    def __init__(self, name, model, year, count):
        super().__init__(name, model, year, count)

    def action(self):
        return 'Copy'


sklad = Sklad()
scaner = Scaner('Scaner', 'hp 1040', 2019, 1)
sklad.add_to(scaner)
scaner = Scaner('Scaner', 'hp 1041', 2020, 1)
sklad.add_to(scaner)
scaner = Scaner('Scaner', 'hp 1042', 2021, 2)
sklad.add_to(scaner)
printer = Printer('Scaner', 'brother 3', 2018, 3)
sklad.add_to(printer)

print(sklad._dict)

sklad.extract('Scaner')
print()
print(sklad._dict)

Equipment.income(scaner)
