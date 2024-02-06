# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"
# print(format_name(input("what is your first name: "), input("What is your second name: ")))


def format_name(f_name, l_name):
    # The below line is to heading of a our function
    """Take the first and the last name and formate
    it to return the title case version of the same"""
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return f"Result: {format_f_name} {format_l_name}"
name = format_name("rakshith", "jakkani")
print(name)