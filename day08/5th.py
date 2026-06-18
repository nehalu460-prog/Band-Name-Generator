# def calculate_love_score(name1,name2 ):
#    name1 = " "

#    for letter in name1:
#        print(letter, "=", name.count(letter))
       
#    name2 = " "
#    name = "Nehal"

#    for letter in name2:
#        print(letter, "=", name.count(letter))

# calculate_love_score(name1="snavi",name2="Tejas")
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")  
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Punit", "Tanisha ")