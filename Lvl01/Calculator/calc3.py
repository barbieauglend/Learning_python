import sys

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

input_first  = input("Input: ")
# x = input_first #python 2.7
x = eval(input_first) #python 3.5

sys.stdout.write("%s %i" % ('Output', x))
sys.stdout.write("\n")

rechnen = True

while rechnen:
#    input_op = raw_input("Input: ") #python 2.7
    input_op = input("Input: ") #python 3.5
    op_raw = str(input_op)
    op_raw.split()
    op = op_raw[0]
    y = int(op_raw[1])

    if op == "+":
        x = add(x,y)

    elif op == "-":
        x = subtract(x,y)

    elif op == "*":
        x = multiply(x,y)

    elif op == "/":
        x = divide(x,y)

    sys.stdout.write("%s %i" % ('Output', x))
    sys.stdout.write("\n")