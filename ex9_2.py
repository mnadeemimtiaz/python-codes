class Car:
    def __init__(car, reg_no, speed_max):
        car.reg_no = reg_no
        car.speed_max = speed_max
        car.speed_cur = 0
        car.dist = 0

    def accelerate(car, change):
        car.speed_cur += change
        car.speed_cur = max(0, min(car.speed_cur, car.speed_max))

if __name__ == "__main__":

    new = Car(reg_no="ABC-123", speed_max=142)

    print("Registration Number:", new.reg_no)
    print("Maximum Speed:", new.speed_max, "km/h")
    print("Travelled Distance:", new.dist, "km")
    

    new.accelerate(30)
    new.accelerate(70)
    new.accelerate(50)

    print("Current Speed of Vehicle:", new.speed_cur, "km/h")

    new.accelerate(-200)

    print("Final Speed of vehicle after Emergency Brakes were applied :", new.speed_cur, "km/h")
