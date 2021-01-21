__author__: 'Сакаев Александр Самигуллович'
# task 1:

if __name__=="__main__":
    def func(*args):
        z = 1
        for i in args:
            z /= i
        print(z)
    func(5, 1)
