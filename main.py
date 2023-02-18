
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
letter = name1 + name2
combine = letter.upper()
t = combine.count("T")
r = combine.count("R")
u = combine.count("U")
e = combine.count("E")
l = combine.count("L")
o = combine.count("O")
v = combine.count("V")
true = t + r + u + e
love = l + o + v + e
true_love = int(str(true) + str(love))
if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love > 40 and true_love < 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")