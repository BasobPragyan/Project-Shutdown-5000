def shutdown():
    shut_input=input("Do you want to shutdown the program y/n?")
    if shut_input=='y':
        print("Shutting down")
    elif shut_input=='n':
        print("Aborting shutdown")
    else:
        print("Sorry could not get the input. What do you want to do?")

print("Program shutdown")
shut=input("Enter choice : y/n")
shutdown()