a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

print(a == 0 or b == 0 or c == 0 or "there aren't zero values")

print(((a == 0 and "a = 0") or (b == 0 and "b = 0") or (c == 0 and "c = 0")) and "there are all zeros")

if a > (b + c):
    print(a - b - c)

if a < (b + c):
    print(b + c - a)

if a > 50 and (b > a or c > a):
    print("Bruno")

if a > 5 and b == 7 and c == 7:
    print("Marty")