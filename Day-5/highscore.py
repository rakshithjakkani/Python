# print the highest score in the list of numbers 72 89 12 45 81 91 28 76 89 18 29 
student_score = input("enter the your score and your friends scores with space sperated\n:").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])

highest_score = 0 
for score in student_score:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
