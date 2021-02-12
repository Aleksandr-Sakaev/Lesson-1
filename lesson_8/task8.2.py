# task 2:
class Example(Exception):

    def my_func(*args):
        try:
            arg_1 = int(input('Enter first number: '))
            arg_2 = int(input('Enter second number:'))
            if arg_2 == 0:
                raise Example('Error. Division by zero')
            else:
                result = arg_1 / arg_2
                return result

        except ValueError:
            return 'Value error'
        except Example as err:
            return err


x = Example()
print(x.my_func())
