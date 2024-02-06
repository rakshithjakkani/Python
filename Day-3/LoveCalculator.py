# print("Welcome to Love calculator")
# first_name = input("Type your name here\n:")
# second_name = input("Type your partner name here\n:")

# combined_name = first_name + second_name

# lowercase_convrt = combined_name.lower()

# t = lowercase_convrt.count("t")
# r = lowercase_convrt.count("r")
# u = lowercase_convrt.count("u")
# e = lowercase_convrt.count("e")
# true_count = t + r + u + e

# l = lowercase_convrt.count("l")
# o = lowercase_convrt.count("o")
# v = lowercase_convrt.count("v")
# # e = lowercase_convrt.count("e")
# love_count = l + o + v 
# love_calculator = int(str(true_count) + str(love_count))
# print(love_calculator)

# if love_calculator > 90 or love_calculator < 10:
#     print(f"Your love is greater than {love_calculator} . You go together like coke and mentos.")
# elif love_calculator > 40 and love_calculator < 50:
#     print(f"Your score is {love_calculator}, Your alright together.")
# else:
#     print(f"Your score is {love_calculator}")

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def love_calculator():
    print("Welcome to Love calculator")
    first_name = request.args.get('first_name')
    second_name = request.args.get('second_name')

    combined_name = first_name + second_name

    lowercase_convrt = combined_name.lower()

    t = lowercase_convrt.count("t")
    r = lowercase_convrt.count("r")
    u = lowercase_convrt.count("u")
    e = lowercase_convrt.count("e")
    true_count = t + r + u + e

    l = lowercase_convrt.count("l")
    o = lowercase_convrt.count("o")
    v = lowercase_convrt.count("v")
    love_count = l + o + v 
    love_calculator = int(str(true_count) + str(love_count))

    if love_calculator > 90 or love_calculator < 10:
        result = f"Your love is greater than {love_calculator}. You go together like coke and mentos."
    elif love_calculator > 40 and love_calculator < 50:
        result = f"Your score is {love_calculator}, Your alright together."
    else:
        result = f"Your score is {love_calculator}"

    return result

if __name__ == '__main__':
    app.run(port=5000)


