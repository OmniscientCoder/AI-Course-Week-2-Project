import Clear_Screen_Command as cls

# Set up login info variables
login_username=None
login_password=None

# Create class for the main network and create lists for usernames and passwords
class SocialNetwork:
    def __init__(self):
        self.user_information=[]
        self.user_login_information=[]
        self.user_info_list=[]

    # Create function for creating a new account on the network
    def NetworkCreateAccount(self, login_username, login_password):
        # Save username and password to list of user login information
        self.user_login_information.append({"username": login_username, "password": login_password})
        
    def NetworkLogin(self):
        # Clear page and welcome
        cls.sleep(1.5)
        cls.clear()

MainNetwork=SocialNetwork()

class User:
    def __init__(self, username, password, hidden_password, age, bio, messages):
        self.username=username
        self.user_password=password
        self.hidden_password=hidden_password
        self.age=age
        self.bio=bio
        self.msgs=messages
        self.friends_list=[]
        self.user_login=[]
        self.message_list=[]
    
    def UserInfo(self):
        print('Username:', self.username)
        print('Password:', self.hidden_password)
        print('Age:', self.age)
        print('Bio:', self.bio)
        print('Friends List:', self.friends_list)
        print('New Messages:', self.msgs)
    
    # All friend/block functions created in main page due to variables not working when set up here
    def UserRemoveFriend(self):
        print('Which friend would you like to remove from your friends list?')