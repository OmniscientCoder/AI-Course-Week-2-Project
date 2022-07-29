# Import only system from os
from os import system, name

# Import sleep to show output for some time period
from time import sleep

# Define our clear function
def clear():
        _ = system('cls')

# Sleep for 2 seconds after printing output
sleep(2)

# Now call function we defined above
clear()