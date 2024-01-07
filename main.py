# ---------
# Imports
import time

# ---------
# Functions

#Listing the option for user
def options():
  print("Here are the available ways we can help you today:")
  print("")
  print("  1. Place Holder 1")
  print("  2. Place Holder 2")
  print("  3. Place Holder 3")
  print("  4. Place Holder 4")
  print("  5. Exit Program")

# Lets user choose and leads them to where ever
def user_selection():
  user_pick = int(input("Pick an option listed above to provide your assistance: "))


  if user_pick == 1:
    print("")
    print("------------------")
    print("You have selected option 1")
    print("------------------")
    print("")
  elif user_pick == 2:
    print("")
    print("------------------")
    print("You have selected option 2")
    print("------------------")
    print("")
  elif user_pick == 3:
    print("")
    print("------------------")
    print("You have selected option 3")
    print("------------------")
    print("")
  elif user_pick == 4:
    print("")
    print("------------------")
    print("You have selected option 4")
    print("------------------")
    print("")
  elif user_pick == 5:
    print("")
    print("------------------")
    print("Thank you for using our program!\nWe hope we provided the help you needed.")
    print("------------------")
    print("")
    exit()
  else:
    print("")
    print("------------------")
    print("Invalid option. Please try again.")
    print("------------------")
    print("")
    time.sleep(1)
    user_selection()

    

# ---------
# Greeting

print("")
print("------------------")
print("Welcome to the Elite 101 Help Desk!")
print("------------------")
print("")
time.sleep(2)
user_name = input("What is your name? ")
time.sleep(1)
print("Hello, " + user_name + "!")
time.sleep(1)
user_age = input("How old are you? ")

# If user doesn't put in a number
while not user_age.isdigit():
  print("")
  print("------------------")
  print("Please enter a valid age in digits.")
  print("------------------")
  print("")
  user_age = input("How old are you? ")

  

time.sleep(1)
print("You're " + str(user_age) +".. well welcome anyways, "+ user_name + "!")
time.sleep(2)

# ---------
# Listing options
print("")
print("------------------------------------")
print("")
options()
time.sleep(1)
print("")
user_selection()
print("")
