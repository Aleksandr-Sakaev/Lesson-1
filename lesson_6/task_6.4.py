# task 4:
class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f'The {self.name} went'

    def stop(self):
        return f'The {self.name} has stopped'

    def turn(self, direction):
        return f'The {self.name} ternad {direction}'
    def show_speed(self):
        return f'Your speed is {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Your speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is correct'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Your speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is correct'

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

town_car = TownCar('Honda', 'Blue', 65, False)
print(town_car.show_speed())
town_car.stop()

work_car = WorkCar('Toyota', 'yellow', 50, False)
print(work_car.go(), work_car.turn('left'), work_car.show_speed(), work_car.stop())

sport_car = SportCar('Nissan GTS', 'white', 180, True)
print(sport_car.go(), sport_car.turn('right'), sport_car.turn('left'), sport_car.show_speed(), sport_car.stop())

police_car = PoliceCar('Dodge', 'black', 80, True)
print(police_car.go(), police_car.turn('right'), police_car.show_speed(), police_car.stop())