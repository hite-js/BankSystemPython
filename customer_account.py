import pathlib
import os
import pickle

class CustomerAccount:
    fname = ''
    lname = ''
    address = ''
    account_no = 0
    balance = 0
    acc_type = ''
    def __init__(self, fname, lname, address, account_no, balance,acc_type):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.account_no = account_no
        self.balance = float(balance)
        self.acc_type = acc_type

        # Creates/modifies the file whenever the object is created
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data', 'rb')
            oldlist = pickle.load(infile)
            oldlist.append(self)
            infile.close()
            os.remove('accounts.data')
        else:
            oldlist = [self]
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
    
    def update_first_name(self, fname):
        self.fname = fname
        # Access the file change and store the value
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data', 'rb')
            oldlist = pickle.load(infile)
            infile.close()
            os.remove('accounts.data')  #Removes old file and insert new one with new values
            for item in oldlist:
                if item.account_no == self.account_no:
                    item.fname = fname

            outfile = open('newaccounts.data', 'wb')
            pickle.dump(oldlist, outfile)
            outfile.close()
            os.rename('newaccounts.data', 'accounts.data')

    
    def update_last_name(self, lname):
        self.lname = lname
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data', 'rb')
            oldlist = pickle.load(infile)
            infile.close()
            os.remove('accounts.data')
            for item in oldlist:
                if item.account_no == self.account_no:
                    item.lname = lname

            outfile = open('newaccounts.data', 'wb')
            pickle.dump(oldlist, outfile)
            outfile.close()
            os.rename('newaccounts.data', 'accounts.data')

    # Defining getters and setters
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        self.address = addr
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data', 'rb')
            oldlist = pickle.load(infile)
            infile.close()
            os.remove('accounts.data')
            for item in oldlist:
                if item.account_no == self.account_no:
                    item.address = addr

            outfile = open('newaccounts.data', 'wb')
            pickle.dump(oldlist, outfile)
            outfile.close()
            os.rename('newaccounts.data', 'accounts.data')
        
    def get_address(self):
        return self.address

    def get_acc_type(self):
        return self.acc_type

    # Get overdraft limit according to the account type
    def get_overdraft_limit(self):
        if self.acc_type == "classic":
            return 300
        elif self.acc_type == "platinum":
            return 700
        elif self.acc_type == "student":
            return 1000
        elif self.acc_type == "premium":
            return 1500

    # Get interest rate according to the account type
    def get_interest_rate(self):
        if self.acc_type == "classic":
            return 1.00
        elif self.acc_type == "platinum":
            return 2.00
        elif self.acc_type == "student":
            return 2.5
        elif self.acc_type == "premium":
            return 5.0

    # If the option is 1 then it is going to deposit and if the option is 2 then it is going to withdraw
    def deposit_withdraw(self, amount, option):
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data', 'rb')
            mylist = pickle.load(infile)
            infile.close()
            os.remove('accounts.data')
            for item in mylist:
                if int(item.account_no) == self.account_no:
                    if option == 1:
                        self.balance += amount
                        item.balance += amount
                        print("The account has updated")
                    elif option == 2:
                        if amount <= item.balance:
                            item.balance -= amount
                            self.balance -= amount
                            print("The account has updated")
                        else:
                            print("You cannot withdraw larger amount")

        else:
            print("No records to Search")
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(mylist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
        
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)
        
    def get_balance(self):
        return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    def account_menu(self):
        while True:
            print ("\n Your Transaction Options Are:")
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("1) Deposit money")
            print ("2) Withdraw money")
            print ("3) Check balance")
            print ("4) Update customer name")
            print ("5) Update customer address")
            print ("6) Show customer details")
            print ("7) Back")
            print (" ")
            try:
                option = int(input("Choose your option: "))
            except ValueError:
                print("[ERROR]Invalid choice")
                break
            return option
    
    def print_details(self):
        print("Full name:","["+self.acc_type.upper()+"]",self.fname,self.lname)# Set the prefix as the account type
        print("Interest rate:",self.get_interest_rate())
        print("Overdraft limit:", self.get_overdraft_limit())
        print("Account No: %s" %self.account_no)
        print("Address: %s" %self.address)
        print(" ")

    # ---------Account menu----------
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                while True:
                    try:
                        amount = float(input("\n Please enter amount to be deposited: "))
                    except ValueError:
                        print("[ERROR]Invalid input.")
                        continue
                    else:
                        self.deposit_withdraw(amount, 1)
                        self.print_balance()
                        break
            elif choice == 2:
                while True:
                    try:
                        amount = float(input("\n Please enter amount to withdraw: "))
                    except ValueError:
                        print("[ERROR]Invalid input.")
                        continue
                    else:
                        self.deposit_withdraw(amount, 2)
                        self.print_balance()
                        break
            elif choice == 3:
                self.print_balance()
                pass
            elif choice == 4:
                while True:
                    fname = input("\n Enter new customer first name: ")
                    lname = input("\nEnter new customer last name: ")
                    if hasNumbers(fname) or hasNumbers(lname):
                        print("[ERROR]Invalid inputs. Names cannot contain numbers")
                        continue
                    else:
                        self.update_first_name(fname)
                        self.update_last_name(lname)
                        print("Customer details has been changed! New details are:")
                        self.print_details()
                        break

            elif choice == 5:
                address = input("Enter the new address (Number/name, Street Name, City, Postcode): ")
                addresslist = address.split()
                self.update_address(addresslist)
                print("The address has been changed! New details are:")
                self.print_details()
            elif choice == 6:
                self.print_details()
            elif choice == 7:
                loop = 0
            else:
                print("[ERROR]Please select one of the following options")


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

# ---------UNCOMMENT THIS IF YOU WANT TO LOAD THESE CUSTOMERS--------
# account_no = 1234
# CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 5000.00,"premium")
#
#
# account_no += 1
# CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], account_no, 3200.00,"classic")
#
#
# account_no += 1
# CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], account_no,18000.00,"platinum")
#
# account_no += 1
# CustomerAccount("Ali", "Abdallah", ["44", "Churchill Way West", "Basingstoke", "RG21 6YR"], account_no,-40.00,"student")