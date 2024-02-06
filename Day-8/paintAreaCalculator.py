import math
def paint_cal(height, width, cover):
    numb_cans = (height * width) / cover
    round_up_cans = math.ceil(numb_cans) # math.ceil will give us 1.234394 to 1.23
    print(f"You'll need {round_up_cans} cans of paint")

test_h = int(input(": ")) # enter the height
test_w = int(input(": ")) # enter the width
coverage = 5 
paint_cal(height=test_h, width=test_w, cover=coverage)