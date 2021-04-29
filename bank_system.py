from customer_account import CustomerAccount
from admin import Admin
import pathlib
import pickle
import os

accounts_list = []
admins_list = []

class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()
    
    def load_bank_data(self):
        
        # LOAD CUSTOMERS FROM ACCOUNT.DATA FILE
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data', 'rb')
            mylist = pickle.load(infile)
            for item in mylist:
                self.accounts_list.append(item)
            infile.close()
        else:
            print("No records to display")

        # LOAD ADMIN FROM ADMINS.DATA FILE
        file = pathlib.Path("admins.data")
        if file.exists():
            infile = open('admins.data', 'rb')
            mylist = pickle.load(infile)
            for item in mylist:
                self.admins_list.append(item)
            infile.close()
        else:
            print("No records to display")


    def search_admins_by_name(self, admin_username): # Search admin in the list
        found_admin = None
        for a in self.admins_list:
            username = a.get_username() #Compare usernam with the object's username
            if username == admin_username:
                found_admin = a
                break
        if found_admin == None:
            print("\n The Admin %s does not exist! Try again...\n" %admin_username)
            
        return found_admin
        
    def search_customers_by_accountno(self, customer_accno):
        found_accno = None
        for a in self.accounts_list:
            acc_no = a.get_account_no()
            if str(acc_no) == str(customer_accno):
                found_accno = a
                break
        if found_accno == None:
            print("\n The Customer %s does not exist! Try again...\n" %customer_accno)
            
        return found_accno

    # --------MAIN MENU---------

    def main_menu(self):
        #print the options you have
        while True:
            print()
            print()
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("Welcome to the Python Bank System")
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("1) Admin login")
            print ("2) Quit Python Bank System")
            print (" ")
            try:
                option = int(input ("Choose your option: "))
            except ValueError:
                print("[ERROR]Invalid choice")
                break
            return option


    def run_main_options(self): # runs main menu
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input ("\n Please input admin username: ")
                password = input ("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj != None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
                print ("\n Thank-You for stopping by the bank!")
            else:
                print("[ERROR]Please select one of the following options")


    def transferMoney(self, sender_account_no, receiver_account_no, amount):
        sender = self.search_customers_by_accountno(sender_account_no)   #Search for sender
        receiver = self.search_customers_by_accountno(receiver_account_no)  #Search for receiver
        if sender is not None and receiver is not None:  #Checks if both are valid customers
            if sender.get_balance() >= amount:
                sender.deposit_withdraw(amount,2)# withdraw money from sender
                receiver.deposit_withdraw(amount, 1)# Deposit money to the receiver
            else:
                print("[ERROR]Transaction cannot be completed as ", sender.get_first_name(), sender.get_last_name(),
                      "does not have enough balance")

                
    def admin_login(self, username, password):
        found_admin = self.search_admins_by_name(username)
        msg = "\n Login failed"
        if found_admin != None:
            if found_admin.get_password() == password:
                msg = "\n Login successful"
        return msg, found_admin  #Returns the message and the amin object

        pass

    def delete_customer_account(self,customer_account):
        if customer_account is not None:
            self.accounts_list.remove(customer_account)
            # Deletes the customer from the account.data file
            file = pathlib.Path("accounts.data")
            if file.exists():
                infile = open('accounts.data', 'rb')
                oldlist = pickle.load(infile)
                infile.close()
                newlist = []
                for item in oldlist:
                    if item.lname != customer_account.lname:
                        newlist.append(item)
                # It removes the old file and replace it with a new one with the new list
                os.remove('accounts.data')
                outfile = open('newaccounts.data', 'wb')
                pickle.dump(newlist, outfile)
                outfile.close()
                os.rename('newaccounts.data', 'accounts.data')

    #-----ADMIN MAIN MENU------

    def admin_menu(self, admin_obj):
        while True:
            print(" ")
            print(
                "Welcome Admin %s %s : Avilable options are:" % (admin_obj.get_first_name(), admin_obj.get_last_name()))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("1) Transfer money")
            print("2) Customer account operations & profile settings")
            print("3) Delete customer")
            print("4) Print all customers detail")
            print("5) Update name")
            print("6) Update address")
            print("7) Management report menu")
            print("8) Create new customer")
            print("9) Sign out")
            print(" ")
            try:
                option = int(input ("Choose your option: "))
            except ValueError:
                print("[ERROR]Invalid choice")
                break
            return option

    def management_menu(self):
        while True:
            print(" ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("1) Total number of customers in the system")
            print("2) Sum of customers money")
            print("3) Sum of interest payable to all accounts for one year")
            print("4) Total amount of overdraft")
            print("5) Go back")
            print("")
            try:
                option = int(input("Choose your option: "))
            except ValueError:
                print("[ERROR]Invalid choice")
                break
            return option

    def run_admin_options(self, admin_obj):                                
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                while True:
                    try:
                        sender_account_no = int(input("\n Please input sender account number: "))
                        amount = float(input("\n Please input the amount to be transferred: "))
                        receiver_account_no = int(input("\n Please input receiver account number: "))
                    except ValueError:
                        print("[ERROR]Invalid input. Account number must be a number")
                        continue
                    else:
                        self.transferMoney(sender_account_no, receiver_account_no, amount)
                        break
            elif choice == 2:
                customer_acc_no = input("\n Please input customer account number :\n")
                customer_account = self.search_customers_by_accountno(customer_acc_no)
                if customer_account != None:
                    customer_account.run_account_options()
            
            elif choice == 3:
                # Check if admin hs full rights
                if admin_obj.has_full_admin_right():
                    customer_acc_no = input("\n input customer account number you want to delete: ")
                    customer_account = self.search_customers_by_accountno(customer_acc_no)
                    if customer_account != None:
                        print(customer_account.get_first_name(), "has been successfully deleted from the system")
                        self.delete_customer_account(customer_account)
                else:
                    print("You don't have enough permission!")
            
            elif choice == 4:
                self.print_all_accounts_details()

            elif choice == 5:
                while True:
                    fname = input("\n Enter new first name: ")
                    lname = input("\nEnter new  last name: ")
                    if hasNumbers(fname) or hasNumbers(lname):
                        print("[ERROR]Invalid input. Names cannot contain numbers")
                        continue
                    else:
                        admin_obj.update_first_name(fname)
                        admin_obj.update_last_name(lname)
                        print("Your details has been changed! New details are:")
                        admin_obj.print_details()
                        break

            elif choice == 6:
                address = input("Enter the new address (Number/name, Street Name, City, Postcode): ")
                addresslist = address.split()
                admin_obj.update_address(addresslist)
                print("The address has been changed! New details are:")
                admin_obj.print_details()

            elif choice == 7:
                while True:
                    option = self.management_menu()
                    if option == 1:
                        len(self.accounts_list)
                        print("Total customers in the systems are:",len(self.accounts_list)) # Prints the lenght of the self.accounts_list
                    elif option == 2:
                        i = 0
                        tot = 0
                        for c in self.accounts_list:
                            i += 1
                            tot += c.get_balance() # Iterates every element and get their balance and add it to the total

                        print("The sum of every customer's money is:","£"+str(tot))
                    elif option == 3:
                        i = 0
                        totint = 0
                        for c in self.accounts_list:
                            i += 1
                            if c.get_balance() > 0:
                                interest = (float(c.get_balance()) / 100) * float(c.get_interest_rate())# Cast the balance and the interest rate as a float to avoid any type error
                                totint += interest

                        print("The sum of interest payable to all accounts for one year is:","£"+str(totint))

                    elif option == 4:
                        i = 0
                        tot_overdraft = 0
                        for c in self.accounts_list:
                            i += 1
                            if c.get_balance() < 0:# If balance is below 0 then the account has overdraft
                                tot_overdraft += float(c.get_balance())

                        print("Total amount of overdraft taken by customers is:","£"+str(tot_overdraft))
                    elif option == 5:
                        break

            elif choice == 8:
                while True:
                    fname = input("Enter first name: ")
                    lname = input("Enter last name: ")
                    if hasNumbers(fname) or hasNumbers(lname):
                        print("[ERROR]Invalid input. Names cannot contain numbers")
                        continue
                    else:
                        address = input("Enter address: ")
                        acc_no = self.accounts_list[-1].get_account_no() + 1
                        try:
                            balance = int(input("Input Balance: "))
                        except ValueError:
                            print("[ERROR]Invalid input.")
                            continue
                        else:
                            while True:
                                print(" ")
                                print("1. Classic")
                                print("2. Platinum")
                                print("3. Student")
                                print("4. Premium")
                                ch = input("Select account type: ")
                                if ch == '1':
                                    acc_type = "classic"
                                    break
                                elif ch == '2':
                                    acc_type = "platinum"
                                    break
                                elif ch == '3':
                                    acc_type = "student"
                                    break
                                elif ch == '4':
                                    acc_type = "premium"
                                    break
                                else:
                                    print("Not a valid option!")
                                    continue

                        c = CustomerAccount(fname,lname,address,acc_no,balance,acc_type)
                        self.accounts_list.append(c)
                        break

            elif choice == 9:
                loop = 0
                print ("\n Exit account operations")
            else:
                print("[ERROR]Please selected one of the following options")



    def print_all_accounts_details(self):
        i = 0
        for c in self.accounts_list:
            i += 1
            print('\n %d. ' % i, end=' ')
            c.print_details()
            print("------------------------")

def hasNumbers(inputString):# Checks if a given string hs number in them
    return any(char.isdigit() for char in inputString)

app = BankSystem()
app.run_main_options()
