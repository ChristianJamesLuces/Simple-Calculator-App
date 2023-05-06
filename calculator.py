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
    #Ask the user to choose one operation
    operation = str(input("Choose one of the four math operatoins (Addition, Subtraction, Multiplication, and Division)"))
    first_number = float(input("Input your first number: "))
    second_number = float(input("Input your second number: "))
#Ask the user for two numbers
#Perform the operation base from the user's choiced
#Display the result
#Ask the user if they want to try again
#Display "Thank you!" before it exits