#!

fruits = {
    "fruit": ["Apple", "Mango", "Banana", "Orange", "Grapes"]
}

print(fruits)

#2

programming_language = {
    "Bug": "An error in a program",
    "Function": "A reusable block of code",
    "Loop": "Repeats a block of code"
}

print(programming_language["Function"])
programming_language["OOPS"] = "Object oriented programming using class and objects" 
print(programming_language)
#  edit an dictionary
programming_language["Bug"] = "different type of error "
print(programming_language)


# 3
fruits = {
    "fruit": ["Apple", "Mango", "Banana", "Orange", "Grapes","Kiwi"],
    "vegatables":["bhandi","ladyfinger","Tamatar"]
}

print(fruits)
for vitamin in fruits :
    print(vitamin)  #give only key not value because of fruit
    print(fruits[vitamin])

empty_dictionary = {} 
# fruits = {}
fruits = empty_dictionary #direct mein fruits = {} bhi kar sakta 
print(fruits)
