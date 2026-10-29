a = float(input ("First number: "))
op = input("Operator (+ - * /): ")
b = float(input ("Second number: "))
if op == "+":
  result = a + b
elif op == "-":
  result = a - b
elif op == "*":
  result = a * b
elif op == "/":
  result = a / b
print (f"{a} {op} {b} = {result}")