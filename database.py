from fileinput import filename
import random
import pyrebase

## Your web app's Firebase configuration
## For Firebase JS SDK v7.20.0 and later, measurementId is optional
firebaseConfig = {
    'apiKey': "AIzaSyDvOJBRKQt6CxH5bF-1Rz1ihzTYQ7kYP5U",
    'authDomain': "dgame-35079.firebaseapp.com",
    'databaseURL': "https://dgame-35079-default-rtdb.firebaseio.com",
    'projectId': "dgame-35079",
    'storageBucket': "dgame-35079.appspot.com",
    'messagingSenderId': "180299174394",
    'appId': "1:180299174394:web:35ece15111582322c05443",
    'measurementId': "G-M9JJ8DNNX2"
}

firebase=pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

#Authentication
loginOrSignup = input("Do you have an account? (yes/no)")
if loginOrSignup == "yes":
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    try:
        auth.sign_in_with_email_and_password(email,password)
        print("Logged in")
    except:
        print("Invalid Login")
else:
#Signup
    email = input("Register your email: ")
    password = input("Enter a password: ")
    repeatpassword = input("Confirm your password: ")
    if password == repeatpassword:
        try:
            ranID = (random.randint(1,1000) * 11)
            
            auth.create_user_with_email_and_password(email,password)
            data = {'ID': ranID, 'email': email}
            db.child("Players").child(ranID).set(data)
            print("Valid")
        except:
            print("Account already exist")

#put file storage
#fileName = input("Enter the name of the file that you are uploading")
#cloudFileName = input("Enter the name of the file from the cloud")
#storage.child(cloudFileName).put(fileName)

#get file from storage
#getFile = input("Enter the name of the file you want to get")
#storage.child(cloudFileName).download("", "downloaded.txt")

# set this later to down from the server and set default values and ID
# so when the user login it gets the default file and assign the values
# that will be required in order for the game to run

