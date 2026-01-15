def my_function():
    for i in range(1, 21):
        print(i)
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
#       The for loop is looping through numbers in range from 1 to 19
# 2. When is the function meant to print "You got it"?
#       The function is meant to print message when the index will have a value of 20
# 3. What are your assumptions about the value of i?
#       That it's not going to achieve 20 because the range will be from 1-19 excluding last value which is 20