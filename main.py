from options import * 
from functions import * 

#calls file selection function the first time 
fileSelection()
 
going = True

#while loop allows for an iterative interface 
while going:
  print(options)
  choice = input("\033[1;38mWhat is your choice?\033[1;m")
  if choice == "1":
    fileSelection()
  elif choice == "2":
    option2()
  elif choice == "3": 
    option3()
  elif choice == "4":
    option4() 
  elif choice == "5":
    option5()
  elif choice == "6":
    option6()
  elif choice == "7":
    option7()
  elif choice == "exit" or choice =="Exit" or choice =="EXIT":
    going = False
  elif choice == "help" or choice =="Help" or choice == "HELP":    
    helpfunction()
  else:
    print("Please select one of the options below.")


#prints when the user exits the program.
print("Goodbye.")
