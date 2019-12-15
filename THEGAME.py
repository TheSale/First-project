'''
def func_constant(values):
    print(values[0])

func_constant ([1,2,3,4,5,6,7,8,9,10,12,13,14])
'''
#userinput = int(input())
import random
for x in range(1):
    print (random.randint(1,10))

user = input()

while random > 5:
    print ("high")
while random <= 5:
    print ("low")


while random > 5 and user == "high":
    print("user win")
while random > 5 and user == "low":
    print("user lose")
while random <= 5 and user == "high":
    print("user lose")
while random <= 5 and user == "low":
    print("user win")

