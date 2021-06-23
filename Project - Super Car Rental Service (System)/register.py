# Initializing Register Class
class Register:
    
    def __init__(self):

        # Initializing Class Attributes 
        self.fname = ''
        self.lname = ''
        self.mob_no = 0
        self.email = ''
        self.password = ''
        self.gender = ''
        self.dob = ''
        self.user_name = ''
        
    # REGISTERATION FORM
    def register_user(self):
        print()
        # Asking user inputs to store the details
        # IF the detials are not accordingly then catch the exception error
        try:
            self.fname = input('Enter First Name (Example: TAYLOR): ').upper()
            self.lname = input('Enter Last Name (Example: SWIFT): ').upper()
            try:
                self.mob_no = int(input('Enter Mobile Number (Example: 01234567890): '))
            except:
                print('\n|!!! NOT A NUMBER !!!|')
            self.user_name = input('Choose a username (Example: taylor234): ')
            self.email = input('Enter Email (Example: taylor234@gmail.com): ')
            self.password = input('Enter Password (Example: faho213hc8): ')
            self.gender = input('Are you a (MALE) or (FEMALE))? ').upper()
            self.dob = input('Enter your Date of Birth (Example: 5-December-1996): ')
            return True

        # Handle the exception error and showing the FORM again
        except ValueError:
            print('\n|!!! Please put suitable values !!!|')
            Register.register_user(Register)

            
