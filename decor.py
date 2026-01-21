login = str(input("enter your login: "))

def login_checker(func):
    def wrapper_decorator(*args, **kwargs):
        if login == "admin":
            value = func(*args, **kwargs)
            return value
        else:
            print("acess denied")
        
        
    return wrapper_decorator

@login_checker
def balance():
    print("your balance is $5")

balance()