def gal_to_l(gal):
    lit = gal * 3.78541
    return lit

def main():
    while True:
        gal = input("Enter Fuel in American gallons and a negative value to exit from the program: ")
        if float(gal) < 0:
            break
        lit = gal_to_l(float(gal))
        print(f"{gal} American gallons are equivalent to {lit} liters.")

main()

