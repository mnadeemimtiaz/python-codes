citys = []
print("Enter Five cities of your choice:")
for i in range(5):
    cityname = input(f"City {i + 1}: ")
    citys.append(cityname)
print("\nList of cities in order they are entered is :")
for city in citys:
    print(city)