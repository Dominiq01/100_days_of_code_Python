from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

first_num = ""
while True:
    if first_num == "":
        first_num = int(input("What is the first number?: "))
    else:
        for op in calculations:
            print(op)

        picked_op = input("Pick an operation: ")
        next_num = int(input("What is the next number?: "))
        result = calculations[picked_op](first_num, next_num)

        print(f"{first_num} {picked_op} {next_num} = {result}")

        keep_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if keep_calc != 'y':
            first_num = ""
        else:
            first_num = result
