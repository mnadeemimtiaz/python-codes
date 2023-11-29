import random

class Car:
    def __init__(self, reg_no, speed_max):
        self.reg_no = reg_no
        self.speed_max = speed_max
        self.speed_cur = 0
        self.dist = 0

    def accelerate(self, change):
        self.speed_cur += change
        self.speed_cur = max(0, min(self.speed_cur, self.speed_max))

    def drive(self, hours):
        distance_traveled = self.speed_cur * hours
        self.dist += distance_traveled

class ElectricCar(Car):
    def __init__(self, reg_no, speed_max, battery_cap):
        super().__init__(reg_no, speed_max)
        self.battery_cap = battery_cap

class gasCar(Car):
    def __init__(self, reg_no, speed_max, tankvol):
        super().__init__(reg_no, speed_max)
        self.tankvol = tankvol

if __name__ == "__main__":
    electric_car = ElectricCar(reg_no="ABC-15", speed_max=180, battery_cap=52.5)
    gas_car = gasCar(reg_no="ACD-123", speed_max=165, tankvol=32.3)

    race_distance_max = 10000
    race_hour = 0

    while electric_car.dist < race_distance_max and gas_car.dist < race_distance_max:
        electric_car.accelerate(random.randint(-10, 15))
        electric_car.drive(3)

        gas_car.accelerate(random.randint(-10, 15))
        gas_car.drive(3)

        race_hour += 3

    print("Final Results:")
    print(f"Type: Electric Car - Registration No: {electric_car.reg_no}: Speed = {electric_car.speed_cur} km/h, Distance = {electric_car.dist} km")
    print(f"Type: Gasoline Car - Registration No: {gas_car.reg_no}: Speed = {gas_car.speed_cur} km/h, Distance = {gas_car.dist} km")
