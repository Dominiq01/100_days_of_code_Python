for number in range(1, 10):
    print(number)

for number in range(1, 11, 3):
    print(number)

total = 0
for number in range(1, 101):
    total += number

print(total)

for number in range(1, 101):
    list_from_num = [int(i) for i in str(number)]
    if (list_from_num[-1] == 0 or list_from_num[-1] == 5) and (number % 3 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif list_from_num[-1] == 0 or list_from_num[-1] == 5:
        print("Buzz")
    else:
        print(number)
