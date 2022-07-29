import Social_Network_Classes as socnetclss
from Social_Network_Classes import SocialNetwork as socnet
import Clear_Screen_Command as cls
import json

info_name=None

MainNetwork=socnetclss.MainNetwork

# Set up sleep and done func for smooth transition between processes
def SleepDoneShort():
    cls.sleep(.5)
    cls.clear()
    print('...')
    cls.sleep(.1)
    print('Done!')
    cls.sleep(.75)
    cls.clear()

def SleepDoneLong():
    cls.sleep(.5)
    cls.clear()
    print('...')
    cls.sleep(.1)
    print('...')
    cls.sleep(.1)
    print('...')
    cls.sleep(.2)
    print('Done!')
    cls.sleep(.75)
    cls.clear()

# Function to add user data to json
def write_json(filename="app.json"):
    with open(filename,'w') as file:

        data=[]
        for user in MainNetwork.user_information:
            data.append(user)

        # Sets file's current position at offset.
        file.seek(0)

        # Convert back to json.
        json.dump(data, file, indent=4)

# Function to save login data to json
def write_json_login(filename="login.json"):
    with open(filename, 'w') as file:

        data2=[]
        for login in MainNetwork.user_login_information:
            data2.append(login)

        file.seek(0)

        json.dump(data2, file, indent=4)

# Create function to load data from saved json file
def load_json():
    user_library=json.load(open("app.json", 'r'))
    for dict in user_library:
        MainNetwork.user_information.append(dict)

    login_library=json.load(open("login.json", 'r'))
    for dict in login_library:
        MainNetwork.user_login_information.append(dict)

load_json()

 # Set-up main welcome page to run at startup
def MainPage():
    print('**************************************************')
    print('**************************************************')
    print('                     Welcome!!                    ')
    print('**************************************************')
    print('**************************************************')
    print('')
    print('')

    while True:
        # Give options to sign-up, log-in, quit
        print('What would you like to do?')
        print('1) Sign-up')
        print('2) Log-in')
        print('3) Quit')

        user_main_page_answer=input("Please type %d, %d, or %d: " %(1, 2, 3))

        # Sign-up
        if user_main_page_answer=='1':
            # Check if user wants to create account
            print('Would you like to create an account? ')
            proceed_with_account_creation=input("Please type 'yes' or 'no': ")
        
            if proceed_with_account_creation=='yes':

                while True:
                    cls.clear()
                    
                    # Set username
                    print('What would you like to be known as? ')
                    login_username=input('Username: ')

                    # Check to see if username already exists
                    def FixUsername():
                        for dict in MainNetwork.user_login_information:
                            if dict['username']==login_username:

                                # If so, ask for another username
                                print('This username is already in use. Please pick another username.')

                                # fix username 
                                return True
                        return False

                    while FixUsername():
                        print('What would you like to be known as? ')
                        login_username=input('Username: ')

                    # If not, ask for password and create account
                    login_password=input('Please enter the password you would like to use: ')
                    MainNetwork.NetworkCreateAccount(login_username, login_password)
                    write_json_login()

                    # Create hidden password and save it to user
                    hidden_password='*' * len(login_password)

                    # Then save username to the user's login information
                    new_user=socnetclss.User(login_username, login_password, hidden_password , 'Not Set', 'None', '0')
                    new_user.user_login.append({"username": login_username, "password": login_password})

                    # Save user to network
                    MainNetwork.user_information.append(new_user.__dict__)
                    MainNetwork.user_info_list.append(new_user)
                    logged_in_user=new_user
                    # Save info to json
                    write_json()
                    
                    # Clear page and welcome
                    cls.clear()
                    print("Welcome, %s!" %(login_username))
                    MainNetwork.NetworkLogin()

                    # Create and send to profile page
                    def ProfilePage():
                       
                        while True:
                            print("Where would you like to go?")
                            print("1) Profile")
                            print("2) Friends List")
                            print("3) Inbox")
                            print("4) Log-out")
                            user_profile_page_answer1=input("Please type %d, %d, %d, or %d: " %(1, 2, 3, 4))
                            cls.sleep(.5)
                            cls.clear()

                            # Open user profile
                            if user_profile_page_answer1=='1':

                                for xuser in MainNetwork.user_information:
                                    
                                    while True:

                                    # Chooses user that is logged in to show the info of correct user
                                        if xuser["username"]==login_username and xuser["user_password"]==login_password:
                                            for user in MainNetwork.user_info_list:
                                                if user.username==xuser["username"]:
                                                    logged_in_user.UserInfo()
                                            cls.sleep(1)
                                            print("What would you like to do?")
                                            print("1) Edit Profile")
                                            print("2) Unhide Password")
                                            print("3) Go Back")
                                            print("4) Delete Profile")
                                            user_profile_page_answer2=input("Please type %d, %d, %d, or %d: " %(1, 2, 3, 4))
                                            
                                            # If user wants to edit profile:
                                            if user_profile_page_answer2=='1':

                                                # Security check 
                                                user_check=input("Please type in your password in order to edit your profile: ")
                                                
                                                while True:
                                                    cls.sleep(.5)
                                                    cls.clear()

                                                    # If correct password is entered, allow edit
                                                    if user_check==logged_in_user.user_password:
                                                        print('What would you like to edit?')
                                                        print("1) Username")
                                                        print("2) Password")
                                                        print("3) Age")
                                                        print("4) Bio")
                                                        print("5) Go Back")
                                                        user_profile_page_answer3=input("Please type %d, %d, %d, %d, or %d: " %(1, 2, 3, 4, 5))

                                                        # Change username
                                                        if user_profile_page_answer3=='1':
                                                            print('Current Username: ', logged_in_user.username)
                                                            new_username=input('What would you like your new username to be? ')
                                                            logged_in_user.username=new_username

                                                            for xuser in MainNetwork.user_login_information:
                                                                while True:
                                                                # Chooses user that is logged in to show the info of correct user
                                                                    if xuser["password"]==logged_in_user.user_password:
                                                                        xuser["username"]==new_username
                                                                        
                                                            write_json()
                                                            write_json_login()
                                                            SleepDoneShort()
                                                        
                                                        # Change password
                                                        elif user_profile_page_answer3=='2':
                                                            
                                                            while True:

                                                                # Again, security check for password change
                                                                user_check=input("Please type in your password in order to change your password: ")

                                                                # If correct password is entered, allow edit
                                                                if user_check==logged_in_user.user_password:
                                                                    print(logged_in_user.user_password)
                                                                    new_user_password=input('What would you like your new password to be? ')
                                                                    logged_in_user.user_password=new_user_password
                                                                    logged_in_user.hidden_password=len(new_user_password) * '*'
                                                                    for user in MainNetwork.user_login_information:
                                                                        while True:
                                                                        # Chooses user that is logged in to show the info of correct user
                                                                            if user["username"]==logged_in_user.username:
                                                                                user["password"]==new_user_password
                                                                    write_json()
                                                                    SleepDoneShort()
                                                                    print('Please wait while your page is reloaded...')
                                                                    SleepDoneShort()
                                                                    ProfilePage()
                                                                    break
                                                                                                                                
                                                                else:
                                                                    print('Incorrect password!!')
                                                                    cls.sleep(1.5)
                                                                    cls.clear()

                                                        # Change age
                                                        elif user_profile_page_answer3=='3':
                                                            print(logged_in_user.age)
                                                            new_age=input('How old are you?')
                                                            logged_in_user.age= new_age
                                                            write_json()
                                                            SleepDoneShort()
                                                        
                                                        # Change Bio
                                                        elif user_profile_page_answer3=='4':
                                                            print(logged_in_user.bio)
                                                            new_bio=input('Please type in a new description: ')
                                                            logged_in_user.bio.replace(new_bio)
                                                            write_json()
                                                            SleepDoneShort()
                                                            
                                                        # Go Back
                                                        elif user_profile_page_answer3=='5':
                                                            SleepDoneShort()
                                                            break
                                                        
                                                        # Unavailable choice
                                                        else:
                                                            print('Choice not available')
                                                            cls.sleep(1.5)
                                                            cls.clear()

                                                    else:
                                                        print("Incorrect password.")
                                                        break

                                            # Unhide password
                                            elif user_profile_page_answer2=='2':
                                                
                                                # Security check
                                                device_password=123
                                                guesses=0
                                                while guesses<=3:
                                                    device_password_check=input("Please enter your device's password to proceed: ")
                                                    
                                                    # If correct device password, then unhide login password
                                                    if device_password_check==device_password:
                                                        SleepDoneShort()
                                                        print("Password will only be shown for 5 seconds...")
                                                        cls.sleep(.75)
                                                        print("Password: ",login_password)
                                                        cls.sleep(5)
                                                        cls.clear()
                                                        break

                                                    else:
                                                        print("Incorrect password!") 
                                                        guesses+=1
                                                        cls.sleep(1)
                                                        cls.clear()
                                                                                                
                                                if guesses>3:
                                                    print("You will be sent back as you have incorrectly guessed your password too many times!")
                                                    cls.sleep(3)
                                                    cls.clear()
                                                    break
                                        else:
                                            break


                            # Open Friends List
                            elif user_profile_page_answer1=='2':

                                for xuser in MainNetwork.user_information:
                                    
                                    while True:

                                        # Chooses user that is logged in to show the info of correct user
                                        if xuser["username"]==login_username and xuser["user_password"]==login_password:
                                            for friend in logged_in_user.friends_list:
                                                print(friend.username)
                                            
                                            cls.sleep(.5)
                                            print('What would you like to do?')
                                            print('1) Add Friends')
                                            print('2) Remove Friends')
                                            print('3) Block Users')
                                            user_profile_page_answer2=input('Please type 1, 2, or 3: ')
                                            
                                            # Add/Block Friends
                                            if user_profile_page_answer2=='1' or '3':

                                                # Print user list       
                                                for xuser in MainNetwork.user_information:
                                                    print(xuser["username"])
                                                
                                                # Add Friends
                                                if user_profile_page_answer2=='1':
                                                    added_friend=input('Type in the username of the user you want to add as a friend: ')
                                                    
                                                    if added_friend in MainNetwork.user_information:
                                                        xuser["friends_list"].append(added_friend)
                                                        SleepDoneLong()
                                                        print("%s has been added as a friend!" %(added_friend))
                                                        print("Here is your new friends list: " )
                                                        for friend in logged_in_user["friends_list"]:
                                                            print(friend.username)
                                                        write_json
                                                    
                                                    else:
                                                        print("This user does not exist.")
                                                        cls.sleep(1)
                                                        cls.clear()

                                                # Block a user
                                                if user_profile_page_answer2=='3':
                                                    blocked_user=input('Type in the username of the user you want to block: ')
                                                    print("This user has now been blocked They can no longer send you messages")                                        

                                            elif user_profile_page_answer2=='2':
                                                print("Option not yet available. Sorry for the inconvenience")
                                            else:
                                                print("Choice not available.")
                                                cls.sleep(1)
                                                cls.clear()
                                        else:
                                            break


                            # Open inbox
                            elif user_profile_page_answer1=='3':
                                for xuser in MainNetwork.user_information:
                                    
                                    # Check for correct user
                                    while True:
                                        if xuser["username"]==login_username and xuser["user_password"]==login_password:
                                            print("1) Send messages?")
                                            print("2) View messages?")
                                            choice=input("Please pick 1 or 2: ")

                                            if choice=='1':
                                                msgto=input('To which user? ')
                                                msg=input('Message: ')
                                                msgto.message_list.append(msg)


                                            if choice=="2":
                                            # Chooses user that is logged in to show the info of correct user
                                                for message in logged_in_user.message_list:
                                                    print("Message: ", message)
                                                else:
                                                    break
                            
                            # Log-out of account
                            elif user_profile_page_answer1=='4':
                                SleepDoneLong()
                                MainPage()
                                break
                                                                        
                            else:
                                print('Choice not available.')
                                cls.sleep(1)
                                cls.clear()

                    ProfilePage()    
                            
            # Send back to main page
            else: 
                cls.clear()
                MainPage()
                break

        # Log-in
        elif user_main_page_answer=='2':
            while True:
                # Ask for username and password
                login_username=input('Please enter your username: ')
                login_password=input('Please enter your user password: ')

                # Do not say username doesn't exist as that would show a possible non-user the username doesn't exist, making any hacks easier.
                for xuser in MainNetwork.user_information:
                    
                #     if xuser["username"]==login_username and xuser["user_password"]==login_password:
                    user_run=socnetclss.User(xuser["username"], xuser["user_password"], xuser["hidden_password"], xuser["age"], xuser["bio"], xuser["msgs"])
                
                MainNetwork.user_info_list.append(user_run)
                MainNetwork.NetworkLogin()
                
                for xuser in MainNetwork.user_information:
                    
                    if xuser["username"]==login_username and xuser["user_password"]==login_password:
                        logged_in_user=xuser

                # Send user to account page on user interface 
                def ProfilePage():
                       
                        while True:
                            print("Where would you like to go?")
                            print("1) Profile")
                            print("2) Friends List")
                            print("3) Inbox")
                            print("4) Log-out")
                            user_profile_page_answer1=input("Please type %d, %d, %d, or %d: " %(1, 2, 3, 4))
                            cls.sleep(.5)
                            cls.clear()

                            # Open user profile
                            if user_profile_page_answer1=='1':

                                for xuser in MainNetwork.user_information:
                                    
                                    while True:

                                    # Chooses user that is logged in to show the info of correct user
                                        if xuser["username"]==login_username and xuser["user_password"]==login_password:
                                            for user in MainNetwork.user_info_list:
                                                if user.username==xuser["username"]:
                                                    logged_in_user.UserInfo()
                                            cls.sleep(1)
                                            print("What would you like to do?")
                                            print("1) Edit Profile")
                                            print("2) Unhide Password")
                                            print("3) Go Back")
                                            print("4) Delete Profile")
                                            user_profile_page_answer2=input("Please type %d, %d, %d, or %d: " %(1, 2, 3, 4))
                                            
                                            # If user wants to edit profile:
                                            if user_profile_page_answer2=='1':

                                                # Security check 
                                                user_check=input("Please type in your password in order to edit your profile: ")
                                                
                                                while True:
                                                    cls.sleep(.5)
                                                    cls.clear()

                                                    # If correct password is entered, allow edit
                                                    if user_check==logged_in_user.user_password:
                                                        print('What would you like to edit?')
                                                        print("1) Username")
                                                        print("2) Password")
                                                        print("3) Age")
                                                        print("4) Bio")
                                                        print("5) Go Back")
                                                        user_profile_page_answer3=input("Please type %d, %d, %d, %d, or %d: " %(1, 2, 3, 4, 5))

                                                        # Change username
                                                        if user_profile_page_answer3=='1':
                                                            print('Current Username: ', logged_in_user.username)
                                                            new_username=input('What would you like your new username to be? ')
                                                            logged_in_user.username=new_username

                                                            for xuser in MainNetwork.user_login_information:
                                                                while True:
                                                                # Chooses user that is logged in to show the info of correct user
                                                                    if xuser["password"]==logged_in_user.user_password:
                                                                        xuser["username"]==new_username
                                                                        
                                                            write_json()
                                                            write_json_login()
                                                            SleepDoneShort()
                                                        
                                                        # Change password
                                                        elif user_profile_page_answer3=='2':
                                                            
                                                            while True:

                                                                # Again, security check for password change
                                                                user_check=input("Please type in your password in order to change your password: ")

                                                                # If correct password is entered, allow edit
                                                                if user_check==logged_in_user.user_password:
                                                                    print(logged_in_user.user_password)
                                                                    new_user_password=input('What would you like your new password to be? ')
                                                                    logged_in_user.user_password=new_user_password
                                                                    logged_in_user.hidden_password=len(new_user_password) * '*'
                                                                    for user in MainNetwork.user_login_information:
                                                                        while True:
                                                                        # Chooses user that is logged in to show the info of correct user
                                                                            if user["username"]==logged_in_user.username:
                                                                                user["password"]==new_user_password
                                                                    write_json()
                                                                    SleepDoneShort()
                                                                    print('Please wait while your page is reloaded...')
                                                                    SleepDoneShort()
                                                                    ProfilePage()
                                                                    break
                                                                                                                                
                                                                else:
                                                                    print('Incorrect password!!')
                                                                    cls.sleep(1.5)
                                                                    cls.clear()

                                                        # Change age
                                                        elif user_profile_page_answer3=='3':
                                                            print(logged_in_user.age)
                                                            new_age=input('How old are you?')
                                                            logged_in_user.age= new_age
                                                            write_json()
                                                            SleepDoneShort()
                                                        
                                                        # Change Bio
                                                        elif user_profile_page_answer3=='4':
                                                            print(logged_in_user.bio)
                                                            new_bio=input('Please type in a new description: ')
                                                            logged_in_user.bio.replace(new_bio)
                                                            write_json()
                                                            SleepDoneShort()
                                                            
                                                        # Go Back
                                                        elif user_profile_page_answer3=='5':
                                                            SleepDoneShort()
                                                            break
                                                        
                                                        # Unavailable choice
                                                        else:
                                                            print('Choice not available')
                                                            cls.sleep(1.5)
                                                            cls.clear()

                                                    else:
                                                        print("Incorrect password.")
                                                        break

                                            # Unhide password
                                            elif user_profile_page_answer2=='2':
                                                
                                                # Security check
                                                device_password=123
                                                guesses=0
                                                while guesses<=3:
                                                    device_password_check=input("Please enter your device's password to proceed: ")
                                                    
                                                    # If correct device password, then unhide login password
                                                    if device_password_check==device_password:
                                                        SleepDoneShort()
                                                        print("Password will only be shown for 5 seconds...")
                                                        cls.sleep(.75)
                                                        print("Password: ",login_password)
                                                        cls.sleep(5)
                                                        cls.clear()
                                                        break

                                                    else:
                                                        print("Incorrect password!") 
                                                        guesses+=1
                                                        cls.sleep(1)
                                                        cls.clear()
                                                                                                
                                                if guesses>3:
                                                    print("You will be sent back as you have incorrectly guessed your password too many times!")
                                                    cls.sleep(3)
                                                    cls.clear()
                                                    break
                                            
                                            # Go Back
                                            else:
                                                cls.sleep(.5)
                                                cls.clear()
                                                break
                                        else:
                                            break



                            # Open Friends List
                            elif user_profile_page_answer1=='2':

                                for xuser in MainNetwork.user_information:
                                    
                                    while True:

                                        # Chooses user that is logged in to show the info of correct user
                                        if xuser["username"]==login_username and xuser["user_password"]==login_password:
                                            for friend in logged_in_user.friends_list:
                                                print(friend.username)
                                            
                                            cls.sleep(.5)
                                            print('What would you like to do?')
                                            print('1) Add Friends')
                                            print('2) Remove Friends')
                                            print('3) Block Users')
                                            user_profile_page_answer2=input('Please type 1, 2, or 3: ')
                                            
                                            # Add/Block Friends
                                            if user_profile_page_answer2=='1' or '3':

                                                # Print user list       
                                                for xuser in MainNetwork.user_information:
                                                    print(xuser["username"])
                                                
                                                # Add Friends
                                                if user_profile_page_answer2=='1':
                                                    added_friend=input('Type in the username of the user you want to add as a friend: ')
                                                    
                                                    if added_friend in MainNetwork.user_information:
                                                        xuser["friends_list"].append(added_friend)
                                                        SleepDoneLong()
                                                        print("%s has been added as a friend!" %(added_friend))
                                                        print("Here is your new friends list: " )
                                                        for friend in logged_in_user["friends_list"]:
                                                            print(friend.username)
                                                        write_json
                                                    
                                                    else:
                                                        print("This user does not exist.")
                                                        cls.sleep(1)
                                                        cls.clear()

                                                # Block a user
                                                if user_profile_page_answer2=='3':
                                                    blocked_user=input('Type in the username of the user you want to block: ')
                                                    print("This user has now been blocked They can no longer send you messages")                                        

                                            elif user_profile_page_answer2=='2':
                                                print("Option not yet available. Sorry for the inconvenience")
                                            else:
                                                print("Choice not available.")
                                                cls.sleep(1)
                                                cls.clear()
                                        else:
                                            break


                            # Open inbox
                            elif user_profile_page_answer1=='3':
                                for xuser in MainNetwork.user_information:
                                    
                                    while True:
                                        if xuser["username"]==login_username and xuser["user_password"]==login_password:
                                            print("1) Send messages?")
                                            print("2) View messages?")
                                            choice=input("Please pick 1 or 2: ")

                                            if choice=='1':
                                                msgto=input('To which user? ')
                                                msg=input('Message: ')
                                                msgto.message_list.append(msg)


                                            if choice=="2":
                                            # Chooses user that is logged in to show the info of correct user
                                                for message in logged_in_user.message_list:
                                                    print("Message: ", message)
                                                else:
                                                    break
                            
                            # Log-out of account
                            elif user_profile_page_answer1=='4':
                                SleepDoneLong()
                                MainPage()
                                break
                                                                        
                            else:
                                print('Choice not available.')
                                cls.sleep(1)
                                cls.clear()

                ProfilePage()

                break
                                            
                    #else:
                        #break
                        
                            
        # Quit
        elif user_main_page_answer=='3':
            SleepDoneLong()
            print('Goodbye!')
            cls.sleep(1)
            cls.clear()
            exit()

        # Unavailable choice
        else:
            cls.clear()
            print('Choice not available.')
            cls.sleep(1)
            cls.clear()

if __name__ == "__main__":
    MainPage()