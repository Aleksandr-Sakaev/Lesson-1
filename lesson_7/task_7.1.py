__author__:'Сакаев Александр Самигуллович'


# task 1:
class Matrix:
    def __init__(self,ls):
        self.ls = ls

    def __str__(self):
        return '\n'.join('\t'.join([str(elem)for elem in i]) for i in self.ls)

    def __add__(self, other):
        for i in range(len(self.ls)):
            for x in range(len(other.ls[i])):
                self.ls[i][x]=self.ls[i][x]+other.ls[i][x]
        return Matrix.__str__(self)

list_1 = Matrix([[1,1,1],[1,1,1],[1,1,1]])
list_2 = Matrix([[2,2,2],[2,2,2],[2,2,2]])
print(list_1.__add__(list_2))
