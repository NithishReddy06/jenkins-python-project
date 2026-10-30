def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":

    print("====================================")
    print("       PYTHON APPLICATION")
    print("====================================")

    print("Addition:       ", add(10, 20))
    print("Multiplication: ", multiply(5, 4))
    print("Subtraction:    ", subtract(20, 5))
    print("Division:       ", divide(20, 4))

    print("===================================")
    print("Hi")
    print("Application executed successfully!")
    