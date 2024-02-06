student_score = {
    "rakshith": 90,
    "akhil": 80,
    "adarsh": 75,
    "saiteja": 99,
    "bokada": 30
}
student_grades = {}
for student in student_score:
    score = student_score[student]
    if score > 90:
        student_grades[student] = "outstanding"
    elif score > 80:
        student_grades[student] = "Exeeds Expectation"
    elif score > 70:
        student_grades[student] = "pass"
    else:
        student_grades[student] = "fail"

print(student_grades)