shelf= [
    {'name': 'headsets','unit price': 250,'rating': 3,'stock': 40,'color': 'blue,white,black,grey'},

    {'name': 'tablet','unit price': '13000','rating': '4','stock': 5,'color': 'blue,white,black,grey'},

    {'name': 'smart phone',   'unit price': '35000','rating': '4.5','stock': 54,'color': 'blue,white,black,grey'},

    {'name': 'phone charger', 'unit price': '400','rating': '4.9','stock': 40,'color': 'blue,white,black,grey'},

    {'name': 'keypad phone','unit price': '3500','rating': '4','stock': 40,'color': 'blue,white,black,grey'},

    {'name': 'monitor','unit price': '5500','rating': '4.6','stock': 102,'color': 'white,black,grey'},

    {'name': 'mouse','unit price': '450','rating': '3.9','stock': 300,'color': 'black',},

    {'name': 'key board','unit price': '560','rating': '4.4','stock': 200,'color': 'white,black,grey'},

    {'name': 'Mic','unit price': '390','rating': '4.3','stock': 130,'color': 'black,grey'},

    {'name': 'CPU','unit price': '7500','rating': '4.9','stock': 80,'color': 'white,black,grey'},

    {'name': 'speaker','unit price': '1500','rating': '5','stock': 106,'color': 'white,black'},

    {'name': 'UPS','unit price': '42000','rating': '4.5','stock': 40,'color': 'white,black,grey'},

    {'name': 'flatbed scanner','unit price':17000 ,'rating': '3.9','stock': 65,'color': 'white,black,grey'},

    {'name': 'hard drive','unit price': '3000','rating': '3.9','stock': 50,'color':'-'},

    {'name': 'USB',   'unit price': '1200','rating': '5','stock': 250,'color':'-'},

    {'name': 'hard disk','unit price': '950','rating': '5','stock': 120,'color':'-'},

    {'name': 'RAM','unit price': '450','rating': '5','stock': 190,'color':'-'},
    ]

S1=shelf
she=[]
order=""


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

def Create_Account():
    Fname=input("First name:")
    Lname=input('Last name:')
    Num=input('Contact Number:')
    email=input('Email:')
    address=input("Current Address:")
    paswrd=input("Password:")

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
        
def View_Items():
    adminDisplayMenuWindow()
    

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
    

def Logout():
    main()

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

def logoutwindow():
    main()


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
        logoutwindow()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n===================================================\n")
        # adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()

main()        
