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
time.sleep(5)

#Create a loop with True condition
while True:
    #Exception handling
    try:
        #Ask the user to choose one operation
        operation = str(input("Choose one of the four math operatoins (Addition, Subtraction, Multiplication, and Division: )"))
        
        #Ask the user for two numbers
        first_number = float(input("Input your first number: "))
        second_number = float(input("Input your second number: "))
        print("Calculating.....")
        time.sleep(5)

        #Perform the operation base from the user's choiced
        if operation == "Addition":
            result = first_number + second_number
        elif operation == "Subtraction":
            result = first_number - second_number
        elif operation == "Multiplication":
            result = first_number * second_number
        elif operation == "Division":
            result = first_number / second_number
        else:
            print("Invalid input: It's not an operation")

        #Display the result
        print("Result: ", result)
        print("-Operation executed-")

        #Ask the user if they want to try again
        try_again = str(input("Do you want to try again? (yes/no): "))

        #If no, Display "Thank you!" and exit the program
        if try_again == "no":
            print("Thank you!")
            break
    
    except ZeroDivisionError:
        print("Invalid Input: Cannot be devide by zero.")
    except ValueError:
        print("Invalid Input: Please enter a number.")
    finally: 
        print("Closing the Simple App Calculator program.")
