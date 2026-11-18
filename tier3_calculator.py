# Tier 3: Input -> Processing -> Output

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # A well-designed program checks first, instead of crashing.
    if b == 0:
        return None
    return a / b


def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That is not a number. Try again.")


def run():
    # INPUT
    number_1 = read_number("First number (example: 20): ")
    number_2 = read_number("Second number (example: 5): ")

    # PROCESSING + OUTPUT
    print(f"{number_1:g} + {number_2:g} = {add(number_1, number_2):g}")
    print(f"{number_1:g} - {number_2:g} = {subtract(number_1, number_2):g}")
    print(f"{number_1:g} x {number_2:g} = {multiply(number_1, number_2):g}")

    result = divide(number_1, number_2)
    if result is None:
        print("Cannot divide by zero. Please enter a different second number.")
    else:
        print(f"{number_1:g} / {number_2:g} = {result:g}")


if __name__ == "__main__":
    run()
