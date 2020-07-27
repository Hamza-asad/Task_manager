#Task 19.2
#Task name: Combined.py
#Written by: Hamza asad
#Date: 2020/03/04

#open the two text files and read and write through it using 'r+'
#open tasks.txt
tasks_file = open("tasks.txt",'r+')
#open user.txt
user_file = open("user.txt",'r+')

#make login_success = true which will be a boolean
login_success = True
#Here we're using a while loop and saying while the statement is true
while login_success:

    #This is where we ask the user to enter their username and password
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    #Use a for loop and check for lines in the user text file
    for lines in user_file:
        #Create a variable named user_cred (user_credentials) and we are spliting the comma from the lines
        user_cred = lines.split(", ")
        #Create a variable named valid_username and get the indexing to find the username in the text file
        valid_username = user_cred[0]
        #Same as above but here we're also spliting the '\n' so that the '\n' is not included in the password
        valid_password = user_cred[1].split("\n")

        #Use the if statement and check if the username and password matches the usernames and passwords that was registered in the text file 
        if username == valid_username and valid_password[0] == password:
            #Make login_success to be false, this will make the True become false which will show that the username and password is correct
            login_success = False
            #Break out of the loop
            break

    #This is using a if statement to check 'if the boolean is true then it will check if incorrect then it will ask the user to enter the correct username and password 
    if login_success:
        #print a message to show the user that the username and password is incorrect
        print("Incorrect username and password, Please try again !")
        #Close the file
        user_file.close()
        #Re open the file user.txt
        user_file = open("user.txt",'r+')
        #Close the file
user_file.close()

#make User_busy the variable for the condition 'true'
User_busy = True
#use a while loop, this condition means while True
while User_busy:
    
    #Use the if statement and check if the username entered is 'admin' 
    if username.lower() == "admin" :
        #FOR READIBILITY AND MORE PRESENTABLE
        print("="*60)
        #This prints out welcome and prints the usernames name
        print(f"Welcome {username}!")
        #FOR READIBILITY AND MORE PRESENTABLE
        print("="*60)
        
        #Print out the options for the user to choose
        print("Please select one of the following options: \n ds - display statistics \n r - register user \n a - add task \n va - view all task \n vm - view my task \n e - exit")
        
        #printing a line space
        print("\n")

        #Ask the user to enter what option they'd like to choose
        options = input("Please select one of the above options: ")

        #Open the user.txt file and append to it
        f = open("user.txt",'a')
        
        #Check if the user entered the letter 'r' which is for registering a new user (make it lower case) 
        if options.lower() == "r":
            #Ask the user to enter their new username
            username1 = input("Enter your new username: ")
            #Ask the user for a new password
            password1 = input("Enter your new password: ")
            #Write the new username and password into the user.txt file and it should save there
            f.write(f" \n{username1}, {password1}")
            #close the file
            f.close()
            #print out a message to tell the user that their username and password was successfully made
            print("Username and Password has been successfully made.")


        #Open the user text file and read through it
        f1 = open("user.txt",'r')
        #Make a count variable and make it equal to 0
        count = 0
        #Check if the user chooses the letter 'ds' which is ti display characteristics 
        if options.lower() == "ds":
            #Use the for loop and check for the lines in f1 
            for lines in f1:
                #Add 1 to count when it reads every line
                count += 1
        #Print out a message and print the number of users that are in the file
            print(f"The total number of users are: {count}")
        #Close the file f1
        f1.close()

        #Open up the tasks file and read through it
        f2 = open("tasks.txt",'r')
        #Make a variable called count1 and make it zero
        count1 = 0
        #Check if the user enters the letter 'ds' 
        if options.lower() == "ds":
            #Use a for loop and check for the lines in f2 which is gonna be reading through the tasks file
            for lines in f2:
                #Add one to count after every line
                count1 += 1
        #print out a message and print out the number of tasks there are.
            print(f"The total number of tasks are: {count1}")
        f2.close()

        #import the date from the function 'import datetime'
        from datetime import date
        #create a new variable and get the date for today
        Todays_date = date.today()
        #open up the tasks file and append to it
        f3 = open("tasks.txt",'a')
        #Use an if statement and chekc if the user enters the letter 'a' which is to add anew task
        if options.lower() == "a":
            #Ask the User for the username of the person
            username2 = input("Please enter the username of the person: ")
            #Ask for the title of the task 
            title = input("Please enter the title of the task: ")
            #Ask for the description of the task
            description = input("Please enter a description of the task: ")
            #Ask for the due date of the task
            due_date = input("What is the due date of the task: ")
            #Now write this information to the tasks.txt file in a easy to read manner
            f3.write(f"\n{username2}, {title}, {description}, {Todays_date}, {due_date}, no ")
            #close the file
            f3.close()
        
        #open up the taskks file again and read through it using 'r'
        f4 = open("tasks.txt",'r')
        #Use a for loop and check the for the lines in task_file
        for lines in tasks_file:
            #Check if the user chooses the letter 'va' which is view all tasks
            if options.lower() == "va":
                #Here we are spliting the comma from the lines between the new sentences and indexing them  
                word = lines.split(", ")
                #Index word zero till the end of the line which is word number 5
                word1 = word[0]
                word2 = word[1]
                word3 = word[2]
                word4 = word[3]
                word5 = word[4]
                word6 = word[5]
                #Print out the task information in an easy to read manner
                print(f"Assigned to: {word1} \nTask Title: {word2} \nTask description: {word3} \nDate assigned: {word4} \nDue date: {word5} \nTask completed: {word6}")
                #Close the task file
                f4.close()

        #Open up the task file again and read and write through it using r+
        f5 = open("tasks.txt",'r+')
        #Check if the user enters the letters 'vm' which is to view my task
        if options.lower() == "vm":
            #use the for loop and check for the lines in f5
            for lines in f5:
                #Split the comma from the lines and make the variable named word
                word = lines.split(",")
                #Make the variable called word_1 and get the index for the first word in the task file to match with the username
                word_1 = word[0]
                #Use the if statement and check if the username is equal to the username in the text file
                if username == word_1:
                    #print out the statement in a easy to read manner
                    print(f"Assigned to: {word[0]} \nTask Title: {word[1]} \nTask Description: {word[2]} \nDate assigned: {word[3]} \nDue Date: {word[4]} \nTask completed: {word[5]}")
        #Close the 'f5' file
        f5.close()

        #Use the for loop and check for the option in the options that the user enters
        for option in options:
            #If the option the user enters is 'e'
            if options.lower() == "e":
                #Print a extra line to make it more presentable
                print("")
                #exit the loop
                exit
        
    ###################################################################################################################################

    #Here we are working with the other valid usernames 
    #Make an else statement that will deal with the other usernames
    else:
        #Print welcome and the admins username that has logged in
        print(f"Welcome {username}!")
        print()
        #Print out the options that the user should choose from 
        print("Please select one of the following options: \n a - add task \n va - view all task \n vm - view my task \n e- exit")
        #ask the user to choose from the above options 
        options1 = input("Please select one of the above options: ")
        print("="*60)
        
        #Close the user_file
        user_file.close()
        #Re open the userfile so that it reads all the names and passwords in the user text file
        user_file = open("user.txt",'r')
        #Make login_success to be false so that it shows the username and password is correct
        login_success = False

        #Get the date from importing date and time from the import datetime function
        from datetime import date
        #Get todays date by typing date.today()
        Todays_date = date.today()
        #Open the tasks.txt text file and append to it
        f2 = open("tasks.txt",'a')
        #Check if the user chooses the letter 'a' which will add a task 
        if options1.lower() == "a":
            #Ask the user for the username
            username2 = input("Please enter the username of the person: ")
            #Ask for the title
            title = input("Please enter the title of the task: ")
            #Ask for the description of the task
            description = input("Please enter a description of the task: ")
            #Request the due date of the task
            due_date = input("What is the due date of the task: ")
            #Write this information in the task file 'tasks.txt'
            f2.write(f"\n{username2}, {title}, {description}, {Todays_date}, {due_date}, no ")
            #Close the file
            f2.close()

        #open up the tasks.txt file and read through it
        f3 = open("tasks.txt",'r')
        #Use the for loop and check for lines in task_file
        for lines in tasks_file:
            #Use the if statement and check if the user enters the letters 'va' which is used to view all tasks
            if options1.lower() == "va":
                #This is where we split the lines from a comma that seperates them
                word = lines.split(", ")
                #This is where we index the words or sentences and put a variable to it
                word1 = word[0]
                word2 = word[1]
                word3 = word[2]
                word4 = word[3]
                word5 = word[4]
                word6 = word[5]
                #Print out the information in a easy to read manner
                print(f"Assigned to: {word1} \nTask Title: {word2} \nTask description: {word3} \nDate assigned: {word4} \nDue date: {word5} \nTask completed: {word6}")
                #Close the file
                f3.close()

        #Open up the tasks.txt file again and read and write through it
        f4 = open("tasks.txt",'r+')
        #Use the if statement and check if the user enters the letters 'vm'
        if options1.lower() == "vm":
            #Use the for loop and check for lines in the task file
            for lines in f4:
                #Split the comma from the lines
                word = lines.split(",")
                #Here we are indexing the first word and storing it in the variable word_2
                word_2 = word[0]
                #Check if the username is equal to word_2
                if username == word_2:
                    #Print out the information in a easy to read manner
                    print(f"Assigned to: {word[0]} \nTask Title: {word[1]} \nTask Description: {word[2]} \nDate assigned: {word[3]} \nDue Date: {word[4]} \nTask completed: {word[5]}")
        #Close the file
        f4.close()

        #Check for the options in options1using the for loop
        for option in options1:
            #If the user enters the letter 'e' which is used for exit
            if options1.lower() == "e":
                #Print a extra space
                print("")
                #exit the loop
                exit

    #Ask the user if they want to continue 
    #if the user doesnt want to continue then break the loop and if they want to continue it should display the menu again
    cont = input("Do you want to continue: \n(Y-yes/N-no): ").lower()
    #Check if the user enters 'n' which is used for no
    if cont == "n":
        #print a message
        print("Thank you for visiting!")
        #Make user_busy to false, this will break the loop and exit
        User_busy = False

    