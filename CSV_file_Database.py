# Creating a user database with CSV files

"""
Logical Process
1. Check to see if user is logged in.
    a. If logged in, ask if they would like to logout or quit
        i. Either quit or logout user and restart
    b. Else, ask if they would like to login/register/quit
        i. If login, ask user for email/password.
            1. If correct, log user in and restart.
            2. Else, display error and restart
        ii. If register,ask for email/password/password2
            1. If passwords match, save user and restart.
            2. Else, display error and restart.
        iii. if quit, say thank you and exit program

"""
import os
import csv

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

# handling user registration and writing to csv
def registerUser():
    with open('users.csv', mode= 'a', newline= '') as f:
        writer = csv.writer(f,delimiter=',')
        print('To register, please enter your info:')
        email = input('E-mail: ')
        password = input('Password: ')
        Confirm_Password = input('Re-type password: ')
        clear_output()

        if password == Confirm_Password:
            writer.writerow([email,password])
            print('You are registered successfully!')
        else:
            print('Fill in your details correctly, passwords should match')

# Handling user Login
def userLogin():
    print('To login, please enter your credentials')

    email = input('E-mail: ')
    password = input('Password: ')
    clear_output()

    with open('users.csv', mode= 'r') as f:
        reader = csv.reader(f,delimiter=',')
        for row in reader:
            if row ==[email,password]:
                print('login was successful!')
                return True
            else:
                print('Please input your credentials correctly')
                return False
            
# main loop
active = True
logged_in = False

while active:
    if logged_in:
        print('a. Logout\nb. Quit')

    else:
        print('a. Login\nb. Register\nc. Quit')
        action = input('What would you like to do?  ').lower()
        clear_output()

        if action == 'register' and logged_in == False:
            registerUser()
        elif action == 'login' and logged_in == False:
            userLogin()
           
        elif action == 'quit':
            active == False
            print('Thank you for using our system!')
        elif action == 'logout' and logged_in == True:
            logged_in = False
            print('You have successfully loged out')
        else:
            print('oops! action failed, please try again')
                

        


