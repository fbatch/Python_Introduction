class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car started! ')

    def stop(self):
        print('Car stopped! ')

    def turn(self, direction):
        print(f'Car turned to the {direction}! ')

    def show_speed(self):
        print(f'Speed: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Speed: {self.speed}') if self.speed <= 60 else print('Вы превысили скорость! ')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Speed: {self.speed}') if self.speed <= 40 else print('Вы превысили скорость! ')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

# print('\nWorking with car:')
# car = Car(50, 'red', 'lada', False)
# car.go()
# car.turn('left')
# car.stop()
# car.show_speed()
#
# print('\nWorking with town_car:')
# town_car = TownCar(70, 'blue', 'Mercedes')
# town_car.show_speed()
# print(town_car.is_police)
# print(town_car.color)
# print(town_car.name)
#
# print('\nWorking with sport_car:')
# sport_car = SportCar(90, 'red', 'XXX')
# sport_car.show_speed()
# print(sport_car.is_police)
# print(sport_car.color)
# print(sport_car.name)
#
# print('\nWorking with work_car:')
# work_car = WorkCar(90, 'Orange', 'Kamaz')
# work_car.show_speed()
# work_car.turn('right')
# print(work_car.is_police)
# print(work_car.color)
# print(work_car.name)
