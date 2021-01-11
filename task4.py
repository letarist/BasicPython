class Car:
    def __init__(self, speed, color, name, is_police):
        self.s = speed
        self.c = color
        self.n = name
        self.p = is_police

    def go(self):
        return f"{self.n} Go"

    def stop(self):
        return f"{self.n} STOP!"

    def turn_left(self):
        return f"{self.n} turned left"

    def turn_right(self):
        return f"{self.n} turned right"

    def show_speed(self):
        return f"{self.s} the current speed of the car"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.s > 60:
            return "overspeed"
        else:
            return f"{self.s} the current speed of the car"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.s > 40:
            return "overspeed"
        else:
            return f"{self.s} the current speed of the car"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


lamborgini = SportCar(100, "Red", "Lamba", False)
jiguli = TownCar(30, "Black", "Jiga", False)
kamaz = WorkCar(70, "White", "Kamaz", False)
ford = PoliceCar(110, "Blue", "Ford", True)
print(ford.turn_left())
print(f"When {lamborgini.turn_right()}, then {jiguli.stop()}")
print(f"{kamaz.go()} with speed exactly {ford.show_speed()}")
print(f"{ford.n} is {lamborgini.c}")
print(f"Is {jiguli.n} a police car? {kamaz.p}")
print(f"Is {lamborgini.n}  a police car? {ford.p}")
print(lamborgini.show_speed())
print(kamaz.show_speed())
print(ford.p)
print(ford.show_speed())
