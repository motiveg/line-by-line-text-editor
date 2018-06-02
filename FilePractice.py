############################################## #
# Program Options: read, rewrite, append, quit #
################################################

# read: displays the contents of the file
def dataRead():
    try:
        fileName = input("\nEnter a file to read: ")

        fCheck = open(fileName, "r")
        fCheck.close()

        print("\nThe file contents will be displayed between upper and lower dashes.")
        print("\n----------")

        with open(fileName, "r") as f:
            print(f.read())

        print("----------")
        print("Going back to main menu.\n")

    except IOError:
        createFile = input("\n\'{}\' does not exist. Would you like to create it?(y/n): ".format(fileName))

        if createFile == "y":
            print("\nCreating new file...")
            newFile = open(fileName, "w+")
            newFile.close()
            print("\'{}\' is now created.".format(fileName))
            print("Going back to main menu.\n")

        elif createFile == "n":
            print("\n\'{}\' was not created.".format(fileName))
            print("Going back to main menu.\n")

        else:
            print("\nNot a valid option.")
            print("Going back to main menu.\n")

# deletes current file contents and writes new content into file
# ask to make a copy before clearing contents
def dataClear():
    try:
        fileName = input("\nEnter a file to clear contents: ")

        fCheck = open(fileName, "r")
        fCheck.close()

        clearFile = input("\nWould you like to make a backup copy of this file before proceeding?\n" + 
          "\'copy\' will automatically prefix the current filename when copied (y/n): ")

        if clearFile == "y":
            print("\nCreating a copy file...")

            src = "{}".format(fileName)
            dest = "copy{}".format(fileName)

            from shutil import copy
            copy(src, dest)

            print("{} has been made.\n".format(dest))

        elif clearFile == "n":
            print("\nWARNING: You will not be able to recover the file contents once you proceed.")
            proceed = input("Would you like to proceed to clear the contents of {}?(y/n): ".format(fileName))

            if proceed == "y":
                print("\nClearing file contents...")
                fClear = open(fileName, "w")
                fClear.close()
                print("File contents have been cleared.")
                print("Going back to main menu.\n")

            elif proceed == "n":
                print("\nFile contents have not been cleared.")
                print("Going back to main menu.\n")

            else:
                print("\nNot a valid option.")
                print("File contents have not been cleared.")
                print("Going back to main menu.\n")

        else:
            print("\nNot a valid option.")
            print("Going back to main menu.\n")

        if clearFile != "n":
            proceed = input("Would you like to proceed to clear the contents of {}?(y/n): ".format(fileName))

            if proceed == "y":
                print("\nClearing file contents...")
                fClear = open(fileName, "w")
                fClear.close()
                print("File contents have been cleared.\n")

            elif proceed == "n":
                print("File contents have not been cleared.")

            else:
                print("Not a valid option.")
                print("File contents have not been cleared.")

    except IOError:
        newFile = input("\n\'{}\' does not exist. Would you like to create it?(y/n): ".format(fileName))

        if newFile == "y":
            print("\nCreating new file...")
            fCreate = open(fileName, "w+")
            fCreate.close()
            print("\'{}\' is now created.".format(fileName))
            print("Going back to main menu.\n")

        elif newFile == "n":
            print("\'{}\' was not created.".format(fileName))
            print("Going back to main menu.\n")

        else:
            print("Not a valid option.")
            print("Going back to main menu.\n")

# keeps current file contents and writes new contents at the end of file
def dataAppend():
    try:
        fileName = input("\nEnter a file to append to: ")

        fCheck = open(fileName, "r")
        fCheck.close()

        print("\nYou may keep entering in text as long as you want.")
        print("Every time you press enter, a new line will be created in the file.")
        print("When you want to quit, type \"^quit^\" on a new line.\n")
        print("Writing the following contents to {}:\n".format(fileName))

        with open(fileName, "a") as f:

            appendString = ""
            while appendString != "^quit^":
                appendString = input()

                if appendString != "^quit^":
                    f.write(appendString)
                    f.write("\n")

        print("\n\nGoing back to main menu.\n")

    except IOError:
        newFile = input("\n\'{}\' does not exist. Would you like to create it?(y/n): ".format(fileName))

        if newFile == "y":
            print("\nCreating new file...")
            fCreate = open(fileName, "w+")
            fCreate.close()
            print("\'{}\' is now created.".format(fileName))
            print("Going back to main menu.\n")

        elif newFile == "n":
            print("\n\'{}\' was not created.".format(fileName))
            print("Going back to main menu.\n")

        else:
            print("\nNot a valid option.")
            print("Going back to main menu.\n")

# does nothing
def doNothing():
    print("", end='')

# print "Goodbye!" with a newline
def printGoodbye():
    print("Goodbye!\n")

# main user interface
if __name__ == "__main__":

    print("---FILE MANIPULATION PROGRAM---\n")

    choice = ""
    while choice != "4" or choice != "quit":
        # print menu options
        print("Options:")
        print("1) READ - displays file contents")
        print("2) CLEAR - clears file contents")
        print("3) APPEND - adds user-inputted strings into file contents")
        print("4) QUIT - exit the program")
        print("\nSelect an option either by inputting a number or the action.")
        print("Example: \"1\" or \"read\" are both acceptable choices.")
        print("Inputs for this menu are not case-sensitive.\n")
        print("Choice: ", end='')

        # user inputs choice
        choice = input()
        #if choice != "1" or choice != "2" or choice != "3" or choice != "4":
        choice = choice.lower()

        # process choice
        if choice == "1" or choice == "read":
            dataRead()
    
        elif choice == "2" or choice == "clear":
            dataClear()
        
        elif choice == "3" or choice == "append":
            dataAppend()
        
        elif choice == "4" or choice == "quit":
            break

        else:
            print("\nNot a valid option.\n")

    print("\n---------END OF PROGRAM---------\n")
    
    # farewell message
    from threading import Timer
    Timer(2.0, printGoodbye).start()
    Timer(4.0, doNothing).start()