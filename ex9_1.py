class Car:
    def __init__(car, reg_no, speed_max):
        car.reg_no = reg_no
        car.speed_max = speed_max
        car.speed_cur = 0
        car.dist = 0

if __name__ == "__main__":
    new = Car(reg_no="ABC-123", speed_max=142)
    print("Registration Number:", new.reg_no)
    print("Maximum Speed:", new.speed_max, "km/h")
    print("Current Speed:", new.speed_cur, "km/h")
    print("Travelled Distance:", new.dist, "km")
