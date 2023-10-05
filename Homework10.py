
#1
def decorator(attempts):
    def decorator_wrapper(function):
        print("Decorator sets quantity of attempts for function")
        def wrapper(*args, **kwargs):
            results = [function(*args, **kwargs) + i for i in range(attempts)]
            return results
        return wrapper
    return decorator_wrapper
@decorator(attempts=5)
def plsOne(x):
    x += 1
    return x
results = plsOne(1)
print("Calculation results =", results)

#2

def logDecorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Function "{func.__name__}" called with arguments: x={args[0]}, y={args[1]}, Result: {result}')
        return result
    return wrapper
@logDecorator
def sumFunc(x, y):
    return x + y
sumFunc(3, 5)

#3
logins=["user1","user2","admin"]
def decorator(function):
    def wrapper(*args,**kwargs):
        login=input("Enter your login")
        if login in logins:
            return function(login,*args,**kwargs)
        else:
            print("Error, you are not logged in ")
    return wrapper

@decorator
def loginIn(login):
    print(f"You are logged in, welcome {login}!")
loginIn()

#4

def checkDecorator(function):
    def wrapper(*args,**kwargs):
        x=input("Enter first integer")
        if x.isnumeric():
            y = input("Enter second integer")
            if y.isnumeric():
                return function(int(x), int(y))
            else:
                print("Second input is not an integer!")
        else:
            print("First input is not an integer!")

    return wrapper

@checkDecorator
def sumFunc(x, y):
    print(x + y)
sumFunc()