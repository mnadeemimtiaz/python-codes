talent_str = input("Enter talents:")
pound_str = input("Enter pounds:")
lot_str = input("Enter lots:")
talent = float(talent_str)
pound = float(pound_str)
lot = float(lot_str)
calctalents = ((talent*20)*32)*13.3
calcpounds = (pound*32)*13.3
calclot = lot*13.3
kg = calctalents+calcpounds+calclot
print("The weight in modern units:")
print("Kilograms:" +str (kg))

