#FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     value = a_dict["key"]
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
#     print("There was an error")
# except KeyError as error_mess:
#     print(f"The key {error_mess} does not exist.")
# else:
#     # IT WILL ACTIVATE WHEN TRY SUCCEEDS
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
#     raise KeyError("This is my own error")

#KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]

height = float(input("Height: ")) # in meters
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2

print(bmi)
