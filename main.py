# Create a menu, which asks the user to read,write or append info from txt files.
# Create 3 userDefine functions for each functionality using the fileName as a parameter.
# use a condition to stop the menu.

def readInfo(fileName):
    file = open(fileName, "r")
    data = file.read()
    print(data)
def writeInfo(fileName):
    file = open(fileName, "w")
    num = int(input("How many lines you wanna enter :"))
    for x in range (num):   # 3
        info = input("Enter the line :")  # Tuesday
        file.write(info+"\n")
    print("Written successful !")
    file.close()
def appendInfo(fileName):
    file = open(fileName, "a")
    data = int(input("How many line do you want? :"))
    for x in range (data):
        cursive = input("write it: ")
        file.write(cursive+"\n")
    print("Append Written successful !")
    file.close()


# check if userAge is more than 18.

#   WAY OF THINKING ---> SKILL


# ask the user to enter the age
# check the condition if > 18
# print the message

#

while True:
    print("Menu :")
    print("1. Read info")
    print("2. Write info")
    print("3. Append info")
    print("4. END")
    user = int(input("Choose :"))

    if user == 1:
        fileName = input("Enter the fileName: ")
        readInfo(fileName)
    elif user == 2:
        fileName = input("Enter the fileName: ")
        writeInfo(fileName)
    elif user == 3:
        fileName = input("Enter the fileName: ")
        appendInfo(fileName)
    elif user == 4:
        print("Thanks for using my Application !")
        break



# strip()  with string
# booleans