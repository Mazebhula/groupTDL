
users = dict()

def create_user():
     import hashlib
     from getpass import getpass
     
     username = input('Username: ')
     if " " in username:
         print("ERROR!, username must not contain spaces")
         return create_user()

     else:
        password = hashlib.sha256(getpass('Type in new password: '  ).encode()).hexdigest()
        #print("password stored is : "+password)
        
        users[username]=password
        return
     
def login():
     
    import hashlib
    from getpass import getpass
    print("welcome please login below")
    username = input('username: ')
    pasid = hashlib.sha256(getpass('password: ').encode()).hexdigest()
    if pasid== users[username]:
        print('welcome '+username +" you have succesfully logged in")
        return True
    else:
        print('username or password incorrect/')
        return 


def start():
    value = input('type in log in or sign up: ')
    if value.upper() == 'SIGN UP':
        create_user()
        login()
    elif value.upper() == 'LOGIN':
        print ('Input Details')
        login()
    else:
        print('Sign up or Login')
        start()
    return 
start()


