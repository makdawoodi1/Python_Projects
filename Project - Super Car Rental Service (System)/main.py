# Importing Modules
import login
import register

# Importing built-in python modules 
import os
import time

# Initializing Main Class
class Main:
    def __init__(self):

        # Initializing Class Attributes
        login.Login.user_validation = False
        login.Login.admin_validation = False
        login.Login.update_car = False
        login.Login.car_viewed = False
        login.Login.from_admin = False
        Main.from_menu = False

        # Printing Welcome Message
        print('\n|---------------------------------------------------|')
        print('|>>> Welcome to Super Car Rental Services (SCRS) <<<|')
        print('|---------------------------------------------------|')

        # Printing Main Menu Message
        print('\n\n|-----------------|')
        print('|>>> MAIN MENU <<<|')
        print('|-----------------|')

        # Taking user choice as an input
        while True:
            self.menu_choice = input('''
1. Login to access system
2. Register yourself to the platform
3. View all cars available for rent
4. Exit --> ''')

            # IF user input is 1 then move to LOGIN SCREEN
            if self.menu_choice == '1': Main.login(Main)

            # IF user input is 2 then move to REGISTERATION SCREEN
            elif self.menu_choice == '2': Main.registeration(Main)

            # IF user input is 3 then move to Display Car Screen
            elif self.menu_choice == '3': Main.view_cars(Main)

            # IF user input is 4 then move to EXIT SCREEN
            elif self.menu_choice == '4': Main.exit(Main)

            # If user input is not from any above option then return to ask user again
            else:
                print('\n|--- Sorry! Choose from the correct options provided below! ---|')
                continue

    # LOGIN SCREEN
    # Taking user input
    def login(self):
        print('\n\n|-----------------------------|')
        print('|>>> WELCOME TO LOGIN PAGE <<<|')
        print('|-----------------------------|')
        user_choice = input('''
1. Login as an Admin
2. Login as a Registered User
3. Exit --> ''')

        # Reading Login Class Attributes and Methods from login module
        login_user = login.Login(Main)

        # Checking the user input
        while True:

            # IF user input is 1 then move to LOGIN as an ADMIN Screen
            if user_choice == '1':
                
                login.Login.admin(Main)

            # IF user input is 2 then move to LOGIN as a REGISTERED USER Screen
            elif user_choice == '2':
                login.Login.registered_user(Main)

            # IF user input is 3 then return to MAIN MENU SCREEN
            elif user_choice == '3':
                print('\n|--- Going back to Main Menu ---|')
                Main()

            # IF user input is not from any above option then return to LOGIN Screen
            else:
                print('\n|!!! Sorry! Choose from the correct options provided below! !!!|')
                Main.login(Main)

    # REGISTERATION SCREEN
    def registeration(self):
        print('\n\n|-------------------------------------|')
        print('|>>> WELCOME TO REGISTERATION PAGE <<<|')
        print('|-------------------------------------|')

        # Reading Register Class Attributes and Methods from register module
        registeration = register.Register()

        # Taking user input
        register_choice = input('''
        1. Register Yourself
        2. Exit --> ''')

        # Checking user input
        while True:

            # IF user input is 1 then register new user
            if register_choice == '1':
                while True:

                    # Creating a list which will store user details
                    registered_users = []

                    # Checking if the user is registered or not
                    if registeration.register_user() == True:

                        # Creating user txt file to store the details
                        file = open(f'Registered_Users\\{registeration.user_name}.txt', 'w')

                        # Appending the user details to the list
                        registered_users.append(registeration)

                        # Writing the user details in the txt file
                        file.write('\n'.join([f'First Name: {registeration.fname}', f'Last Name: {registeration.lname}', f'Mobile Number: {registeration.mob_no}', f'Username: {registeration.user_name}', f'Email: {registeration.email}', f'Password: {registeration.password}', f'Gender: {registeration.gender}', f'Date of Birth: {registeration.dob}']))

                        file.close()

                        # Storing user details in variables to write them in a registered_users.txt file
                        with open(f'Registered_Users\\{registeration.user_name}.txt', 'r') as file1:

                            # Checking if the details stored exist
                            for content in file1.readlines():
                                if registeration.user_name in content: USERNAME = registeration.user_name
                                if registeration.email in content: EMAIL = registeration.email
                                if registeration.password in content: PASSWORD = registeration.password

                        # # Writing lines in a txt file
                        with open('registered_users.txt', 'a') as file2:
                            # file2.write('---------------------------------\n')
                            # file2.write(''.join([f'USERNAME: {USERNAME}', f'EMAIL: {EMAIL}', f'PASSWORD: {PASSWORD}']))
                            # file2.write('\n---------------------------------')
                            file2.write('\n'.join([f'{USERNAME}', f'{EMAIL}', f'{PASSWORD}\n']))
                            file2.write('---------------------------------------------------------\n')

                        print('\n|--- The User has been added to registry! ---|')

                    # Asking if the user wants to register another user or not
                    while True:
                        another_register = input('\n\nDo you want to Register another user? Reply with (YES) or (NO) --> ').upper()

                        # IF the user input is YES then Moving back to REGISTERATION FORM
                        if another_register == 'YES':
                            print('\n|--- Moving to REGISTERATION FORM ---|')
                            break

                        # IF the user input is NO then returning back to MAIN MENU SCREEN
                        elif another_register == 'NO':
                            print('\n|--- Moving back to REGISTERATION SCREEN ---|')
                            Main.registeration(Main)

                        # IF the user input is not from above option then asking the user again for the input
                        else:
                            print('\n|!!! Please put suitable values !!!|')
                            continue
                    
                    break

            # IF user input is 2 then returning back to MAIN MENU SCREEN
            elif register_choice == '2':
                print('\n--- Going back to Menu ---|')
                Main()

            # IF the user input is not from above option then asking the user again for the input
            else:
                print('\n|!!! Sorry! Choose from the correct options provided below !!!|')
                Main.registeration(Main)

    # DISPLAY CAR SCREEN
    # Moving to Car Details Screen
    def view_cars(self):
        Main.from_menu = True
        _login = login.Login(Main)

    # EXIT SCREEN
    # Printing Exit Program Message
    def exit(self):
        print('\n|---------------------------------------|')
        print('|>>> THANK YOU FOR USING OUR PROGRAM <<<|')
        print('|---------------------------------------|')
        exit()

# Making object of the Main Class
scrs = Main()
