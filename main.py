

def readInfo(fileName):                # function to read a txt file
    file = open(fileName, "r")
    data = file.read()
    print(data)
def writeInfo(fileName):             # used to write stuff in txt file
    file = open(fileName, "w")
    num = int(input("How many lines you wanna enter :"))
    for x in range (num):   # 3
        info = input("Enter the line :")  # Tuesday
        file.write(info+"\n")
    print("Written successful !")
    file.close()
def appendInfo(fileName):            # used to append the info in txt file instead of writing
    file = open(fileName, "a")
    data = int(input("How many line do you want? :"))
    for x in range (data):
        cursive = input("write it: ")
        file.write(cursive+"\n")
    print("Append Written successful !")
    file.close()





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



