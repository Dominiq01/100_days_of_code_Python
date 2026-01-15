import random
import my_module
# random_integer = random.randint(1,6)
#
# print(random_integer)
# print(my_module.my_fav_num)
#
# random_num_0_to_1 = random.random() * 10
# print(random_num_0_to_1)
#
# random_float = random.uniform(1, 10)
# print(random_float)

random_num = random.randint(0, 1)
print(random_num)
if random_num == 0:
    print("Heads")
else:
    print("Tails")