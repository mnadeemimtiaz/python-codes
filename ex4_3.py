nos = []

while True:
    user = input("Enter a number or press Enter to quit: ")

    if user == "":
        break

    try:
        number = float(user)
        nos.append(number)
    except ValueError:
        pass

if nos:
    small = min(nos)
    large = max(nos)
    print(f"Smallest No Entered: {small}")
    print(f"Largest No Entered: {large}")