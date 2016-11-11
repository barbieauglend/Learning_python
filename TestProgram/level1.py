# 01
#
#for i in range(999):
#   print(i+1)

# 02
#
#n = ""
#for i in range(99):
#    if (i + 1) % 5 == 0:
#        n = n + str(i + 1) + "\n"
#    i += 1
#
#f = open("Test1.txt", "w")
#f.write(n)

#03
#input_age  = input("Enter your age: ")
#age = int(input_age)
#if age < 18:
#    print("So sorry! Too young!")
#    exit()
#else: print("yay, you can use it!")

#04
input_login  = raw_input("Enter your login: ")
login = str(input_login)

input_text  = raw_input("Enter text: ")
text = str(input_text)

input_filename = raw_input("save to file: ")
filename = str(input_filename)

f = open(filename, "w")
f.write(text)