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


