import os

user_list = {
    1 : {
        "name" : "andres", "gender" : "m", "age" : 36, "height" : 188, "weight" : 188
    }
}

def clear_screen():
    os.system("clear")


def create_user():
    new_name = input("enter your name: ")
    new_gender = input("enter your gender")
    new_age = int(input("enter your age: "))
    new_height = int(input("enter your height: "))
    new_weight = int(input("enter your weight: "))
    new_id = (len(user_list) + 1)
    user_list[new_id] = {"name" : new_name, "gender" : new_gender, "age" : new_age, "height" : new_height, "weight" : new_weight}
    

def read_user():
    user_id = int(input("enter user id: "))
    print(user_list[user_id])

def update_user():
    id_to_update = int(input("enter id to update: "))
    updated_name = input("enter new name: ")
    updated_gender = input("enter new gender")
    updated_age = int(input("enter new age: "))
    updated_height = int(input("enter new height: "))
    updated_weight = int(input("enter new weight: "))
    user_list[id_to_update] = {"name" : updated_name, "gender" : updated_gender, "age" : updated_age, "height" : updated_height, "weight" : updated_weight}


def delete_user():
    id_to_delete = int(input("enter id to delete: "))
    del(user_list[id_to_delete])

def show_all_users():
    print(user_list)

def print_menu_and_get_option():
    option = int(input("enter your choice: "))
    clear_screen()
    return option

def process_option(option):
    if option == 1:
        create_user()
    elif option == 2:
        read_user()
    elif option == 3:
        update_user()
    elif option == 4:
        delete_user()
    elif option == 5:
        show_all_users()

def main():
    
    while True:
        option = print_menu_and_get_option()

        process_option(option)

main()