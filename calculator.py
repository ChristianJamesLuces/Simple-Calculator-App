#Luces, Christian James M. | BSCpE 1-5 | Assignment #5 | Simple Calculator

#Pseudocode
#Import the necessary modules
import pyfiglet
import time
#Welcome message and its function
intro = pyfiglet.figlet_format("WELCOME".center(39, "="), font = "digital")
print(intro)
print("\033[44;1m" + "This program is a simple app calculator that will ask the user to a math operation and perform it." + "\033[0m")
input("Press the ENTER key to run the program....\n")
time.sleep(2)


#Create a loop with True condition
while True:
    #Exception handling
    try:
        #Ask the user to choose one operation
        math_operations = print("\033[93;1m" + " Addition = + \n Subtraction = - \n Multiplication = * \n Division = /\n" + "\033[0m")
        operation = input("\033[92;1m" + "Choose one symbol to perform the math operation: " + "\033[0m")
        operators = ['+', '-', '*', '/']
        while operation not in operators:
            print ("Invalid input: It's not an operation.\n")
            operation = input("\033[92;1m" + "Choose one symbol to perform the math operation: " + "\033[0m")

        #Ask the user for two numbers
        first_number = float(input("Input your first number: "))
        second_number = float(input("Input your second number: "))
        print("\033[30m" + "Calculating....." + "\033[0m")
        time.sleep(1)

        #Perform the operation base from the user's choiced
        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            result = first_number / second_number
        
        #Display the result
        print("-" * 20)
        print("\033[91;1m" + "Result: ", result, "\033[0m")
        print("\033[100m" + "-Operation executed-\n" + "\033[0m" )

        try:
            #Ask the user if they want to try again
            try_again = str(input("\033[95m" + "Do you want to try again? (yes/no): " + "\033[0m"))

            #If yes, rerun the program
            if try_again == "yes":
                continue
            #If no, Display "Thank you!" and exit the program
            elif try_again == "no":
                gratitude = "\033[102;1m" + "Thank you!" + "\033[0m"
                print("\n" + ":" * 50)
                print(gratitude.center(60))
                print(":" * 50)
                break
            while try_again != "yes" and try_again != "no":
                print("Invalid input: Please enter only 'yes or no'.")
                try_again = str(input("\033[95m" + "Do you want to try again? (yes/no): " + "\033[0m"))

        except ValueError: 
            print("Invalid input: Please enter only 'yes or no'.")
    
    except ZeroDivisionError:
        print("Invalid Input: Cannot be devide by zero.")
    except ValueError:
        print("Invalid Input: Please enter a number")
    finally: 
        print("\033[36m" + "...Simple App Calculator Program...".center(50) + "\033[0m")
        print("=" * 50 + "\n")
