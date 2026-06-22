print("💕 Welcome to the Love Calculator 💕")

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

combined_names = (name1 + name2).lower()

true_score = (
    combined_names.count("t")
    + combined_names.count("r")
    + combined_names.count("u")
    + combined_names.count("e")
)

love_score = (
    combined_names.count("l")
    + combined_names.count("o")
    + combined_names.count("v")
    + combined_names.count("e")
)

score = int(str(true_score) + str(love_score))

print(f"\nYour Love Score is {score}%")

if score < 10 or score > 90:
    print("💘 You go together like Coke and Mentos!")
elif 40 <= score <= 50:
    print("😊 You are alright together.")
elif 51 <= score <= 75:
    print("❤️ A beautiful connection!")
elif 76 <= score <= 90:
    print("💞 Soulmate vibes!")
else:
    print("🤔 Love is mysterious, keep exploring!")
