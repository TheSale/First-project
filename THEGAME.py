'''
def func_constant(values):
    print(values[0])

func_constant ([1,2,3,4,5,6,7,8,9,10,12,13,14])
'''
#userinput = int(input())
import random
while True:
  user = input()
  num = random.randint(1,10)
  print (num)

  if num > 5 and user == "high":
      print("User Win")
  elif num > 5 and user == "low":
      print("User Lose")
  elif num <= 5 and user == "high":
      print("User Lose")
  elif num <= 5 and user == "low":
      print("User Win")
