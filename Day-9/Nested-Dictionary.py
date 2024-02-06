# ########-----Dictionary-------###########
# minfy = {
#     "aws": "bharath",
#     "devops": "bharath",
#     "mimo": "sreekanth"
# }   

# ############----nested-dictionary--------##########
# devops = {
#     "team": ["viswa", "akhil", "rakshith", "sai"],
#     "other_team": {"nitin": ["waheed", "someone"], "sreekant": ["leads", "sreeram"]} 
# }

# ###########-----Nesting-Dictionary in List---###########
# travel_log = [
#     {
#         "country": "india",
#         "cities_visited": ["knr", "hyd", "mumbai"],
#         "total_count": 3
#     },
#     {
#         "country": "china",
#         "cities_visited": ["ahuang", "chuang", "chelio"],
#         "total_count": 3
#     }

# ]

import random
country = input("Enter the country that you have visited recently: ") # enter the country that you have visited.
visits = int(input("How many times you visited the country: ")) # enter the number of visits
list_of_cities = eval(input()) # enter the cities you have visited
travel_log = [
    {
        "country": "india",
        "cities_visited": ["knr", "hyd", "mumbai"],
        "total_count": 3
    },
    {
        "country": "china",
        "cities_visited": ["ahuang", "chuang", "chelio"],
        "total_count": 3
    }

]

def add_new_country(country_name, times_visited, cities_visited):
    new_travel_log = {}
    new_travel_log["country"] = country_name
    new_travel_log["visits"] = times_visited
    new_travel_log["cities"] = cities_visited
    travel_log.append(new_travel_log)
add_new_country(country, visits, list_of_cities)

print(f"I have been visited {travel_log[2]['country']} times and cities are {travel_log[2]['visits']}")
print(f"my favorite city is  ")