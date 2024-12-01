def function_1(f_name, l_name):
    """It takes first and last name. And it will formate into title case then give it to you""" # this is called Docstrings
    fi_name = f_name.title()
    la_name = l_name.title()
    return f"{fi_name} {la_name}"

def function_2(name):
    return f"{name}"
output = function_2(function_1("rakshith", "jakkani"))
print(output)