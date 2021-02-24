# task 3:
class Example(Exception):
    def __init__(self, *args):
        self.my_list = []

    def func_str(self, my_list):
        for el in self.my_list:
            if type(el) == '3':
                print('The list contains the type "string"')
                my_list.pop(el)

    def div(self, my_list):
        while True:
            try:
                value = input('Enter number, for exit "q": ')
                if value == 'q':
                    break
                if not value.isdigit():
                    raise Example(value)
                my_list.append(int(value))
            except Example as ex:
                print('String!', ex)


my_list = [1, 2, '3']
print("List: ", my_list, "\n")
e = Example()
e.func_str(my_list)
e.div(my_list)
print("New list: ", my_list, "\n")