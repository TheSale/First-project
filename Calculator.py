print("Operation-Command")
print("addition-add\nsubtraction-sub\nmultiplication-mult\ndivision-div")
operation = input ("command ")
x = float(input ())
y = float(input ())

if operation == "add":
    print("result", x+y)
if operation == "sub":
    print("result", x-y)
if operation == "mult":
    print("result", x*y)
if operation == "div":
    print("result", x/y)
