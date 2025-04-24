from user import User
from admin import Adminsitrator


def main():
    print("Welcom to W_Electronic Shope")
    print("==========================================================")
    print("==========================================================")
    print("Type A for Admin or Type U for User")
    tp=input(":")
    if tp=='A' or tp=='a':
        Adminsitrator()
    elif tp=='U' or tp=='u':
        User() 
    else:
        print("Enter the correct option")
        main()

def Create_Account():
    Fname=input("First name:")
    Lname=input('Last name:')
    Num=input('Contact Number:')
    email=input('Email:')
    address=input("Current Address:")
    paswrd=input("Password:")

def Logout():
    main()

main() 