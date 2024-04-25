# building a calculator in python


num1 = int(input("Write your first number: "))
op = input("What operator (multiplication *, division / , addition + , subtraction -) will you use? ")
num2 = int(input("Write your second number: "))

if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2) 
elif op == "/":
  print(num1 / num2)
elif op == "*":
  print(num1 * num2)
else : 
  print("invalid operator")
