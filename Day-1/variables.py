a = input('enter "a" value:')
b = input('enter "b" number')
# Here "a" value loaded to the "c". Now, "a" doesn't have any value, a is free now
# "b" value assigned to the a, now the b is free now
c = a
a = b
b = c

print("a:" + a)
print("b:" + b)
