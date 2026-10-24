# Global Scope and Local Scope

x = 100

def display():
    y = 50
    print("Local Variable:", y)
    print("Global Variable:", x)

display()
print("Global Variable:", x)


a = 10

def show():
    a = 20
    print("Local a:", a)

show()
print("Global a:", a)


number = 5

def change():
    global number
    number = 15

change()
print("Number:", number)