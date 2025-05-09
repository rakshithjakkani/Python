from user_class import User

user_1 = User("01", "rakshith")
user_2 = User("02", "jakkani")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)