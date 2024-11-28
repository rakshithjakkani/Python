# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# def student_grades():
#     student_grades = {}
#     for students, score in student_scores.items():
#         if score >= 91 and score <= 100:
#             student_grades[students] = "oustanding"
#         elif score >= 81 and score <= 90:
#             student_grades[students] = "Exceeds Expectations" 
#         elif score >= 71 and score <= 80:
#             student_grades[students] = "Acceptable"
#         else:
#             student_grades[students] = "failed"  
#     print(student_grades)
            
# student_grades()


rakshith_travel_log = {
    "country_india": {
        "number_of_visits": 2,
        "cities_visited": ["mumbai", "bangalore", "hyderabad"]
    },
    "country_us": {
        "number_of_visits": 3,
        "cities_visited": ["chia", "chilo", "kua", ["a", "b", "c"]]
    } 
}


print(rakshith_travel_log["country_us"]["cities_visited"])