# fruits = ["apple", "banana", "tomato"]
# for fruit in fruits:
#     print(fruit)

### general sum function 
# numbers = [9, 4, 5, 7, 4, 4, 8, 98, 5, 938, 376, 23, 65, 99]
# print(sum(numbers))

### builing our own sum function using for loop
# numbers = [9, 4, 5, 7, 4, 4, 8, 98, 5, 938, 376, 23, 65, 99]
# sum = 0
# for a in numbers:
#     sum += a 
# print(sum)

### general max function
# numbers = [9, 4, 5, 7, 4, 4, 8, 98, 5, 938, 376, 23, 65, 99]
# print(max(numbers))

# ## building max function using for loop
# numbers = [9, 4, 5, 7, 4, 4, 8, 98, 5, 938, 376, 23, 65, 99]
# max = 0
# for a in numbers:
#     if a > max:
#         max = a
# print(max)

#### range function in for loop
# sum100 = 0
# for a in range(1, 101):
#     sum100 += a
# print(sum100)

for a in range(1, 101):
    if a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    elif a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    else:
        print(a)