# task 5:
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Starting rendering'


class Pen(Stationery):
    def draw(self):
        return f'Starting rendering {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Starting rendering {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Starting rendering {self.title}'


b = Pen('with a pen')
print(b.draw())

c = Pencil('with a pencil')
print(c.draw())

d = Handle('with a handle')
print(d.draw())
