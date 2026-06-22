# first_name = input("Enter first Name:")
# last_name = input("ENter last Name :") #ye print nhi ho rha input le rha per output ni denga   
#  
def my_function(first_name,last_name):
    final1_name = first_name.title()
    final2_name = last_name.title()
    return f"{final1_name} {final2_name}" # obv yha tak 

last_function = my_function(first_name="Nehal",last_name="Uikey") # yha tak kuch print nhi karega agar humne isko run bhi kiyo toh run
print(last_function)





# x = input("Enter your first name:")
# y = input("Enter your last name:")
# last_function = my_function(first_name=x,last_name=y) # ye input lekar ans bhi de denga
# print(last_function)
