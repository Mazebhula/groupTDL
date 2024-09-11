
users = dict()
def create_user():
     import hashlib
     from getpass import getpass
     
     username = input('Username: ')
     password = hashlib.sha256(getpass('password: '  ).encode()).hexdigest()
     #print(password)
     users[username]=password
     return
 
def login():
     
    import hashlib
    from getpass import getpass
    print("welcome please login below")
    username = input('username: ')
    pasid = hashlib.sha256(getpass('password: ').encode()).hexdigest()
    if pasid== users[username]:
        print('GTF0')
        return True
    else:
        print('username or password incorrect/')
        return 
    
value = input('type "new"" for new user: ')
if value == 'new':
    create_user()
    login()
else:
    print ('user found')
    login()
