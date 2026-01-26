a = str(input("enter smth: "))
def funny(a):
    if a == "admin":
        print("bingo")
    else:
        print("zero")
    



user_list = {
    1 : {
        "name" : "andres", "gender" : "m", "age" : 36, "height" : 188, "weight" : 188
    }
}

print(type(user_list))
print(len(user_list))

user_list[2]["name"] = "kutska"
print(user_list)