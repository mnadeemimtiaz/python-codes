username = "python"
password = "rules"
attempts = 0
while attempts < 5:
   user = str(input("Enter User ID :"))
   passw = str(input("Enter User ID :"))

   if user == username and passw == password:
      print("Welcome")
      break
   if attempts == 5:
      print("Access Denied")
   elif user != username and passw != password:
      print("Try again")
      attempts = attempts + 1

