from main import Create_Account, Logout
from admin import View_Items
from item import she, shelf

def User():               
    print("Type L to login or Type C to create Account")
    W=input(':')
    if W =='L' or W=='l':
        Login()
    elif W=='C'or W=='c':
        User_Account()
    else:
        User()


def Login():
    username=input("User name:")
    password=input("Password:")
    if username=='waseela zehra' and password=='12345':
        print("Login successfully")
        List()
        User_Choice_Option() 
    else:
        print('Enter the correct username and password')
        Login()

def user_login():
    Login()
    List()
    User_Choice_Option()

def User_Account():
    Create_Account()    
    List()
    User_Choice_Option()

def List():
    print("1. View Items") 
    print("2. Place Order")
    print("3. Cancel Order")
    print("4. Log out")
    print("=========================================================")
    User_Choice_Option()

def User_Choice_Option():
    choice=int(input("Enter your choice:"))
    if choice ==1:
        View_Items()
        print("\n==========================================================")
        List()
        print("\n------------------------------------------------------------")
        User_Choice_Option()
        print("\n===========================================================")
    elif choice ==2:
        Place_Order()
        print("\n==========================================================")
        List()
        print("\n------------------------------------------------------------")
        User_Choice_Option()
        print("\n===========================================================")
    elif choice ==3:
        Cancel_Order()
        print("\n==========================================================")
        List()
        print("\n------------------------------------------------------------")
        User_Choice_Option()
        print("\n===========================================================")
    elif choice==4:
        Logout()
    else:
        print("you have entered wrong option, Enter the correct option")
        User_Choice_Option()

def Place_Order():
    order_no=10
    View_Items()
    iname=input("Enter Product name:")
    for d in shelf:
        if d["name"]  ==iname:
            print("\n Name\t\t\t\tUnit Price\t\t\t\tRating\t\t\t\tStock\t\t\t\tColor")
            print("===============================================================")
            print(f'{d["name"]}\t\t{d["unit price"]}{d["stock"]}\t\t{d["color"]}')
            order = '{d["name"]}\t{d["unit price"]}\t{d["stock"]}\t\t{d["color"]}'
            conform = input("\nDo you want to place an order on the above shown product : Y/N ")

            if conform == 'Y' or conform == 'y':
                print("\nSuccessfully placed the order on the product {} {}".format(d["name"], d["unit price"]))
                order_no += 1
                print("Your order number is : ",order_no )
                #d["stock"] -= 1
                break

            elif conform == 'N' or conform == 'n':
                print("The order is not placed. You can carry on with you purchase.")
                break
            else:
                print("\nYou have entered wrong option. Please enter again\n")
                conform = input("\nDo you want to place an order on the above shown product : Y/N ")
                break

    if d["name"] != iname:
        print("\nYou have entered invalid id. Please enter valid name\n")
        product_name()
    print("\nAvailable products : \n")
    View_Items()

def product_name():
    View_Items()
    iname=input("\n Enter the Name:  ") 

def Cancel_Order():
    found = False
    Shope = []
    iname = input("Enter the order Name : ")
    for d in shelf:
        found = d["name"] == iname
        if found != True:
            she.append(d)
    if len(she) == d:
        print(f'{iname} is not found')
    else:
        print(f'{iname} is removed from the placed order') 