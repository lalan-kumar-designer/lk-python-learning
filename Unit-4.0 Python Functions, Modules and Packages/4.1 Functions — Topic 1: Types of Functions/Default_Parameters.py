# Default Parameters

def greet(name="Student"):
    print("Hello", name)

greet()
greet("Lalan")


def add(a, b=10):
    print(a + b)

add(5)
add(5, 20)


def student(name, branch="Electrical Engineering"):
    print("Name:", name)
    print("Branch:", branch)

student("Lalan")
student("Lalan", "Civil Engineering")