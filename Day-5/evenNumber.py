#############--this will give you addition of all even number between 2 and you specified number
# print("welcom to even number calculator! specify a number ill tell you number of even number up to your number")

# total_even_numbers = 0
# target = int(input("enter a number"))
# for number in range(2, target + 1, 2):
#     total_even_numbers += number
# print(total_even_numbers)
    
print("Welcome to even number calculator! Specify a number and I'll tell you the number of even numbers up to your number.")

total_even_numbers = 0
target = int(input("Enter a number: "))

for number in range(2, target + 1, 2):
    total_even_numbers += 1

print(total_even_numbers)
