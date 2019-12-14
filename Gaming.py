'''
Hello
this simple questionare about what games do you play
Enter your Name
Enter your age

are you fpr pc or console

if console exit program and say people who use console are not gamers

if pc then proceed

within this 5 categories tell us what game you like the most
MOBA MMORPG FPS RACING SURVIVAL

each categorie will have 3 games

you will say why you like it

how many hours per week you spend on gaming
if less than 3 hours say good try but you are not gamer and exit questionare

if your game was not on the list tell us or use X to skip this questionare

rate my questionare
'''
import sys
print("Hello and Welcome")
print("This is simple questionare about what games do you play")
name = input ("Enter your Name: ")
age = int(input ("Enter your age: "))

print("Are you for PC or console")
platform = input("choice: " )
if platform == ("console"):
    print("People who use console are not gamers")
    sys.exit(0)
    


print("Within this 5 categories tell us what game you like the most")
print("MOBA MMORPG FPS RACING SURVIVAL")
categories = ["moba", "mmorpg", "fps", "racing", "survival"]

moba = ["lol", "dota2", "battelrite royale" ]
mmorpg = ["wow", "dns", "pwi"]
fps = ["fortnite", "pubg", "csgo"]
racing = ["nfs", "mario cart", "f1"]
survival = ["minecraft", "rift", "arc"]

category = input ("Chose category: ")
def validate(cat):
    if category in categories:
        return True
    return False
    print("wrong entery!")

if category == ("moba"):
    print(moba)
if category == ("mmorpg"):
    print(mmorpg)
if category == ("fps"):
    print(fps)
if category == ("racing"):
    print(racing)
if category == ("survival"):
    print(survival)

game = input("Chose a game you like the most: ")
if game in moba:
    print("How many hours you play games per week")
if game in mmorpg:
    print("How many hours you play games per week")
if game in fps:
    print("How many hours you play games per week")
if game in racing:
    print("How many hours you play games per week")
if game in survival:
    print("How many hours you play games per week")

time = int(input("Hours/week: "))
if time < 4:
    print("you are not true GAMER")
    print("LEAVE")
if time in range (4,10):
    print("you are a Casual gamer")
if time in range (11,100):
    print("YOU ARE GAMER")

print("Rate this program from 1 to 10")
rate = int(input ())
if rate <= 0 :
    print("invalid number")
if rate >= 11:
    print("invalid number")
if rate in range (1,10):
    print ("thanks for rating")
if rate in range (7,10):
    print (":)")
if rate in range (4,6):
    print (":(")
if rate in range (1,3):
    print (":O")