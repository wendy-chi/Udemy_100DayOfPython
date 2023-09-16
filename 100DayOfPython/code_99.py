def format_name(f_name, l_name):
    family_name = f_name.title()
    last_name = l_name.title()
    name = family_name + " " + last_name
    return name

a = input("What is your family name?\n")
b = input("What is your last name?\n")

name = format_name(a, b)
print(name)
