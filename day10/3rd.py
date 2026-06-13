def my_function(name, section):
    if name == "" or section == "":
        return "You did not provide valid inputs"

    final_name = name.title()
    final_section = section.title()

    return f"{final_name} {final_section}"

name = input("What is your name? ")
section = input("Which section are you from? ")

print(my_function(name, section))