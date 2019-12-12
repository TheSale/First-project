print("Hello World")
print("welcome\nto \nmy \nprogram")

print("This is yours")
Day = input ()
#Day = int(Day)
print(Day + " visit")

print("Thank you for your time \nI hope you will have fun time here")


Odraslih = 76
Dece = 112
print("Today we have", Odraslih+Dece, "visitors")
print("From what", Dece, "are kids", "and", Odraslih, "are grown up")

cenaodrasli = 7
cenadeca = 5
print("From what we earn", (Odraslih*cenaodrasli)+(Dece*cenadeca),"eur", "so far")
if ((Odraslih*cenaodrasli)+(Dece*cenadeca) >= 300):
    print("we had a good day")
if ((Odraslih*cenaodrasli)+(Dece*cenadeca) <= 300):
    print("we had a bad day")
print("Rate this program from 1 to 10")
rate = int(input ())
mylist = [1,2,3,4,5,6,7,8,9,10]
'''
if rate in range (1,10):
    print ("thanks for rating")
if rate in range (11,999999999999999,):
    print ("Invalid number")
'''
#if (rate >= 11, rate<= 0) :
#    print("invalid number")
#if ("rate" <= 0):
#    print("invalid number")
#if (rate != mylist):
#    print("error")
#if rate in range (1,10):
 #       return True
    #return False
      #  print ("thanks for rating")
'''
def check(rate):
    if 0 <= rate >= 11 and round(rate,2)==rate:
        return True
        print("thanks")
    return False 
    while True 
    print("error")
'''
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
