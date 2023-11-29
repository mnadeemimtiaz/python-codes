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

if __name__ == "__main__":
    cars = []

    for i in range(1, 11):
        reg_no = f"ABC-{i}"
        speed_max = random.randint(100, 200)
        car = Car(reg_no=reg_no, speed_max=speed_max)
        cars.append(car)

    race_distance_max = 10000
    race_hour = 0

    while all(car.dist < race_distance_max for car in cars):
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
        race_hour += 1

    print("Final Results:")

    for car in cars:
        print(f"Car Registration No: {car.reg_no}: Speed = {car.speed_cur} km/h, Distance = {car.dist} km")
