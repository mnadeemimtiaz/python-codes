class Car:
    def __init__(self, reg_no, speed_max):
        self.reg_no = reg_no
        self.speed_max = speed_max
        self.speed_cur = 0
        self.dist = 0

    def accelerate(self, change):
        self.speed_cur += change
        self.speed_cur = max(0, min(self.speed_cur, self.speed_max))

    def drive(self, hours_drive):
        dist_travel = self.speed_cur * hours_drive
        self.dist += dist_travel

if __name__ == "__main__":
    car = Car(reg_no="ABC-123", speed_max=142)

    print("Registration Number:", car.reg_no)
    print("Maximum Speed:", car.speed_max, "km/h")
    print("Initial Travelled Distance:", car.dist, "km")

    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)

    print("Current Speed of Vehicle:", car.speed_cur, "km/h")

    car.drive(1.5)
    print("Travelled Distance after driving for 1.5 hours:", car.dist, "km")

    car.accelerate(-200)

    print("Final Speed of vehicle after Emergency Brakes were applied:", car.speed_cur, "km/h")
    print("Final Travelled Distance of the vehicle:", car.dist, "km")
