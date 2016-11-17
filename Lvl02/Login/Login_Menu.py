# python 3.5
import getpass
from time import gmtime, strftime

def getpswd():
    pswd = getpass.getpass('Password:')
    return pswd

def startmenu():
    user_choice = input(" 1. Kochrezepte \n 2. Weltherrschaft \n 3. Uhrzeit \n Q. Beenden \n Your choice: ")
    return user_choice

input_login = input("Enter your Username: ")
user = str(input_login)
test = 0
pswd = getpswd()

while pswd != "superhacker":
    if test < 2:
        print("Wrong Password! Try again!")
        pswd = getpswd()
        test += 1
    else:
        print("Wrong Password! I am sorry!")
        exit()

user_choice = startmenu()
online = True

while online:
    if user_choice == "1":
        print("Kochrezepte aus der ganzen Welt! \n www.chefkoch.de")
        user_choice = startmenu()

    elif user_choice == "2":
        print("Weltherrschaft? Die Plannung findet erst morgen statt")
        user_choice = startmenu()

    elif user_choice == "3":
        print(strftime("%H : %M :%S", gmtime()))
        user_choice = startmenu()

    elif user_choice == "Q":
        print("Bye =)")
        online = False

    else:
        print("Something went wrong! What do you want me to do?")
        user_choice = startmenu()

