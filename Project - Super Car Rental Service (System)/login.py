# Importing Built-in modules
import os
import time

# Importing register module
from register import *

# Initializing Car_Details Class
class Car_Details:
    def __init__(self):

        # Initializing Class Attributes
        self._make = ''
        self._model = ''
        self._year = 0
        self._color = ''
        self._mileage = 0
        self._car_mechanics = ''
        self._with_driver = ''
        self._seats = 0
        self.cost = 0
        self.duration = 0

    # ADD CAR FORM
    def add_car(self):
        print('\n\n|-------------------------------|')
        print('|>>> WELCOME TO ADD CAR FORM <<<|')
        print('|-------------------------------|')
        # Asking admin inputs to store the details
        # IF the detials are not accordingly then catch the exception error
        try:
            while True:
                print('\n')
                self._make = input('Enter Car Company (Example: HONDA): ').upper()
                self._model = input('Enter Car Model: (Example: CIVIC): ').upper()
                while True:
                    try:
                        self._year = int(input('Enter Car Model Year (Example: 2020): '))
                        break
                    except:
                        print('\n!!! NOT A NUMBER !!!')
                        continue
                self._color = input('Enter the color of a Car (Example: BLACK): ').upper()
                while True:
                    try:
                        self._mileage = int(input('Enter Car Mileage (Example: 7): '))
                        break
                    except:
                        print('\n!!! NOT A NUMBER !!!')
                        continue
                while True:
                    self._car_mechanics = input('Enter Car Mechanics (AUTO) or (MANUAL): ').upper()
                    if self._car_mechanics == 'AUTO' or self._car_mechanics == 'MANUAL':
                        self._car_mechanics = self._car_mechanics
                        break
                    else:
                        print('\n|!!! Car Mechanics should be either (AUTO) or (MANUAL) !!!|')
                        continue
                while True:
                    self._with_driver = input('Is the car with driver or not? Reply with (Yes) or (No): ').upper()
                    if self._with_driver == 'YES' or self._with_driver == 'NO':
                        self._with_driver = self._with_driver
                        break
                    else:
                        print('\n|!!! The input should be (YES) or (NO) !!!|')
                        continue
                while True:
                    try:
                        self._seats = int(input('Enter number of seats in a car (2) or (4) or (6) or (8) or (16): '))
                        if self._seats == 2 or self._seats == 4 or self._seats == 6 or self._seats == 8 or self._seats == 16:
                            self._seats = self._seats
                            break
                        break
                    except:
                        print('\n!!! NOT A NUMBER !!!')
                        continue
                while True:
                    try:
                        self._cost = int(input('How many PKR/DAY? '))
                        break
                    except:
                        print('\n!!! NOT A NUMBER !!!')
                        continue
                while True:
                    self._duration = input('How many Hours for rent? (Full day) or (Half day) --> ').upper()
                    if self._duration == 'FULL DAY' or self._duration == 'HALF DAY':
                        self._duration = self._duration
                        break
                    else:
                        print('\n|!!! The input should be (YES) or (NO) !!!|')
                        continue

                # Converting integer values to string so they can be written on txt files
                self._year = str(self._year)
                self._mileage = str(self._mileage)
                self._seats = str(self._seats)
                self._cost = str(self._cost)

                return True

        # Handle the exception error and showing the FORM again
        except ValueError:
            print('\n|>>> Please try entering suitable vehicle information using only whole numbers for Year, Mileage and Driver <<<|')
            Car_Details.add_car(Car_Details)

    # DISPLAY CAR SCREEN
    def display_car(self):

        # Checking if the car exists or not
        if os.listdir('Registered_Cars'):
            self.detail_of_cars = os.listdir('Registered_Cars')
        else:
            # IF the car doesn't exist then ask to add more cars
            add_car = input('\nSorry there are no cars to rent. Do you want to add more cars? (Yes) or (No) --> ').upper()
            # IF the user says yes then check IF admin is logged in or not
            if add_car == 'YES':
                # IF admin is logged in then ask the admin to add a car
                if Login.admin_validation: Login.add_car(Car_Details)
                # IF not then ask admin to login first
                else: 
                    print('\n|--- Sorry you have to login as an Admin in order to proceed ---|')
                    Login.admin(Car_Details)
            # IF the user says no then move to MAIN MENU SCREEN or LOGIN PAGE based on where the user is coming from
            elif add_car == 'NO':
                # IF the user is coming from MAIN MENU SCREEN then move back to MAIN MENU SCREEN
                if Login.main.from_menu:
                    Login.main.from_menu = False
                    Login.main()
                # IF not then move to LOGIN PAGE
                else:
                    Login.user_validation = False
                    Login.admin_validation = False
                    print('\n|--- Going back to Login Page ---|')
                    Login.main.from_menu = False
                    Login.main.login(Car_Details)
            # IF the user input is not from above then ask the user to put suitable values
            else:
                print('\n|!!! Put suitable values !!!|')
                Car_Details.display_car(Car_Details) 

        
        # self.car_contents = []

        # PRINTING DISPLAY SCREEN MESSAGE
        print('\n\n|-------------------------------------|')
        print('|>>> WELCOME TO DISPLAY CAR SCREEN <<<|')
        print('|-------------------------------------|')
        print('\n')
        print('       ----------------------------------------------------------------------------------------------------------------------------------------------------')
        print('       |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CAR DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
        print('       ----------------------------------------------------------------------------------------------------------------------------------------------------')
        print('       ====================================================================================================================================================')
        print('       %-13s %-21s %-10s %-15s %-15s %-14s %-17s %-11s %-11s %-9s' %('| COMPANY', '| MODEL', '| YEAR', '| COLOR', '| DURATION', '| CAR MECHANICS', '| WITH DRIVER', '| SEATS', '| COST', '| MILEAGE |'))
        print('       ====================================================================================================================================================')

        # Reading Files in Registered Cars Folders and Storing car details in separate variables
        # Printing Cars with Display
        for idx, files in enumerate(os.listdir('Registered_Cars')):
            with open(f'Registered_Cars\\{files}', 'r') as f:
                for car_content_line in f.readlines():
                    if '\n' in car_content_line: car_content_line = car_content_line.replace('\n', '')
                    
                    car_content_details = car_content_line.split(' | ')
                    COMPANY = car_content_details[0]
                    MODEL = car_content_details[1]
                    YEAR = car_content_details[2]
                    COLOR = car_content_details[3]
                    DURATION = car_content_details[4]
                    CAR_MECHANICS = car_content_details[5]
                    WITH_DRIVER = car_content_details[6]
                    SEATS = car_content_details[7]
                    COST = car_content_details[8]
                    MILEAGE = car_content_details[9]

                    if idx < 9:
                        print(f'({idx + 1}) = %-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))
                    else:
                        print(f'({idx + 1}) =%-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))

            print('       ====================================================================================================================================================')

        # IF the request is from admin to view details of cars
        if Login.from_admin:
            # Checking the user input
            while True:
                admin_choice = input('\nDo you want to go back? (YES) or (NO): ').upper()
                # IF the user input is YES then Going back to ADMIN DASHBOARD
                if admin_choice == 'YES':
                    print('\n|--- Going back to ADMIN DASHBOARD ---|')
                    Login.from_admin = False
                    Login.menu_admin(Car_Details)
                # IF the user input is NO then asking the user to select a car or not 
                elif admin_choice == 'NO':
                    admin_choice_1 = input('\nDo you want to select a car? (YES) or (NO): ').upper()
                    if admin_choice_1 == 'YES':
                        print('\n|--- Please Login as a Registered Users first ---|')
                        Login.from_admin = False
                        Login.registered_user(Car_Details)
                    elif admin_choice_1 == 'NO':
                        print('\n|--- Going back to ADMIN DASHBOARD ---|')
                        Login.from_admin = False
                        Login.menu_admin(Car_Details)
                # IF the input is not from above then asking the user again
                else:
                    print('\n|!!! Please put suitable values !!!|')
                    continue

        # IF the user wants to select and view a car
        if not (Login.update_car):
            user_choice = input('''
            1. Do you want to Select and Book a car?
            2. Exit --> ''')
            if user_choice == '1':
                Login.car_viewed = True
                Car_Details.select_and_book_car(Car_Details)
            elif user_choice == '2':
                if Login.main.from_menu:
                    scrs = Login.main
                else:
                    if Login.user_validation:
                        Login.menu_user(Car_Details)
                    else:
                        scrs = Login.main
            else:
                    print('\n|!!! Please put suitable values !!!|')
                    Car_Details.display_car(Car_Details)

        # IF the user wants to modify a car
        else:   
            while True:
                # Selecting a car to modify
                try:
                    self.product = int(input('\nSelect a Car to modify: '))
                except:
                    print('\n|!!! Please put in numbers !!!|')
                    continue
                try:
                    f = open(f'Registered_Cars\\{self.detail_of_cars[self.product - 1]}', 'r')
                    f.close()
                except:
                    print('\n|!!! Sorry your choice is invalid. Please select the car again. !!!|')
                    Car_Details.display_car(Car_Details)
                    
                # Checking which features of a car user wants to change and changing them exactly
                while True:
                    with open(f'Registered_Cars\\{self.detail_of_cars[self.product - 1]}', 'r') as f:
                        while True:
                            self.car_feature = input('\nWhich car feature do you want to modify?\n \
(COMPANY) | (MODEL) | (YEAR) | (COLOR) | (DURATION) | (CAR MECHANICS) | (WITH DRIVER) | (SEATS) | (COST) | (MILEAGE): ').upper()
                            for idx, car_content_line in enumerate(f.readlines()):
                                if '\n' in car_content_line: car_content_line = car_content_line.replace('\n', '')

                                car_content_details = car_content_line.split(' | ')
                                COMPANY = car_content_details[0]
                                MODEL = car_content_details[1]
                                YEAR = car_content_details[2]
                                COLOR = car_content_details[3]
                                DURATION = car_content_details[4]
                                CAR_MECHANICS = car_content_details[5]
                                WITH_DRIVER = car_content_details[6]
                                SEATS = car_content_details[7]
                                COST = car_content_details[8]
                                MILEAGE = car_content_details[9]
                                if self.car_feature == 'COMPANY': 
                                    COMPANY = input('\nEnter Company details: ').upper()
                                elif self.car_feature == 'MODEL': 
                                    MODEL = input('\nEnter Model details: ').upper()
                                elif self.car_feature == 'YEAR': 
                                    while True:
                                        try:
                                            YEAR = int(input('\nEnter Year details: '))
                                            break
                                        except:
                                            print('\n|!!! Please put in numbers !!!|')
                                            continue
                                elif self.car_feature == 'COLOR': 
                                    COLOR = input('\nEnter Color details: ').upper()
                                elif self.car_feature == 'DURATION': 
                                    while True:
                                        DURATION = input('\nEnter Duration details (FULL DAY) or (HALF DAY): ').upper()
                                        if DURATION == 'FULL DAY' or DURATION == 'HALF DAY': 
                                            DURATION = DURATION
                                            break
                                        else:
                                            print('\n|!!! Duration should be either(FULL DAY) or (HALF DAY) !!!|')
                                            continue
                                elif self.car_feature == 'CAR MECHANICS':
                                    while True:
                                        CAR_MECHANICS = input('\nEnter Car Mechancis (AUTO) or (MANUAL): ').upper()
                                        if CAR_MECHANICS == 'AUTO' or CAR_MECHANICS == 'MANUAL':
                                            CAR_MECHANICS = CAR_MECHANICS
                                            break
                                        else:
                                            print('\n|!!! Car Mechanics should be either (AUTO) or (MANUAL) !!!|')
                                            continue
                                elif self.car_feature == 'WITH DRIVER': 
                                    while True:
                                        WITH_DRIVER = input('\nIs there a Driver? (YES) or (NO): ').upper()
                                        if WITH_DRIVER == 'YES' or WITH_DRIVER == 'NO':
                                            WITH_DRIVER = WITH_DRIVER
                                            break
                                        else:
                                            print('\n|!!! The input should be (YES) or (NO) !!!|')
                                            continue
                                elif self.car_feature == 'SEATS': 
                                    while True:
                                        try:
                                            SEATS = int(input('\nEnter number of seats in a car (2) or (4) or (6) or (8) or (16): '))
                                            if SEATS == 2 or SEATS == 4 or SEATS == 6 or SEATS == 8 or SEATS == 16:
                                                SEATS = SEATS
                                                break
                                            else:
                                                print('\n|!!! Please put numbers from below !!!|')
                                                continue
                                        except:
                                            print('\n|!!! Please put values in numbers !!!|')
                                elif self.car_feature == 'COST': 
                                    while True:
                                        try:
                                            COST = int(input('\nEnter Amount of car: '))
                                            break
                                        except:
                                            print('\n|!!! Please put values in numbers !!!|')
                                            continue
                                elif self.car_feature == 'MILEAGE': 
                                    while True:
                                        try:
                                            MILEAGE = int(input('\nEnter Mileage amount: '))
                                            break
                                        except:
                                            print('\n|!!!Please put values in numbers !!!|')
                                            continue
                                else:
                                    print('\n|!!! This feature is invalid. Please select car again and put features from below. !!!|')
                                    Car_Details.display_car(Car_Details)
                                break
                            break
                    
                    # Modifying Car details and removing previous records
                    with open(f'Registered_Cars\\{Car_Details.detail_of_cars[Car_Details.product - 1]}', 'r') as file:
                        previous_car_content = file.read()
                    os.remove(f'Registered_Cars\\{Car_Details.detail_of_cars[Car_Details.product - 1]}')                         
                    with open(f'Registered_Cars\\{COMPANY}_{MODEL}_{YEAR}_{COLOR}_{DURATION}_{CAR_MECHANICS}_{WITH_DRIVER}_{SEATS}_{COST}_{MILEAGE}.txt', 'w') as file:
                        file.write(' | '.join([f'{COMPANY}', f'{MODEL}', f'{YEAR}', f'{COLOR}', f'{DURATION}', f'{CAR_MECHANICS}', f'{WITH_DRIVER}', f'{SEATS}', f'{COST}', f'{MILEAGE}']))
                
                    with open(f'Registered_Cars\\{COMPANY}_{MODEL}_{YEAR}_{COLOR}_{DURATION}_{CAR_MECHANICS}_{WITH_DRIVER}_{SEATS}_{COST}_{MILEAGE}.txt', 'r') as file:
                        new_car_content = file.read()
                                  
                    with open(f'Registered_Cars\\{COMPANY}_{MODEL}_{YEAR}_{COLOR}_{DURATION}_{CAR_MECHANICS}_{WITH_DRIVER}_{SEATS}_{COST}_{MILEAGE}.txt', 'r') as file:
                        new_car_content = file.read()
                        
                    # Asking user if the user wants to change another car features or not
                    while True:
                            another_change = input('\nDo you want to change another car detail? (YES) or (NO): ').upper()
                            if another_change == 'YES' or another_change == 'NO': 
                                break
                            else: 
                                print('\n|!!! Please put suitable values !!!|')
                                continue
                    if another_change == 'YES': Car_Details.display_car(Car_Details)
                    elif another_change == 'NO': 
                        print('\n|--- The Car Details has been changed ---|')
                        Login.menu_admin(Car_Details)
                    else: break
                    break
                print('\n|--- The Car Details has been changed ---|')
                Car_Details.display_car(Car_Details)

    # Function for Selecting and Booking a Car
    def select_and_book_car(self):
        # IF the car isn't viewed already then show car details
        if not (Login.car_viewed):
            while True:
                show_car_details = input('\nDo you want to show car details? (YES) or (NO): ').upper()
                if show_car_details == 'YES':
                    Login.car_viewed = False
                    Car_Details.display_car(Car_Details)
                elif show_car_details == 'NO':
                    print('\n|--- Going back to ADMIN DASHBOARD ---|')
                    Login.menu_user(Car_Details)
                else:
                    print('\n|!!! Please put suitable values !!!|')
                    continue
        # IF the user is coming from REGISTERED USER DASHBOARD then ask the user to select a car
        while True:
            if Login.main.from_menu == False:
                # Storing the car choice in variable
                try:
                    self.car_choice = int(input('\nSelect a Car: '))
                except Exception as e:
                    print('\n|!!! Please put numbers !!!|')
                    continue
                Login.car_selected = True
                try:
                    self.car_for_booking = self.detail_of_cars[self.car_choice - 1]
                except:
                    print('\n|!!! Invalid choice. Please select the car again !!!|')
                    continue
                if self.car_for_booking:
                    user_choice = input('''
        1. Do Payment to Confirm Booking?
        2. Exit --> ''')
                # IF user choice is 1 then Showing the payment screen to user
                if user_choice == '1': 
                    Login.from_payment = False
                    Car_Details.payment_screen(Car_Details)
                # IF the user choice is 2 then showing the Display Car Screen
                elif user_choice == '2': Car_Details.display_car(Car_Details)
                # IF the user input is not from above then asking the user again
                else:
                    print('\n|!!! Please put suitable values !!!|')
                    continue
            # Asking user to login as a registered user first in order to rent a car
            else:
                print('\n|--- Please you have to login as a user first to rent a car ---|')
                Login.main.from_menu = False
                Login.registered_user(Car_Details)

    # Function for Payment Screen
    def payment_screen(self):
        # IF coming from REGISTERED MENU to payment screen
        if Login.from_payment:
            if Login.car_selected:
                Login.from_payment = False
                Car_Details.payment_screen(Car_Details)
            else:
                print('\n|--- You have to select a car first ---|')
                Car_Details.display_car(Car_Details)

        # IF coming from SELECT AND BOOK A CAR
        while True:
            # IF THE car is selected then ask the user to Enter payment for the selected car
            try:
                Login.car_selected = False
                while True:
                    self.car_payment = int(input('\nEnter your payment for the selected car: '))
                    with open(f'Registered_Cars\\{self.car_for_booking}', 'r') as f:
                        for line in f.readlines():
                            content = line.split(' | ')
                            if str(self.car_payment) == content[8]:
                                self.car_payment = self.car_payment 
                            else:
                                print('\n|!!! Invalid payment. Please put again. !!!|')
                                break
                        if str(self.car_payment) != content[8]:
                            continue
                        else:
                            break

                self.car_payment = str(self.car_payment)
                with open(f'Registered_Cars\\{self.car_for_booking}', 'r') as f:
                    content = f.read()
            except:
                print('\n|!!! Please put numbers !!!|')
                continue

            # IF THE payment is correct then ask the user to Enter the duration of the car
            while True:
                self.car_duration = input('\nEnter the duration for the selected car: ').upper()
                with open(f'Registered_Cars\\{self.car_for_booking}', 'r') as f:
                    for line in f.readlines():
                        _content = line.split(' | ')
                        if self.car_duration == _content[4]:
                            self.car_duration = self.car_duration
                            break
                        else:
                            print('\n|!!! Invalid duration. Please put again. !!!|')
                            break
                    if self.car_duration != _content[4]:
                        continue
                    else: break
            
            file = open(f'Registered_Cars\\{self.car_for_booking}', 'r')
            content = file.read()
            file.close()
            self.booking_confirmed = True
            

            with open(f'Registered_Cars\\{self.car_for_booking}', 'r') as f:
                self.car_content = f.read()
            with open(f'Rented_Cars\\{self.car_for_booking}', 'w') as file:
                file.write(self.car_content)
            with open(f'Rental_History\\{Login.user_contents}_{Car_Details.car_for_booking}', 'w') as file2:
                file2.write(f'{Login.user_contents} | {self.car_content}')
            with open(f'User_Rental_History\\{Login.user_contents}_{Car_Details.car_for_booking}', 'w') as file3:
                file3.write(f'{Login.user_contents} | {self.car_content}')

            os.remove(f'Registered_Cars\\{self.car_for_booking}')

            # ASK the user if the user wants to rent another car            
            while True:
                another_payment = input('\nDo you want to pay for another rented car? (Yes) or (No) --> ').upper()
                if another_payment == 'YES':
                    Car_Details.display_car(Car_Details)
                elif another_payment == 'NO':
                    Login.menu_user(Car_Details)
                else:
                    print('\n|!!! Please put suitable values !!!|')
                    continue

    # Function for User Rental History
    def rental_history(self):
        # DEFINING LIST to store rental history files
        self.rental_history_contents = []

        # IF user isn't logged in
        if not (Login.user_validation):
            Car_Details._rental_history = True
            Login.registered_user(Car_Details)

        # IF user is logged in
        else:
            # IF there is rental history of user
            if os.listdir('User_Rental_History'):
                rental_history_files = os.listdir('User_Rental_History')
                for files in rental_history_files:
                    if f'{Login.user_contents}' in files:
                        with open(f'User_Rental_History\\{files}', 'r') as f:
                            rental_history_content = f.read()
                            self.rental_history_contents.append(rental_history_content)
                    else:
                        pass
                if not (self.rental_history_contents):
                    print('\n|--- Sorry, You have no rental history ---|')
                    while True:
                        rental_history_choice = input('\nDo you want to rent a car? (Yes) or (No) --> ').upper()
                        if rental_history_choice == 'YES':
                            if Login.registered_user: Car_Details.display_car(Car_Details)
                            else:
                                print('\n|--- Sorry, You have to login as a user first ---|')
                                Login.registered_user(Car_Details)
                        elif rental_history_choice == 'NO':
                            Login.registered_user(Car_Details)
                        else: continue
                print('\n')
                print('      --------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> USER RENTAL HISTORY <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                print('      --------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('      ====================================================================================================================================================================')
                print('      %-15s %-13s %-21s %-10s %-15s %-15s %-14s %-17s %-11s %-11s %-9s' %('| USERNAME', '| COMPANY', '| MODEL', '| YEAR', '| COLOR', '| DURATION', '| CAR MECHANICS', '| WITH DRIVER', '| SEATS', '| COST', '| MILEAGE |'))
                print('      ====================================================================================================================================================================')
                for idx, vehicle in enumerate(self.rental_history_contents):
                    vehicle_content = vehicle.split(' | ')
                    print(f'({idx + 1}) = %-15s %-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-10s|' %(f'| {vehicle_content[0]}', f'| {vehicle_content[1]}', f'| {vehicle_content[2]}', f'| {vehicle_content[3]}', f'| {vehicle_content[4]}', f'| {vehicle_content[5]}', f'| {vehicle_content[6]}', f'| {vehicle_content[7]}', f'| {vehicle_content[8]}', f'| {vehicle_content[9]}', f'| {vehicle_content[10]}'))
                print('      ====================================================================================================================================================================')
                while True:
                    rental_choice = input('\n1. Exit --> ')
                    if rental_choice == '1':
                        if Login.user_validation: Login.menu_user(Car_Details)
                        else: 
                            print('\n|--- Sorry you have to login as a user first ---|')
                            Login.registered_user(Car_Details)
                    else:
                        print('\n|!!! Put suitable values !!!|')
                        continue

            # IF there is no rental history of user
            else:
                while True:
                    rental_history_choice = input('\nSorry, There is no rental history. Do you want to add more cars? (Yes) or (No) --> ').upper()

                    if rental_history_choice == 'YES':
                        try:
                            if Login.admin_validation: Login.add_car(Car_Details)
                        except:
                            print('\n|--- Sorry, You have to login as an ADMIN first ---|')
                            Login.admin(Car_Details)
                    elif rental_history_choice == 'NO':
                        try:
                            if Login.user_validation: Login.menu_user(Car_Details)
                        except:
                            print('\n|--- Sorry, You have to login as a user first ---|')
                            Login.registered_user(Car_Details)
                    else:
                        print('\n|!!! Please put suitable values !!!|')
                        continue

# Initializing Login Class
class Login:
    
    # Initializing Class Atributes
    def __init__(self, main):
        Login.USERNAME = 'u'
        Login.EMAIL = 'e'
        Login.PASSWORD = 'p'
        Login.user_validation = False
        Login.admin_validation = False
        Login.main = main
        Login.update_car = False
        Login.car_viewed = False
        Login.from_payment = False
        Login.from_admin = False
        Login.car_selected = False

        # Reading Car Details Class attributes and properties
        _car_details = Car_Details()

        # IF user is coming from admin then display car details
        if Login.main.from_menu:
            _car_details.display_car()

    # Function for ADMIN VALIDATION
    def admin(self):
        while True:
            # PRINTING WELCOME MESSAGE
            print('\n\n|---------------------------------------|')
            print('|>>> WELCOME TO LOGIN PAGE FOR ADMIN <<<|')
            print('|---------------------------------------|')
            # ASKING ADMIN TO ENTER USERNAME AND EAMIL ADDRESS
            self.username = input('\nEnter admin username: ')
            self.email = input('Enter admin email address: ')

            file = open('admin.txt', 'r')
    
            for line in file.readlines():
                if line == f'Username: {self.username}' + '\n': self.USERNAME = self.username
                elif line == f'Email: {self.email}' : self.EMAIL = self.email
                
            file.close()

            # CHECKING IF USERNAME AND PASSWORD ARE CORRECT THEN ASK TO ENTER PASSWORD
            try:
                if (self.username == self.USERNAME) and (self.email == self.EMAIL):
                
                    while True:
                        print('\n|--- Email and Username are correct. Now put your password ---|')
                        self.password = input('\nEnter your password: ')
                    
                        file = open('admin.txt', 'r')
                        try:
                            for line in file.readlines():
                                if (line == f'Password: {self.password}' + '\n'): 
                                    self.PASSWORD = self.password
                                    print('\n|--- Your Email and Password are correct ---|')
                                    break
                            else:
                                print('\n|!!! Sorry your password is not correct !!!|')
                                continue
                            break
                        except:
                            break
                    break
                raise os.error
            # IF THE USERNAME OR EMAIL IS NOT CORRECT THEN PRINT THE MESSAGE AND ASK AGAIN TO ENTER
            except:
                print('\n|!!! Please enter correct username or email !!!|')
                continue

        # GIVING ADMIN ACCESS TO DASHBOARD
        Login.admin_validation = True
        # DENYING ACCESS TO REGISTERED USER TO ACCESS MENU
        Login.user_validation = False
        Login.menu_admin(Login)

    # FUNCTION for ADMIN DASHBOARD
    def menu_admin(self):
        # SHOWING THE ADMIN DASHBOARD ONLY WHEN ADMIN IS LOGGED IN ONLY
        if Login.admin_validation and not (Login.user_validation):
            # PRINTING THE WELCOME MESSAGE
            print('\n|----------------------------------|')
            print('|>>> WELCOME TO ADMIN DASHBOARD <<<|')
            print('|----------------------------------|')
            # ASKING ADMIN TO ENTER THE CHOICE
            user_choice = input('''
            1. Logout from the system
            2. Add car with details to be rented out
            3. Modify car details
            4. Display all records of:
                (a) - Cars available for rent
                (b) - Customer payment for a specific time duration
            5. Search specific records of:
                (a) - Specific car booking
                (b) - Specific customer payment
            6. Return a rented car
            7. Exit --> ''')

            # IF THE admin choice is 1 then Logout from the system
            if user_choice == '1':
                Login.main.from_menu = False
                Login.admin_validation = False
                Login.main.login(Login)

            # IF THE admin choice is 2 then showing the available cars to admin
            elif user_choice == '2':
                Login.add_car(Login)
            
            # IF THE admin choice is 3 then let the admin modify car details
            elif user_choice == '3':
                Login.car_viewed = False
                Login.update_car = True
                Car_Details.display_car(Car_Details)

            # IF THE admin choice is 4 then show another menu screen to admin and let admin decide whether admin wants to display cars available for rent or customer payment for a specific duration
            elif user_choice == '4':
                while True:
                    display_choice = input('''
    A. Cars Available for rent
    B. Customer Payment for a specific duration 
    C. Exit--> ''').upper()
                    # IF ADMIN choice is A then DISPLAY ADMIN AVAILABLE CARS TO RENT
                    if display_choice == 'A':
                        Login.from_admin = True
                        Car_Details.display_car(Car_Details)
                    # IF ADMIN choice is B then DISPLAY CUSTOMER PAYMENT RECORDS
                    elif display_choice == 'B':
                        # IF THERE IS NO RENTAL HISTORY
                        if not (os.listdir('Rental_History')):
                            print('\n|--- Sorry you have to rent a car because there are no cars rented ---|')
                            print('\n|--- You have to login as a registered user first ---|')
                            while True:
                                _ask = input('\nDo you want to login as a registered user? (YES) or (NO): ').upper()
                                if _ask == 'YES':
                                    Login.admin_validation = False
                                    Login.registered_user(Login)
                                elif _ask == 'NO':
                                    print('\n|--- Going back to ADMIN DASHBOARD ---|')
                                    Login.menu_admin(Login)
                                else:
                                    print('\n|!!! Please put suitable values !!!|')
                                    continue

                        # IF THERE IS RENTAL HISTORY THEN PRINTING THE CUSTOMER RECORDS
                        print('\n')
                        print('      ------------------------------------------------------------------------------------------------------------')
                        print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CUSTOMER PAYMENT DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                        print('      ------------------------------------------------------------------------------------------------------------')
                        print('      ============================================================================================================')
                        print('      %-17s %-18s %-17s %-16s %-17s %-17s|' %('| USERNAME', ' | COMPANY', ' | MODEL', ' | YEAR', ' | DURATION', ' | COST'))
                        print('      ============================================================================================================')
                        for idx, files in enumerate(os.listdir('Rental_History')):
                            with open(f'Rental_History\\{files}', 'r') as f:
                                for customer_payment_line in f.readlines():
                                    if '\n' in customer_payment_line: customer_payment_line = customer_payment_line.replace('\n', '')
                        
                                    customer_payment_details = customer_payment_line.split(' | ')
                                    USERNAME = customer_payment_details[0]
                                    COMPANY = customer_payment_details[1]
                                    MODEL = customer_payment_details[2]
                                    YEAR = customer_payment_details[3]
                                    DURATION = customer_payment_details[5]
                                    COST = customer_payment_details[9]

                                    print(f'({idx + 1}) = %-17s %-18s %-17s %-16s %-17s %-17s|' %('| ' + USERNAME, ' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + DURATION, ' | ' + COST))

                            print('      ============================================================================================================')
                        
                        # ASKING ADMIN TO GO BACK 
                        while True:
                            admin_choice = input('\nDo you want to go back? (YES): ').upper()
                            if admin_choice == 'YES':
                                Login.menu_admin(Login)
                            else:
                                print('\n|!!! Please put suitable values !!!|')
                                continue
                    # IF THE admin choice is C then go back to ADMIN DASHBOARD
                    elif display_choice == 'C':
                        print('\n|--- Going back to ADMIN DASHBOARD ---|')
                        Login.menu_admin(Login)
                    # IF THE admin choice is not from above then print error message and ask again
                    else:
                        print('\n|!!! Please put suitable values !!!|')
                        continue

            # IF THE admin choice is 5 then show another menu screen to admin and let admin decide whether admin wants to search for specific car booking or specific customer payment    
            elif user_choice == '5':
                while True:
                    search_choice = input('''
    A. Specific Car Booking
    B. Specific Customer Payment 
    C. Exit --> ''').upper()
                    # IF admin choice is A then search for specific car booking
                    if search_choice == 'A':
                        # Store rented cars in a list
                        self.rented_car_files = os.listdir('Rented_Cars')
                        while True:
                            # ENTER search results
                            search_by = input('''
How do you want to search by: 
(COMPANY) or (MODEL) or (YEAR) or (COLOR) or (DURATION) or (CAR MECHANICS) or (WITH DRIVER) or (SEATS) or (COST) or (MILEAGE) or (EXIT): ''').upper()
                            # IF COMPANY is selected then search by COMPANY
                            if search_by == 'COMPANY':
                                ask_company = input('\nEnter company name to search for: ').upper()
                            
                                company_history_files = []
                                for company_files in self.rented_car_files:
                                    with open(f'Rented_Cars\\{company_files}', 'r') as f:
                                        for line in f.readlines():
                                            content = line.split(' | ')
                                            if ask_company == content[0]:
                                                company_history_files.append(company_files)
                                if company_history_files:
                                    print('\n')
                                    print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                    print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CAR DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                                    print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                    print('      ====================================================================================================================================================')
                                    print('      %-13s %-21s %-10s %-15s %-15s %-14s %-17s %-11s %-11s %-9s' %(' | COMPANY', '| MODEL', '| YEAR', '| COLOR', '| DURATION', '| CAR MECHANICS', '| WITH DRIVER', '| SEATS', '| COST', '| MILEAGE |'))
                                    print('      ====================================================================================================================================================')

                                else:
                                    print('\n|--- Sorry there are no cars here according to Company name ---|')
                                    print('\n|--- Returning to Search by Screen ---|')
                                    continue

                                for idx, file_names in enumerate(company_history_files):
                                    with open(f'Rented_Cars\\{file_names}', 'r') as f:
                                        for file_content_line in f.readlines():
                                            file_content = file_content_line.split(' | ')
                                            if ask_company == file_content[0]:
                                                COMPANY = file_content[0]
                                                MODEL = file_content[1]
                                                YEAR = file_content[2]
                                                COLOR = file_content[3]
                                                DURATION = file_content[4]
                                                CAR_MECHANICS = file_content[5]
                                                WITH_DRIVER = file_content[6]
                                                SEATS = file_content[7]
                                                COST = file_content[8]
                                                MILEAGE = file_content[9]

                                                if idx < 9:
                                                    print(f'({idx + 1}) = %-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))
                                                else:
                                                    print(f'({idx + 1}) =%-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))

                                            else:
                                                break

                                        if ask_company == file_content[0]:
                                            print('      ====================================================================================================================================================')


                                while True:     
                                    ask_again = input('\nDo you want to go back? (YES) or (NO): ').upper()
                                    if ask_again == 'YES': break
                                    elif ask_again == 'NO': break
                                    else:
                                        print('\n|!!! Please put suitable values !!!|')
                                        continue
                                if ask_again == 'YES': break
                                elif ask_again == 'NO': continue

                                continue

                            # IF MODEL is selected then search by MODEL
                            elif search_by == 'MODEL':
                                ask_model = input('\nEnter company name to search for: ').upper()
                            
                                model_history_files = []
                                for model_files in self.rented_car_files:
                                    with open(f'Rented_Cars\\{model_files}', 'r') as f:
                                        for line in f.readlines():
                                            content = line.split(' | ')
                                            if ask_model == content[1]:
                                                model_history_files.append(model_files)
                                if model_history_files:
                                    print('\n')
                                    print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                    print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CAR DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                                    print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                    print('      ====================================================================================================================================================')
                                    print('      %-13s %-21s %-10s %-15s %-15s %-14s %-17s %-11s %-11s %-9s' %(' | COMPANY', '| MODEL', '| YEAR', '| COLOR', '| DURATION', '| CAR MECHANICS', '| WITH DRIVER', '| SEATS', '| COST', '| MILEAGE |'))
                                    print('      ====================================================================================================================================================')

                                else:
                                    print('\n|--- Sorry there are no cars here according to Car Model name ---|')
                                    print('\n|--- Returning to Search by Screen ---|')
                                    continue

                                for idx, file_names in enumerate(model_history_files):
                                    with open(f'Rented_Cars\\{file_names}', 'r') as f:
                                        for file_content_line in f.readlines():
                                            file_content = file_content_line.split(' | ')
                                            if ask_model == file_content[1]:
                                                COMPANY = file_content[0]
                                                MODEL = file_content[1]
                                                YEAR = file_content[2]
                                                COLOR = file_content[3]
                                                DURATION = file_content[4]
                                                CAR_MECHANICS = file_content[5]
                                                WITH_DRIVER = file_content[6]
                                                SEATS = file_content[7]
                                                COST = file_content[8]
                                                MILEAGE = file_content[9]

                                                if idx < 9:
                                                    print(f'({idx + 1}) = %-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))
                                                else:
                                                    print(f'({idx + 1}) =%-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))

                                            else:
                                                break

                                        if ask_model == file_content[1]:
                                            print('      ====================================================================================================================================================')


                                while True:     
                                    ask_again = input('\nDo you want to go back? (YES) or (NO): ').upper()
                                    if ask_again == 'YES': break
                                    elif ask_again == 'NO': break
                                    else:
                                        print('\n|!!! Please put suitable values !!!|')
                                        continue
                                if ask_again == 'YES': break
                                elif ask_again == 'NO': continue

                                continue

                            # IF YEAR is selected then search by YEAR
                            elif search_by == 'YEAR':
                                while True:
                                    try:
                                        ask_year = int(input('\nEnter year to search for: '))
                                    except:
                                        print('\n|!!! Please put in numbers !!!|')
                                        continue

                                    year_history_files = []
                                    for year_files in self.rented_car_files:
                                        with open(f'Rented_Cars\\{year_files}', 'r') as f:
                                            for line in f.readlines():
                                                content = line.split(' | ')
                                                if str(ask_year) == content[2]:
                                                    year_history_files.append(year_files)

                                    if year_history_files:
                                        print('\n')
                                        print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                        print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CAR DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                                        print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                        print('      ====================================================================================================================================================')
                                        print('      %-13s %-21s %-10s %-15s %-15s %-14s %-17s %-11s %-11s %-9s' %(' | COMPANY', '| MODEL', '| YEAR', '| COLOR', '| DURATION', '| CAR MECHANICS', '| WITH DRIVER', '| SEATS', '| COST', '| MILEAGE |'))
                                        print('      ====================================================================================================================================================')

                                    else:
                                        print('\n|--- Sorry there are no cars here according to Year ---|')
                                        print('\n|--- Returning to Search by Screen ---|')
                                        self.return_search_by = True

                                    for idx, file_names in enumerate(year_history_files):
                                        with open(f'Rented_Cars\\{file_names}', 'r') as f:
                                            for file_content_line in f.readlines():
                                                file_content = file_content_line.split(' | ')
                                                if str(ask_year) == file_content[2]:
                                                    COMPANY = file_content[0]
                                                    MODEL = file_content[1]
                                                    YEAR = file_content[2]
                                                    COLOR = file_content[3]
                                                    DURATION = file_content[4]
                                                    CAR_MECHANICS = file_content[5]
                                                    WITH_DRIVER = file_content[6]
                                                    SEATS = file_content[7]
                                                    COST = file_content[8]
                                                    MILEAGE = file_content[9]

                                                    if idx < 9:
                                                        print(f'({idx + 1}) = %-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))
                                                    else:
                                                        print(f'({idx + 1}) =%-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))

                                                else:
                                                    break

                                            if str(ask_year) == file_content[2]:
                                                print('      ====================================================================================================================================================')
                                    
                                    try:
                                        if self.return_search_by: break
                                    except:
                                        pass

                                    while True:     
                                        ask_again = input('\nDo you want to go back? (YES) or (NO): ').upper()
                                        if ask_again == 'YES': break
                                        elif ask_again == 'NO': break
                                        else:
                                            print('\n|!!! Please put suitable values !!!')
                                            continue
                                        
                                try:
                                    if self.return_search_by: 
                                        self.return_search_by = False
                                        continue
                                except:
                                    pass

                                if ask_again == 'YES': break
                                elif ask_again == 'NO': continue

                                continue

                            # IF COLOR is selected then search by COLOR
                            elif search_by == 'COLOR':
                                ask_color = input('\nEnter color to search for: ').upper()
                            
                                color_history_files = []
                                for color_files in self.rented_car_files:
                                    with open(f'Rented_Cars\\{color_files}', 'r') as f:
                                        for line in f.readlines():
                                            content = line.split(' | ')
                                            if ask_color == content[3]:
                                                color_history_files.append(color_files)
                                if color_history_files:
                                    print('\n')
                                    print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                    print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CAR DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                                    print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                    print('      ====================================================================================================================================================')
                                    print('      %-13s %-21s %-10s %-15s %-15s %-14s %-17s %-11s %-11s %-9s' %(' | COMPANY', '| MODEL', '| YEAR', '| COLOR', '| DURATION', '| CAR MECHANICS', '| WITH DRIVER', '| SEATS', '| COST', '| MILEAGE |'))
                                    print('      ====================================================================================================================================================')

                                else:
                                    print('\n|--- Sorry there are no cars here according to Color ---|')
                                    print('\n|--- Returning to Search by Screen ---|')
                                    continue

                                for idx, file_names in enumerate(color_history_files):
                                    with open(f'Rented_Cars\\{file_names}', 'r') as f:
                                        for file_content_line in f.readlines():
                                            file_content = file_content_line.split(' | ')
                                            if ask_color == file_content[3]:
                                                COMPANY = file_content[0]
                                                MODEL = file_content[1]
                                                YEAR = file_content[2]
                                                COLOR = file_content[3]
                                                DURATION = file_content[4]
                                                CAR_MECHANICS = file_content[5]
                                                WITH_DRIVER = file_content[6]
                                                SEATS = file_content[7]
                                                COST = file_content[8]
                                                MILEAGE = file_content[9]

                                                if idx < 9:
                                                    print(f'({idx + 1}) = %-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))
                                                else:
                                                    print(f'({idx + 1}) =%-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))

                                            else:
                                                break

                                        if ask_color == file_content[3]:
                                            print('      ====================================================================================================================================================')


                                while True:     
                                    ask_again = input('\nDo you want to go back? (YES) or (NO): ').upper()
                                    if ask_again == 'YES': break
                                    elif ask_again == 'NO': break
                                    else:
                                        print('\n|!!! Please put suitable values !!!|')
                                        continue
                                if ask_again == 'YES': break
                                elif ask_again == 'NO': continue

                                continue

                            # IF DURATION is selected then search by DURATION
                            elif search_by == 'DURATION':
                                while True:
                                    ask_duration = input('\nEnter duration detials (FULL DAY) or (HALF DAY) to search for: ').upper()
                                    if ask_duration == 'FULL DAY' or ask_duration == 'HALF DAY':
                                        ask_duration = ask_duration
                                    else:
                                        print('\n|!!! Please suitable values !!!|')
                                        continue

                                    duration_history_files = []
                                    for duration_files in self.rented_car_files:
                                        with open(f'Rented_Cars\\{duration_files}', 'r') as f:
                                            for line in f.readlines():
                                                content = line.split(' | ')
                                                if ask_duration == content[4]:
                                                    duration_history_files.append(duration_files)

                                    if duration_history_files:
                                        print('\n')
                                        print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                        print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CAR DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                                        print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                        print('      ====================================================================================================================================================')
                                        print('      %-13s %-21s %-10s %-15s %-15s %-14s %-17s %-11s %-11s %-9s' %(' | COMPANY', '| MODEL', '| YEAR', '| COLOR', '| DURATION', '| CAR MECHANICS', '| WITH DRIVER', '| SEATS', '| COST', '| MILEAGE |'))
                                        print('      ====================================================================================================================================================')

                                    else:
                                        print('\n|--- Sorry there are no cars here according to Duration details ---|')
                                        print('\n|--- Returning to Search by Screen ---|')
                                        self.return_search_by = True

                                    for idx, file_names in enumerate(duration_history_files):
                                        with open(f'Rented_Cars\\{file_names}', 'r') as f:
                                            for file_content_line in f.readlines():
                                                file_content = file_content_line.split(' | ')
                                                if ask_duration == file_content[4]:
                                                    COMPANY = file_content[0]
                                                    MODEL = file_content[1]
                                                    YEAR = file_content[2]
                                                    COLOR = file_content[3]
                                                    DURATION = file_content[4]
                                                    CAR_MECHANICS = file_content[5]
                                                    WITH_DRIVER = file_content[6]
                                                    SEATS = file_content[7]
                                                    COST = file_content[8]
                                                    MILEAGE = file_content[9]

                                                    if idx < 9:
                                                        print(f'({idx + 1}) = %-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))
                                                    else:
                                                        print(f'({idx + 1}) =%-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))

                                                else:
                                                    break
                                            if ask_duration == file_content[4]:

                                                print('      ====================================================================================================================================================')


                                    try:
                                        if self.return_search_by: break
                                    except:
                                        pass

                                    while True:     
                                        ask_again = input('\nDo you want to go back? (YES) or (NO): ').upper()
                                        if ask_again == 'YES': break
                                        elif ask_again == 'NO': break
                                        else:
                                            print('\n|!!! Please put suitable values !!!|')
                                            continue
                                        
                                try:
                                    if self.return_search_by: 
                                        self.return_search_by = False
                                        continue
                                except:
                                    pass

                                if ask_again == 'YES': break
                                elif ask_again == 'NO': continue

                                continue

                            # IF CAR MECHANICS is selected then search by CAR MECHANICS
                            elif search_by == 'CAR MECHANICS':
                                while True:
                                    ask_car_mechanics = input('\nEnter car mechanics to search for (AUTO) or (MANUAL): ').upper()
                                    if ask_car_mechanics == 'AUTO' or ask_car_mechanics == 'MANUAL':
                                        ask_car_mechanics = ask_car_mechanics
                                    else:
                                        print('\n|!!! Please put car mechanics !!!|')
                                        continue
                                    
                                    car_mechanics_rented_files = []
                                    for car_mechanics_files in self.rented_car_files:
                                        with open(f'Rented_Cars\\{car_mechanics_files}', 'r') as f:
                                            for line in f.readlines():
                                                content = line.split(' | ')
                                                if ask_car_mechanics == content[5]:
                                                    car_mechanics_rented_files.append(car_mechanics_files)

                                    if car_mechanics_rented_files:
                                        print('\n')
                                        print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                        print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CAR DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                                        print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                        print('      ====================================================================================================================================================')
                                        print('      %-13s %-21s %-10s %-15s %-15s %-14s %-17s %-11s %-11s %-9s' %(' | COMPANY', '| MODEL', '| YEAR', '| COLOR', '| DURATION', '| CAR MECHANICS', '| WITH DRIVER', '| SEATS', '| COST', '| MILEAGE |'))
                                        print('      ====================================================================================================================================================')

                                    else:
                                        print('\n|--- Sorry there are no cars here according to car mechanics ---|')
                                        print('\n|--- Returning to Search by Screen ---|')
                                        self.return_search_by = True

                                    for idx, file_names in enumerate(car_mechanics_rented_files):
                                        with open(f'Rented_Cars\\{file_names}', 'r') as f:
                                            for file_content_line in f.readlines():
                                                file_content = file_content_line.split(' | ')
                                                if ask_car_mechanics == file_content[5]:
                                                    COMPANY = file_content[5]
                                                    MODEL = file_content[1]
                                                    YEAR = file_content[2]
                                                    COLOR = file_content[3]
                                                    DURATION = file_content[4]
                                                    CAR_MECHANICS = file_content[5]
                                                    WITH_DRIVER = file_content[6]
                                                    SEATS = file_content[7]
                                                    COST = file_content[8]
                                                    MILEAGE = file_content[9]

                                                    if idx < 9:
                                                        print(f'({idx + 1}) = %-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))
                                                    else:
                                                        print(f'({idx + 1}) =%-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))

                                                else:
                                                    break
                                            if ask_car_mechanics == file_content[5]:

                                                print('      ====================================================================================================================================================')

                                    try:
                                        if self.return_search_by: break
                                    except:
                                        pass

                                    while True:     
                                        ask_again = input('\nDo you want to go back? (YES) or (NO): ').upper()
                                        if ask_again == 'YES': break
                                        elif ask_again == 'NO': break
                                        else:
                                            print('\n|!!! Please put suitable values !!!|')
                                            continue
                                        
                                try:
                                    if self.return_search_by: 
                                        self.return_search_by = False
                                        continue
                                except:
                                    pass

                                if ask_again == 'YES': break
                                elif ask_again == 'NO': continue

                                continue
                            
                            # IF WITH DRIVER is selected then search by WITH DRIVER
                            elif search_by == 'WITH DRIVER':
                                while True:
                                    ask_with_driver = input('\nEnter driver availibility to search for (YES) or (NO): ').upper()
                                    if ask_with_driver == 'YES' or ask_with_driver == 'NO':
                                        ask_with_driver = ask_with_driver
                                    else:
                                        print('\n|!!! Please put driver availibility !!!|')
                                        continue

                                    with_driver_history_files = []
                                    for with_driver_files in self.rented_car_files:
                                        with open(f'Rented_Cars\\{with_driver_files}', 'r') as f:
                                            for line in f.readlines():
                                                content = line.split(' | ')
                                                if ask_with_driver == content[6]:
                                                    with_driver_history_files.append(with_driver_files)

                                    if with_driver_history_files:
                                        print('\n')
                                        print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                        print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CAR DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                                        print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                        print('      ====================================================================================================================================================')
                                        print('      %-13s %-21s %-10s %-15s %-15s %-14s %-17s %-11s %-11s %-9s' %(' | COMPANY', '| MODEL', '| YEAR', '| COLOR', '| DURATION', '| CAR MECHANICS', '| WITH DRIVER', '| SEATS', '| COST', '| MILEAGE |'))
                                        print('      ====================================================================================================================================================')

                                    else:
                                        print('\n|--- Sorry there are no cars here according to Driver availibility ---|')
                                        print('\n|--- Returning to Search by Screen ---|')
                                        self.return_search_by = True

                                    for idx, file_names in enumerate(with_driver_history_files):
                                        with open(f'Rented_Cars\\{file_names}', 'r') as f:
                                            for file_content_line in f.readlines():
                                                file_content = file_content_line.split(' | ')
                                                if ask_with_driver == file_content[6]:
                                                    COMPANY = file_content[0]
                                                    MODEL = file_content[1]
                                                    YEAR = file_content[2]
                                                    COLOR = file_content[3]
                                                    DURATION = file_content[4]
                                                    CAR_MECHANICS = file_content[5]
                                                    WITH_DRIVER = file_content[6]
                                                    SEATS = file_content[7]
                                                    COST = file_content[8]
                                                    MILEAGE = file_content[9]

                                                    if idx < 9:
                                                        print(f'({idx + 1}) = %-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))
                                                    else:
                                                        print(f'({idx + 1}) =%-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))

                                                else:
                                                    break
                                            if ask_with_driver == file_content[6]:

                                                print('      ====================================================================================================================================================')


                                    try:
                                        if self.return_search_by: break
                                    except:
                                        pass

                                    while True:     
                                        ask_again = input('\nDo you want to go back? (YES) or (NO): ').upper()
                                        if ask_again == 'YES': break
                                        elif ask_again == 'NO': break
                                        else:
                                            print('\n|!!! Please put suitable values !!!|')
                                            continue
                                        
                                try:
                                    if self.return_search_by: 
                                        self.return_search_by = False
                                        continue
                                except:
                                    pass

                                if ask_again == 'YES': break
                                elif ask_again == 'NO': continue

                                continue

                            # IF SEATS is selected then search by SEATS
                            elif search_by == 'SEATS':
                                while True:
                                    try:
                                        while True:
                                            ask_seats = int(input('\nEnter year to search for (2) or (4) or (6) or (8) or (16): '))
                                            if ask_seats == 2 or ask_seats == 4 or ask_seats == 6 or ask_seats == 8 or ask_seats == 16:
                                                ask_seats = ask_seats
                                                break
                                            else:
                                                print('\n|!!! Please put numbers accordingly !!!|')
                                                continue
                                    except:
                                        print('\n|!!! Please put in numbers !!!|')
                                        continue

                                    finally:
                                        ask_seats_files = []
                                        for seats_files in self.rented_car_files:
                                            with open(f'Rented_Cars\\{seats_files}', 'r') as f:
                                                for line in f.readlines():
                                                    content = line.split(' | ')
                                                    if str(ask_seats) == content[7]:
                                                        ask_seats_files.append(seats_files)

                                        if ask_seats_files:
                                            print('\n')
                                            print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                            print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CAR DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                                            print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                            print('      ====================================================================================================================================================')
                                            print('      %-13s %-21s %-10s %-15s %-15s %-14s %-17s %-11s %-11s %-9s' %(' | COMPANY', '| MODEL', '| YEAR', '| COLOR', '| DURATION', '| CAR MECHANICS', '| WITH DRIVER', '| SEATS', '| COST', '| MILEAGE |'))
                                            print('      ====================================================================================================================================================')

                                        else:
                                            print('\n|--- Sorry there are no cars here according to seats ---|')
                                            print('\n|--- Returning to Search by Screen ---|')
                                            self.return_search_by = True

                                        for idx, file_names in enumerate(ask_seats_files):
                                            with open(f'Rented_Cars\\{file_names}', 'r') as f:
                                                for file_content_line in f.readlines():
                                                    file_content = file_content_line.split(' | ')
                                                    if str(ask_seats) == file_content[7]:
                                                        COMPANY = file_content[0]
                                                        MODEL = file_content[1]
                                                        YEAR = file_content[2]
                                                        COLOR = file_content[3]
                                                        DURATION = file_content[4]
                                                        CAR_MECHANICS = file_content[5]
                                                        WITH_DRIVER = file_content[6]
                                                        SEATS = file_content[7]
                                                        COST = file_content[8]
                                                        MILEAGE = file_content[9]

                                                        if idx < 9:
                                                            print(f'({idx + 1}) = %-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))
                                                        else:
                                                            print(f'({idx + 1}) =%-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))

                                                    else:
                                                        break
                                                if str(ask_seats) == file_content[7]:

                                                    print('      ====================================================================================================================================================')


                                        try:
                                            if self.return_search_by: break
                                        except:
                                            pass

                                    while True:     
                                        ask_again = input('\nDo you want to go back? (YES) or (NO): ').upper()
                                        if ask_again == 'YES': break
                                        elif ask_again == 'NO': break
                                        else:
                                            print('\n|!!! Please put suitable values !!!|')
                                            continue
                                        
                                try:
                                    if self.return_search_by: 
                                        self.return_search_by = False
                                        continue
                                except:
                                    pass

                                if ask_again == 'YES': break
                                elif ask_again == 'NO': continue

                                continue

                            # IF COST is selected then search by COST
                            elif search_by == 'COST':
                                while True:
                                    
                                    try:
                                        min_cost = int(input('\nEnter minimum cost amount to search for (MUST BE IN NUMBERS): '))
                                        max_cost = int(input('\nEnter maximum cost amount to search for (MUST BE IN NUMBERS): '))
                                    except:
                                        print('\n|!!! Please put number values !!!|')
                                        continue
                                    
                                    cost_rented_files = []
                                    for cost_files in self.rented_car_files:
                                        with open(f'Rented_Cars\\{cost_files}', 'r') as f:
                                            for line in f.readlines():
                                                content = line.split(' | ')
                                                if min_cost <= int(content[8]) and max_cost >= int(content[8]):
                                                    cost_rented_files.append(cost_files)
                                    
                                    if cost_rented_files:
                                        print('\n')
                                        print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                        print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CAR DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                                        print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                        print('      ====================================================================================================================================================')
                                        print('      %-13s %-21s %-10s %-15s %-15s %-14s %-17s %-11s %-11s %-9s' %(' | COMPANY', '| MODEL', '| YEAR', '| COLOR', '| DURATION', '| CAR MECHANICS', '| WITH DRIVER', '| SEATS', '| COST', '| MILEAGE |'))
                                        print('      ====================================================================================================================================================')
                                    
                                    else:
                                        print('\n|--- Sorry there are no customer payment record according to amount of cost ---|')
                                        print('\n|--- Returning to Search by Screen ---|')
                                        self.return_search_by = True
                                        break

                                    for idx, file_names in enumerate(cost_rented_files):
                                        with open(f'Rented_Cars\\{file_names}', 'r') as f:
                                            for file_content_line in f.readlines():
                                                file_content = file_content_line.split(' | ')
                                                if min_cost <= int(file_content[8]) and max_cost >= int(file_content[9]):
                                                    COMPANY = file_content[0]
                                                    MODEL = file_content[1]
                                                    YEAR = file_content[2]
                                                    COLOR = file_content[3]
                                                    DURATION = file_content[4]
                                                    CAR_MECHANICS = file_content[5]
                                                    WITH_DRIVER = file_content[6]
                                                    SEATS = file_content[7]
                                                    COST = file_content[8]
                                                    MILEAGE = file_content[9]

                                                    if idx < 9:
                                                        print(f'({idx + 1}) = %-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))
                                                    else:
                                                        print(f'({idx + 1}) =%-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))

                                                else:
                                                    break
                                            if min_cost <= int(file_content[8]) and max_cost >= int(file_content[8]):
                                                print('      ====================================================================================================================================================')
                                    while True:     
                                        ask_again = input('\nDo you want to go back? (YES) or (NO): ').upper()
                                        if ask_again == 'YES': break
                                        elif ask_again == 'NO': break
                                        else:
                                            print('\n|!!! Please put suitable values !!!|')
                                            continue
                                    break
                                try:
                                    if self.return_search_by: 
                                        self.return_search_by = False
                                        continue
                                except: pass
                                if ask_again == 'YES': break
                                elif ask_again == 'NO': continue

                                continue

                            # IF MILEAGE is selected then search by MILEAGE
                            elif search_by == 'MILEAGE':
                                while True:
                                    try:
                                        ask_mileage = int(input('\nEnter mileage amount to search for: '))
                                    except:
                                        print('\n|!!! Please put in numbers !!!|')
                                        continue

                                    mileage_history_files = []
                                    for mileage_files in self.rented_car_files:
                                        with open(f'Rented_Cars\\{mileage_files}', 'r') as f:
                                            for line in f.readlines():
                                                content = line.split(' | ')
                                                if str(ask_mileage) == content[9]:
                                                    mileage_history_files.append(mileage_files)

                                    if mileage_history_files:
                                        print('\n')
                                        print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                        print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CAR DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                                        print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                                        print('      ====================================================================================================================================================')
                                        print('      %-13s %-21s %-10s %-15s %-15s %-14s %-17s %-11s %-11s %-9s' %(' | COMPANY', '| MODEL', '| YEAR', '| COLOR', '| DURATION', '| CAR MECHANICS', '| WITH DRIVER', '| SEATS', '| COST', '| MILEAGE |'))
                                        print('      ====================================================================================================================================================')

                                    else:
                                        print('\n|--- Sorry there are no cars here according to the Mileage amount ---|')
                                        print('\n|--- Returning to Search by Screen ---|')
                                        self.return_search_by = True

                                    for idx, file_names in enumerate(mileage_history_files):
                                        with open(f'Rented_Cars\\{file_names}', 'r') as f:
                                            for file_content_line in f.readlines():
                                                file_content = file_content_line.split(' | ')
                                                if str(ask_mileage) == file_content[9]:
                                                    COMPANY = file_content[0]
                                                    MODEL = file_content[1]
                                                    YEAR = file_content[2]
                                                    COLOR = file_content[3]
                                                    DURATION = file_content[4]
                                                    CAR_MECHANICS = file_content[5]
                                                    WITH_DRIVER = file_content[6]
                                                    SEATS = file_content[7]
                                                    COST = file_content[8]
                                                    MILEAGE = file_content[9]

                                                    if idx < 9:
                                                        print(f'({idx + 1}) = %-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))
                                                    else:
                                                        print(f'({idx + 1}) =%-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))

                                                else:
                                                    break
                                            if str(ask_mileage) == file_content[9]:

                                                print('      ====================================================================================================================================================')


                                    try:
                                        if self.return_search_by: break
                                    except:
                                        pass

                                    while True:     
                                        ask_again = input('\nDo you want to go back? (YES) or (NO): ').upper()
                                        if ask_again == 'YES': break
                                        elif ask_again == 'NO': break
                                        else:
                                            print('\n|!!! Please put suitable values !!!|')
                                            continue
                                        
                                try:
                                    if self.return_search_by: 
                                        self.return_search_by = False
                                        continue
                                except:
                                    pass

                                if ask_again == 'YES': break
                                elif ask_again == 'NO': continue

                                continue

                            # IF EXIT is selected then search by EXIT
                            elif search_by == 'EXIT':
                                print('\n|--- Going back to ADMIN DASHBOARD ---|')
                                Login.menu_admin(Login)

                            # IF EXIT is selected then exit to SEARCH BY SCREEN
                            else:
                                print('\n|!!! Please put suitable values from below !!!|')
                                continue

                    elif search_choice == 'B':
                        
                        # STORE rental history files
                        self.rental_history_files = os.listdir('Rental_History')
                        while True:
                            search_by = input('''
How do you want to search by: (USERNAME) or (DURATION) or (COST) or (EXIT): ''').upper()
                            # IF search by is USERNAME 
                            if search_by == 'USERNAME':

                                ask_username = input('\nEnter username to search for: ').lower()
                                                             
                                username_history_files = []
                                for username_files in self.rental_history_files:
                                    with open(f'Rental_History\\{username_files}', 'r') as f:
                                        for line in f.readlines():
                                            content = line.split(' | ')
                                            if ask_username == content[0]:
                                                username_history_files.append(username_files)
                                
                                if username_history_files:
                                    print('\n')
                                    print('      ------------------------------------------------------------------------------------------------------------')
                                    print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CUSTOMER PAYMENT DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                                    print('      ------------------------------------------------------------------------------------------------------------')
                                    print('      ============================================================================================================')
                                    print('      %-17s %-18s %-17s %-16s %-17s %-17s|' %('| USERNAME', ' | COMPANY', ' | MODEL', ' | YEAR', ' | DURATION', ' | COST'))
                                    print('      ============================================================================================================')
                                else:
                                    print('\n|--- Sorry there are no customer payment record here according to username ---|')
                                    print('\n|--- Returning to Search by Screen ---|')
                                    continue


                                for idx, file_names in enumerate(username_history_files):
                                    with open(f'Rental_History\\{file_names}', 'r') as f:
                                        for file_content_line in f.readlines():
                                            file_content = file_content_line.split(' | ')
                                            if ask_username == file_content[0]:
                                                USERNAME = file_content[0]
                                                COMPANY = file_content[1]
                                                MODEL = file_content[2]
                                                YEAR = file_content[3]
                                                DURATION = file_content[5]
                                                COST = file_content[9]

                                                print(f'({idx + 1}) = %-17s %-18s %-17s %-16s %-17s %-17s|' %('| ' + USERNAME, ' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + DURATION, ' | ' + COST))

                                            else:
                                                break
                                        if ask_username == file_content[0]:
                                            print('      ============================================================================================================')
                                while True:     
                                    ask_again = input('\nDo you want to go back? (YES) or (NO): ').upper()
                                    if ask_again == 'YES': break
                                    elif ask_again == 'NO': break
                                    else:
                                        print('\n|!!! Please put suitable values !!!|')
                                        continue
                                if ask_again == 'YES': break
                                elif ask_again == 'NO': continue

                                continue

                            # IF search by is DURATION
                            elif search_by == 'DURATION':
                                while True:
                                    
                                    ask_duration = input('\nEnter duration to search for (FULL DAY) or (HALF DAY): ').upper()
                                    if ask_duration == 'FULL DAY' or ask_duration == 'HALF DAY':
                                        ask_duration = ask_duration
                                    else:
                                        print('\n|!!! Please put suitable values !!!|')
                                        continue
                                    
                                    duration_history_files = []
                                    for duration_files in self.rental_history_files:
                                        with open(f'Rental_History\\{duration_files}', 'r') as f:
                                            for line in f.readlines():
                                                content = line.split(' | ')
                                                if ask_duration == content[5]:
                                                    duration_history_files.append(duration_files)

                                    if duration_history_files:
                                        print('\n')
                                        print('      ------------------------------------------------------------------------------------------------------------')
                                        print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CUSTOMER PAYMENT DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                                        print('      ------------------------------------------------------------------------------------------------------------')
                                        print('      ============================================================================================================')
                                        print('      %-17s %-18s %-17s %-16s %-17s %-17s|' %('| USERNAME', ' | COMPANY', ' | MODEL', ' | YEAR', ' | DURATION', ' | COST'))
                                        print('      ============================================================================================================')
                                    else:
                                        print('\n|--- Sorry there are no customer payment record according to duration ---|')
                                        print('\n|--- Returning to Search by Screen ---|')
                                        self.return_search_by = True

                                    for idx, file_names in enumerate(duration_history_files):
                                        with open(f'Rental_History\\{file_names}', 'r') as f:
                                            for file_content_line in f.readlines():
                                                file_content = file_content_line.split(' | ')
                                                if ask_duration == file_content[5]:
                                                    USERNAME = file_content[0]
                                                    COMPANY = file_content[1]
                                                    MODEL = file_content[2]
                                                    YEAR = file_content[3]
                                                    DURATION = file_content[5]
                                                    COST = file_content[9]

                                                    print(f'({idx + 1}) = %-17s %-18s %-17s %-16s %-17s %-17s|' %('| ' + USERNAME, ' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + DURATION, ' | ' + COST))

                                                else:
                                                    break
                                            if ask_duration == file_content[5]:
                                                print('      ============================================================================================================')
                                    
                                    try:
                                        if self.return_search_by: break
                                    except:
                                        pass

                                    while True:     
                                        ask_again = input('\nDo you want to go back? (YES) or (NO): ').upper()
                                        if ask_again == 'YES': break
                                        elif ask_again == 'NO': break
                                        else:
                                            print('\n|!!! Please put suitable values !!!|')
                                            continue
                                        
                                try:
                                    if self.return_search_by: 
                                        self.return_search_by = False
                                        continue
                                except:
                                    pass

                                if ask_again == 'YES': break
                                elif ask_again == 'NO': continue

                                continue

                            # IF search by is COST    
                            elif search_by == 'COST':
                                while True:
                                    
                                    try:
                                        min_cost = int(input('\nEnter minimum cost amount to search for (MUST BE IN NUMBERS): '))
                                        max_cost = int(input('\nEnter maximum cost amount to search for (MUST BE IN NUMBERS): '))
                                    except:
                                        print('\n|!!! Please put number values !!!|')
                                        continue
                                    
                                    cost_history_files = []
                                    for cost_files in self.rental_history_files:
                                        with open(f'Rental_History\\{cost_files}', 'r') as f:
                                            for line in f.readlines():
                                                content = line.split(' | ')
                                                if min_cost <= int(content[9]) and max_cost >= int(content[9]):
                                                    cost_history_files.append(cost_files)
                                    
                                    if cost_history_files:
                                        print('\n')
                                        print('      ------------------------------------------------------------------------------------------------------------')
                                        print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CUSTOMER PAYMENT DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                                        print('      ------------------------------------------------------------------------------------------------------------')
                                        print('      ============================================================================================================')
                                        print('      %-17s %-18s %-17s %-16s %-17s %-17s|' %('| USERNAME', ' | COMPANY', ' | MODEL', ' | YEAR', ' | DURATION', ' | COST'))
                                        print('      ============================================================================================================')
                                    else:
                                        print('\n|--- Sorry there are no customer payment record according to amount of cost ---|')
                                        print('\n|--- Returning to Search by Screen ---|')
                                        self.return_search_by = True
                                        break

                                    try:
                                        if self.return_search_by:
                                            break
                                    except:
                                        pass

                                    for idx, file_names in enumerate(cost_history_files):
                                        with open(f'Rental_History\\{file_names}', 'r') as f:
                                            for file_content_line in f.readlines():
                                                file_content = file_content_line.split(' | ')
                                                if min_cost <= int(file_content[9]) and max_cost >= int(file_content[9]):
                                                    USERNAME = file_content[0]
                                                    COMPANY = file_content[1]
                                                    MODEL = file_content[2]
                                                    YEAR = file_content[3]
                                                    DURATION = file_content[5]
                                                    COST = file_content[9]
                                                    print(f'({idx + 1}) = %-17s %-18s %-17s %-16s %-17s %-17s|' %('| ' + USERNAME, ' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + DURATION, ' | ' + COST))

                                                else:
                                                    break
                                            if min_cost <= int(file_content[9]) and max_cost >= int(file_content[9]):
                                                print('      ============================================================================================================')
                                    while True:     
                                        ask_again = input('\nDo you want to go back? (YES) or (NO): ').upper()
                                        if ask_again == 'YES': break
                                        elif ask_again == 'NO': break
                                        else:
                                            print('\n|!!! Please put suitable values !!!|')
                                            continue
                                    break
                                try:
                                    if ask_again == 'YES': break
                                    elif ask_again == 'NO': continue
                                except: pass

                                try:
                                    if search_by: continue
                                except: 
                                    pass

                                continue

                            # IF search by is EXIT then to SEARCH BY SCREEN
                            elif search_by == 'EXIT':
                                print('\n|--- Going back to ADMIN DASHBOARD ---|')
                                Login.menu_admin(Login)

                            # IF search by is invalid and not from above then ask again
                            else:
                                print('\n|!!! Please put suitable values !!!|')
                                continue
                            
                    elif search_choice == 'C':
                        print('\n|--- Going back to ADMIN DASHBOARD ---|')
                        Login.menu_admin(Login)
                    else:
                        print('\n|!!! Please put suitable values !!!|')
                        continue

            # IF admin choice is 6 then look for cars that has to be returned to registered cars
            elif user_choice == '6':
                while True:
                    path = "Rented_Cars"
                    now = time.time()
                    rented_files = os.listdir(path)
                    car_to_rent_files = []
                    cars_to_rent_content = []

                    if not (os.listdir(path)):
                        print('\n|--- Sorry there are no rented cars ---|')
                        while True:
                            _ask = input('\nGo back (YES): ').upper()
                            if _ask == 'YES':
                                Login.menu_admin(Login)
                            else:
                                print('\n|!!! Please put suitable values !!!|')
                                continue
                    else:
                        rented_files = os.listdir(path)

                        for filename in rented_files:
                            filestamp = os.stat(os.path.join(path, filename)).st_mtime
                            if 'FULL DAY' in filename:
                                filecompare = now - 36000
                            elif 'HALF DAY' in filename:
                                filecompare = now - 21600

                            if filestamp < filecompare:
                                car_to_rent_files.append(filename)
                                with open(f'Rented_Cars\\{filename}', 'r') as f:
                                    cars_to_rent_content.append(f.read())

                        if car_to_rent_files:
                            print('\n')
                            print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                            print('      |>%-50s<|' %('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CAR DETAILS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))
                            print('      ----------------------------------------------------------------------------------------------------------------------------------------------------')
                            print('      ====================================================================================================================================================')
                            print('      %-13s %-21s %-10s %-15s %-15s %-14s %-17s %-11s %-11s %-9s' %(' | COMPANY', '| MODEL', '| YEAR', '| COLOR', '| DURATION', '| CAR MECHANICS', '| WITH DRIVER', '| SEATS', '| COST', '| MILEAGE |'))
                            print('      ====================================================================================================================================================')
                        else:
                            pass       
                        
                        for idx, file_names in enumerate(car_to_rent_files):
                            with open(f'Rented_Cars\\{file_names}', 'r') as f:
                                for file_content_line in f.readlines():
                                    file_content = file_content_line.split(' | ')
                                    COMPANY = file_content[0]
                                    MODEL = file_content[1]
                                    YEAR = file_content[2]
                                    COLOR = file_content[3]
                                    DURATION = file_content[4]
                                    CAR_MECHANICS = file_content[5]
                                    WITH_DRIVER = file_content[6]
                                    SEATS = file_content[7]
                                    COST = file_content[8]
                                    MILEAGE = file_content[9]

                                    if idx < 9:
                                        print(f'({idx + 1}) = %-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))
                                    else:
                                        print(f'({idx + 1}) =%-13s %-21s %-10s %-15s %-15s %-15s %-17s %-11s %-11s %-11s|' %(' | ' + COMPANY, ' | ' + MODEL, ' | ' + YEAR, ' | ' + COLOR, ' | ' + DURATION, ' | ' + CAR_MECHANICS, ' | ' + WITH_DRIVER, ' | ' + SEATS, ' | ' + COST, ' | ' + MILEAGE))

                            print('      ====================================================================================================================================================')
                        
                        if not (car_to_rent_files):
                            print('\n|--- Sorry there are no cars for you to return at this time ---|')
                            while True:
                                _return = input('\nGo back? (YES): ').upper()
                                if _return == 'YES':
                                    Login.menu_admin(Login)
                                else:
                                    print('\n|!!! Please put suitable values !!!|')
                                    continue

                        else:
                            while True:
                                try:
                                    ask_to_return = int(input('\nWhich car do you want to return? (REPLY MUST BE IN NUMBER): '))
                                except:
                                    print('\n|!!! Please put number !!!|')
                                    continue

                                if ask_to_return > len(car_to_rent_files):
                                    print('\n|!!! Invalid choice. Please try again. !!!|')
                                    continue
                                else:
                                    dir = os.listdir('Rental_History')
                                    for files in dir:
                                        if car_to_rent_files[ask_to_return - 1] in files:
                                            os.remove(f'Rental_History\\{files}')
                                    with open(f'Registered_Cars\\{car_to_rent_files[ask_to_return - 1]}', 'w') as f:
                                        f.write(str(cars_to_rent_content[ask_to_return - 1]))
                                    
                                    os.remove(f'Rented_Cars\\{car_to_rent_files[ask_to_return - 1]}')

                                break
                            
                        while True:
                            ask_user = input('\nDo you want to return another car? (YES) or (NO): ').upper()
                            if ask_user == 'YES':
                                break
                            elif ask_user == 'NO':
                                print('\n|--- Going back to ADMIN DASHBOARD ---|')
                                Login.menu_admin(Login)
                            else:
                                print('\n|!!! Please put suitable values !!!|')
                                continue
            
            # IF admin choice is 7 then exit the program
            elif user_choice == '7':
                print('\n|---------------------------------------|')
                print('|>>> THANK YOU FOR USING OUR PROGRAM <<<|')
                print('|---------------------------------------|')
                exit()

            # IF admin choice is not from above then go to DASHBOARD for
            else:
                print('\n|!!! Please put suitable values !!!|')
                Login.menu_admin(Login)

    # FUNCTION OF ADDING CAR BY ADMIN
    def add_car(self):
        # MAKING OBJECT OF CAR DETAILS
        vehicle_details = Car_Details()
        # DEFINING LIST TO STORE VEHICLE DETAILS
        self.cars = []
        while True:
            # IF THE CAR DETAILS HAS BEEN ENTERED SUCCESSFULLY BY THE ADMIN PRINTING THE MESSAGE
            if vehicle_details.add_car():

                file = open(f'Registered_Cars\\{vehicle_details._make}_{vehicle_details._model}_{vehicle_details._year}_{vehicle_details._color}_{vehicle_details._duration}_{vehicle_details._car_mechanics}_{vehicle_details._with_driver}_{vehicle_details._seats}_{vehicle_details._cost}_{vehicle_details._mileage}.txt', 'w')
                self.cars.append(vehicle_details)
                file.write(' | '.join([f'{vehicle_details._make}', f'{vehicle_details._model}', f'{vehicle_details._year}', f'{vehicle_details._color}', f'{vehicle_details._duration}', f'{vehicle_details._car_mechanics}', f'{vehicle_details._with_driver}', f'{vehicle_details._seats}', f'{vehicle_details._cost}', f'{vehicle_details._mileage}']))

                file.close()

                with open(f'Registered_Cars\\{vehicle_details._make}_{vehicle_details._model}_{vehicle_details._year}_{vehicle_details._color}_{vehicle_details._duration}_{vehicle_details._car_mechanics}_{vehicle_details._with_driver}_{vehicle_details._seats}_{vehicle_details._cost}_{vehicle_details._mileage}.txt', 'r') as file1:
                    for content in file1.readlines():
                        if vehicle_details._make in content: MAKE = vehicle_details._make
                        if vehicle_details._model in content: MODEL = vehicle_details._model
                        if vehicle_details._year in content: YEAR = vehicle_details._year
                        if vehicle_details._color in content: COLOR = vehicle_details._color
                        if vehicle_details._duration in content: DURATION = vehicle_details._duration
                        if vehicle_details._car_mechanics in content: CAR_MECHANICS = vehicle_details._car_mechanics
                        if vehicle_details._with_driver in content: WITH_DRIVER = vehicle_details._with_driver
                        if vehicle_details._seats in content: SEATS = vehicle_details._seats
                        if vehicle_details._cost in content: COST = vehicle_details._cost
                        if vehicle_details._mileage in content: MILEAGE = vehicle_details._mileage

                print('\n|--- The Car has been registered and added to the inventory ---|')

            # ASK THE ADMIN TO ADD ANOTHER CAR OR NOT
            while True:
                another_register = input('\nDo you want to add another car? Reply with (YES) or (NO) --> ').upper()

                if another_register == 'YES':
                    Login.add_car(Login)
                
                elif another_register == 'NO':
                    Login.user_validation = False
                    Login.menu_admin(Login)
                else:
                    print('\n|!!! Please put suitable values !!!|')
                    continue
                continue

    # FUNCTION OF REGISTERED USER VALIDATION
    def registered_user(self):
        # IF THERE IS NO USER REGISTERED TO THE SYSTEM
        if not (os.listdir('Registered_Users')):
            reg_user_choice = input('\nSorry there are no users registered right now. Do you want to create one? (YES) or (NO): ').upper()
            if reg_user_choice == 'YES':
                reg_user_choice = reg_user_choice
                Login.main.registeration(Login)
            elif reg_user_choice == 'NO':
                reg_user_choice = reg_user_choice
                Login.main.login(Login)
            else:
                print('\n|!!! Please put suitable values !!!|')
                Login.registered_user(Login)

        # IF THE USER IS REGISTERED TO THE SYSTEM
        print()
        while True:
            # PRINT WELCOME MESSAGE
            print('\n|-------------------------------------------------|')
            print('|>>> ELCOME TO LOGIN PAGE FOR REGISTERED USERS <<<|')
            print('|-------------------------------------------------|')
            # ASKING USER TO ENTER USERNAME AND EMAIL
            self.username = input('\nEnter your username: ')
            self.email = input('Enter your email address: ')

            # IF THE USER FILE (username.txt) DOESN'T EXIST HANDLE THE ERROR
            try:
                file = open(f'Registered_Users\\{self.username}.txt', 'r')

                for line in file.readlines():
                    if line == f'Username: {self.username}' + '\n': self.USERNAME = self.username
                    elif line == f'Email: {self.email}' + '\n': self.EMAIL = self.email

            # PRINTING THE ERROR MESSAGE AND CALLING REGISTERED FUNCTION AGAIN
            except:
                print('\n|!!! The username is incorrect. Please put the correct username !!!|')
                Login.registered_user(Login)
            file.close()

            # VALIDATION USERNAME AND EMAIL AND IF VALIDATED VALIDATE PASSWORD AND SHOWING THE MESSAGE
            try:
                if (self.username == self.USERNAME) and (self.email == self.EMAIL):
                    while True:
                        Login.user_contents = self.USERNAME
                        print('\n|--- Email and Username are correct. Now put your password ---|')
                        self.password = input('\nEnter your password: ')
                    
                        file = open(f'Registered_Users\\{self.USERNAME}.txt', 'r')
                        try:
                                for line in file.readlines():
                                    if (line == f'Password: {self.password}' + '\n'): 
                                        self.PASSWORD = self.password
                                        print('\n|--- Your Email and Password are correct ---|')
                                        break
                                else:
                                    print('\n|!!! Sorry your password is not correct !!!|')
                                    continue
                                break
                        except:
                            break
                    break
                raise os.error
            # HANDLE THE EXCEPTION ERROR IF EMAIL IS NOT CORRECT
            except:
                print('\n|!!! Please enter correct email !!!|')
                continue

        # GIVING ACCESS TO REGISTERED USER TO ACCESS MENU
        Login.user_validation = True
        # DENYING ACCESS TO ADMIN TO ACCESS MENU
        Login.admin_validation = False
        try:
            if Car_Details._rental_history:
                Car_Details.rental_history(Login)
        except:
            Login.menu_user(Login)

    # FUNCTION OF REGISTERED USER MENU
    def menu_user(self):
        # IF user is logged in admin is logged out then show the registered user menu
        if Login.user_validation and not (Login.admin_validation):
            print('\n|--------------------------------------------|')
            print('|>>> WELCOME TO REGISTERED USER DASHBOARD <<<|')
            print('|--------------------------------------------|')
            # Checking user input
            user_choice = input('''
            1. Logout from the system
            2. View Personal Rental History
            3. View detail of cars to be rented out
            4. Select and book a car for a specific duration
            5. Do payment to confirm booking
            6. Exit --> ''')

            # IF user input is 1 then log out as a registered user
            if user_choice == '1':
                Login.main.from_menu = False
                Login.user_validation = False
                Login.main.login(Login)
            # IF ther user input 2 then show the rental history to user
            elif user_choice == '2':
                Car_Details.rental_history(Login)
            # IF the user input is 3 then show details of cars to be rented out
            elif user_choice == '3':
                Login.car_viewed = False
                Login.update_car = False
                Car_Details.display_car(Car_Details)
            # IF the user input is 4 then select and book a car for a specific duration
            elif user_choice == '4':
                Login.car_viewed = False
                Car_Details.select_and_book_car(Car_Details)
            # IF the user input is 5 then show payment screen
            elif user_choice == '5':
                Login.from_payment = True
                Car_Details.payment_screen(Login)
            elif user_choice == '6':
                print('\n|---------------------------------------|')
                print('|>>> THANK YOU FOR USING OUR PROGRAM <<<|')
                print('|---------------------------------------|')
                exit()
            # IF the user input is not from above printing the error message and showing the menu of registerd user again
            else:
                print('\n|!!! Please put suitable values !!!|')
                Login.menu_user(Login)
