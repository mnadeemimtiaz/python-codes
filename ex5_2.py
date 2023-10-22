numb = []

for i in range(1, 6):
    while True:
        uinp = input(f"Enter a random number: ")
        if uinp == '':
            break
        number = float(uinp)
        numb.append(number)
numb.sort(reverse=True)
print("5 greatest numbers:")
for i in range(min(5, len(numb))):
    print(numb[i])