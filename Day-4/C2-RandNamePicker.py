names_string = input("enter the names here\n:")
# Name should provide with , seperated like rakshith, raghu, akhil
# The below slipt function is used to split the each element in list should be seperated.
names = names_string.split(", ")
print(names)

import random
# when i provide the 3 three names the num_items=3
num_items = len(names)
# the number_items would look like this [0,1,2,3]. but we don't have four. len fucntion count exact number.
# but list index starts from 0, 1, 3 .... 
# so thats why we use [0,1,2,3 - 1] = [2] is nothing but [0,1,2]
random_number = random.randint(0, num_items - 1)
person_to_pay = names[random_number]
print(person_to_pay)