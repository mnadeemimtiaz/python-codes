gender = str(input("Enter your gender: "))

if gender == "female" or gender == "male":
    hemo = int(input("Enter your hemoglobin value(g/l): "))
if (hemo>=117 and hemo<=155 and gender=="female"):
    print("Your Hemoglobin Value is Normal")
if (hemo<117 and gender=="female"):
     print("Your Hemoglobin Value is low")
if (hemo>155 and gender=="female"):
     print("Your Hemoglobin Value is high")
if (hemo>=134 and hemo<=167 and gender=="male"):
    print("Your Hemoglobin Value is Normal")
if (hemo<134 and gender=="male"):
        print("Your Hemoglobin Value is low")
if (hemo>167 and gender=="male"):
        print("Your Hemoglobin Value is high")