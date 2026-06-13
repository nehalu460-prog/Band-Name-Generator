def format_name(f_name, l_name):
    """Take a first and last name and format it to return the
    title case version of the name."""
    
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"

f_name = input("ENTER FIRST NAME: ")
l_name = input("ENTER LAST NAME: ")

full_name = format_name(f_name, l_name)

print(full_name)
print("Length:", len(full_name))