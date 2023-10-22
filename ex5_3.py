def prime(j):
    if j <= 1:
        return False
    for f in range(2, int(j ** 0.5) + 1):
        if j % f == 0:
            return False
    return True
try:
    userno = int(input("Enter a number = "))
    if prime(userno):
        print(f"{userno} is prime no.")
    else:
        print(f"{userno} is not prime no.")