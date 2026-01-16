while True:
    print("Check your BMI")
    age = int(input("How old are you? "))
    if age == 999:
        break
    gender = input("what is you gender? (f or m)")
    weight = float(input("Enter your weight :"))
    height = float(input("Enter your height :"))/100
    
    min = 20
    max = 50
    s = "="
    bmi = round(weight/height**2)

    print(f"Your bmi is {bmi}")
    l = (bmi - min)//5
    r = 6 - l

    print(str(min) + s * l + "I" + s * r + str(max))

    if gender == "m" and bmi < 30 and age < 40:
        print("recomendation 1")
    if gender == "m" and bmi > 30 and age < 40:
        print("recomendation 2")
    if gender == "m" and bmi < 30 and age > 40:
        print("recomendation 3")
    if gender == "m" and bmi > 30 and age > 40:
        print("recomendation 4")
    if gender == "f" and bmi < 30 and age < 40:
        print("recomendation 5")
    if gender == "f" and bmi > 30 and age < 40:
        print("recomendation 6")
    if gender == "f" and bmi < 30 and age > 40:
        print("recomendation 7")
    if gender == "f" and bmi > 30 and age > 40:
        print("recomendation 8")
    
    
    