print (" \n                             >>> Welcome to a simple python Calculator \n")
num1 = float(input("          >>> Enter a Number :  "))

num2 = float(input("          >>> Enter another Number :  "))
op = input ("\n Type the type of Operations that you'd like to perform + - * /  ")

if op == "+" :
    print ("\n Your answer is: ")
    print (num1 + num2)
elif op == "-":
    print  (num1 - num2)
elif op == "*":
    print (num1* num2)
elif op == "/":
    print (num1 / num2)
else:
    print ("Invalid Operation")
