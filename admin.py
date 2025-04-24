from main import Create_Account, Logout
from item import she, shelf, S1

def Adminsitrator():
    Admin_Login()
    '''print("Create Account or Login")
    ty=input("")
    if ty=="Create Account" or ty=="create account":
        Admin_create_account()
    elif ty=="Login" or ty=="login":
        Admin_Login()
    else:
        print("Write correct option") 
        Adminsitrator()  '''        
    
def View_Items():
    adminDisplayMenuWindow()

def Admin_create_account():
    Create_Account()
    print("Your Account has been created successfully")
    Admin_Options()

def Admin_Login():
    username=input("User name:")
    password=input("Password:")
    if username=='waseela zehra' and password=='12345':
        print("Login successfully")
    Admin_Options()

def Admin_Options():
    print("=====================")
    print("1.Display Menu")
    print("2.Add Product")
    print("3.Remove Product")
    print("4.Products goods available")
    print("5.Logout")
    print("=====================")
    adminOptions()

def adminDisplayMenuWindow(): #Display Menu
    print("Name\tUnit Price\tStock\tRating\tColor")
    print("====================================================")
    for d in shelf:
        print(f'{d["name"]}\t{d["unit price"]}\t{d["stock"]}\t\t{d["rating"]}\t{d["color"]}')


def addproducts():
    n = int(input("Enter the no.of.items need to be added : "))
    for i in range(n):
        new_name = input("Enter name : ")
        new_unitprice = int(input("Enter Unit Price : "))
        new_stock = int(input("Enter stock: "))
        new_rating=input("Enter Ratinga:  ")
        new_color = input("Enter color : ")
        d = [{"name": new_name, "unit price": new_unitprice, "stock": new_stock, "rating": new_rating, "color": new_color}]
        shelf.extend(d)
        adminDisplayMenuWindow()

def removeproducts():
    item_name = input("Enter the item name need to be deleted : ")
    found = False
    for d in S1:
        found = d["name"] == item_name
        if found != True:
            she.append(d)
            continue
        if found == True:
            d["stock"] -= 1
    print("Deleting item....")
    if len(she) == d:
        print(f"{item_name} not found")
    else:
        print(f"{item_name}'s one available is removed from the list")
    adminDisplayMenuWindow()


def availableproducts():
    Total = 0
    print("\n")
    for d in shelf:
        print(f'{d["name"]} = {d["stock"]}')
        Total += d["stock"]
    print("\nTotal available goods is : ", Total)

def adminOptions():
    choice = int(input("Please enter your choice : "))
    if choice == 1:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        Admin_Options()
    elif choice == 2:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        addproducts()
        print("\n===================================================\n")
        Admin_Options()
    elif choice == 3:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        removeproducts()
        print("\n===================================================\n")
        Admin_Options()
    elif choice == 4:
        availableproducts()
        print("\n===================================================\n")
        Admin_Options()
    elif choice == 5:
        Logout()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n===================================================\n")
        # adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()