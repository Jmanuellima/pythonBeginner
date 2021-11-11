# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1Lower = name1.lower()
name2Lower = name2.lower()
loveWord = "love"
trueWord = "true"
countLove = 0
countLove2 = 0
countTrue = 0
countTrue2 = 0
for letter in trueWord:
    countTrue = name1Lower.count(letter) + countTrue
    countTrue2 = name2Lower.count(letter) + countTrue2

countTrueTotal = countTrue + countTrue2

for letter in loveWord:
    countLove = name1Lower.count(letter) + countLove
    countLove2 = name2Lower.count(letter) + countLove2

countLoveTotal = countLove + countLove2

loveScoreStr = str(countTrueTotal) + str(countLoveTotal)
loveScoreInt = int(loveScoreStr)
if loveScoreInt < 10 or loveScoreInt > 90:
    print(
        f"Your score is {loveScoreInt}, you go together like coke and mentos.")

elif loveScoreInt >= 40 and loveScoreInt <= 50:
    print(f"Your score is {loveScoreInt}, you are alright together.")

else:
    print(f"Your score is {loveScoreInt}.")
