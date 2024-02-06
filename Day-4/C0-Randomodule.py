# The modules are the set of code which is already developed and build. In python it is a feature to use another code
# When we build custom modules, lets say ill create one file called rakshith.py in that file ill define a variable like love = mygirl
# then ill import that module like 
# import rakshith
# a = rakshith.love
# print(a)-----> it will be mygirl
import random

# when i want to print a random number between 1 to 10 
random_number = random.randint(1, 10)
print(random_number)

# when i want to print random floating number b/w 0 and 1
random_float = random.random()
print(random_float)

# when i want to print random floating number up to 5 
float_extension5 = random_float * 5
print(float_extension5)

#when i want to print random float from specifi floating number to other floating number
float = random.uniform(2.5, 4.2)
print(float)

# when i want to print random number from 0 to 9 inclusive
random0_9 = random.randrange(9)
print(random0_9)

# when we want to print random even number which is divisable by 2 from 0 100
random_even = random.randrange(0, 101, 2) 
print(random_even)

# Four samples without replacement
# This prints random four numbers from the list of numbers.
random_sample = random.sample([10, 20, 30, 40, 50], k=4)
print(random_sample)