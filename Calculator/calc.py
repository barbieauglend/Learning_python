import sys

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

input_first = input("First number: ")
x = int(input_first)

# input_op = raw_input("Op: ") # python 2.7
input_op = input("Op: ") #python 3.5
op = str(input_op)

input_second = input("Second number: ")
y = int(input_second)

if op == "+":
    res = add(x,y)

elif op == "-":
    res = subtract(x,y)

elif op == "*":
    res = multiply(x,y)

elif op == "/":
    res = divide(x,y)

else: print("Not a valid input")

sys.stdout.write("%i %s %i %s %i" % (x, op, y, '=', res))
sys.stdout.write("\n")