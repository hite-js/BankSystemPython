import pathlib
import pickle
import os

class Admin:
    fname = ''
    lname = ''
    address = ''
    user_name = ''
    password = ''
    full_admin_rights = ''

    def __init__(self, fname, lname, address, user_name, password, full_admin_rights):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.user_name = user_name
        self.password = password
        self.full_admin_rights = full_admin_rights

        # Creates/modifies the file whenever the object is created
        file = pathlib.Path("admins.data")
        if file.exists():
            infile = open('admins.data', 'rb')
            oldlist = pickle.load(infile)
            oldlist.append(self)
            infile.close()
            os.remove('admins.data')
        else:
            oldlist = [self]
        outfile = open('newadmins.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newadmins.data', 'admins.data')

    #--------GETTERS AND SETTERS--------

    def update_first_name(self, fname):  # Access the file change and store the value
        self.fname = fname
        file = pathlib.Path("admins.data")
        if file.exists():
            infile = open('admins.data', 'rb')
            oldlist = pickle.load(infile)
            infile.close()
            os.remove('admins.data')
            for item in oldlist:
                if item.user_name == self.user_name:
                    item.fname = fname

            outfile = open('newadmins.data', 'wb')
            pickle.dump(oldlist, outfile)
            outfile.close()
            os.rename('newadmins.data', 'admins.data')
    
    def update_last_name(self, lname):
        self.lname = lname
        file = pathlib.Path("admins.data")
        if file.exists():
            infile = open('admins.data', 'rb')
            oldlist = pickle.load(infile)
            infile.close()
            os.remove('admins.data')
            for item in oldlist:
                if item.user_name == self.user_name:
                    item.lname = lname

            outfile = open('newadmins.data', 'wb')
            pickle.dump(oldlist, outfile)
            outfile.close()
            os.rename('newadmins.data', 'admins.data')
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        self.address = addr
        file = pathlib.Path("admins.data")
        if file.exists():
            infile = open('admins.data', 'rb')
            oldlist = pickle.load(infile)
            infile.close()
            os.remove('admins.data')
            for item in oldlist:
                if item.user_name == self.user_name:
                    item.address = addr

            outfile = open('newadmins.data', 'wb')
            pickle.dump(oldlist, outfile)
            outfile.close()
            os.rename('newadmins.data', 'admins.data')
    
    def set_username(self, uname):
        self.user_name = uname
        file = pathlib.Path("admins.data")
        if file.exists():
            infile = open('admins.data', 'rb')
            oldlist = pickle.load(infile)
            infile.close()
            os.remove('admins.data')
            for item in oldlist:
                if item.user_name == self.user_name:
                    item.user_name = uname

            outfile = open('newadmins.data', 'wb')
            pickle.dump(oldlist, outfile)
            outfile.close()
            os.rename('newadmins.data', 'admins.data')

        
    def get_username(self):
        return self.user_name
        
    def get_address(self):
        return self.address      
    
    def update_password(self, password):
        self.password = password
        file = pathlib.Path("admins.data")
        if file.exists():
            infile = open('admins.data', 'rb')
            oldlist = pickle.load(infile)
            infile.close()
            os.remove('admins.data')
            for item in oldlist:
                if item.user_name == self.user_name:
                    item.password = password

            outfile = open('newadmins.data', 'wb')
            pickle.dump(oldlist, outfile)
            outfile.close()
            os.rename('newadmins.data', 'admins.data')
    
    def get_password(self):
        return self.password
    
    def set_full_admin_right(self, admin_right):
        self.full_admin_rights = admin_right
        file = pathlib.Path("admins.data")
        if file.exists():
            infile = open('admins.data', 'rb')
            oldlist = pickle.load(infile)
            infile.close()
            os.remove('admins.data')
            for item in oldlist:
                if item.user_name == self.user_name:
                    item.full_admin_rights = admin_right

            outfile = open('newadmins.data', 'wb')
            pickle.dump(oldlist, outfile)
            outfile.close()
            os.rename('newadmins.data', 'admins.data')

    def has_full_admin_right(self):
        return self.full_admin_rights

    def print_details(self):
        print("First name", self.fname)
        print("Last name", self.lname)
        print("Username name", self.user_name)
        print("Address: %s" % self.address)
        print(" ")
        print(" ")


# ---------UNCOMMENT THIS IF YOU WANT TO LOAD THESE CUSTOMERS--------
# Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True)
# Admin("Cathy",  "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False)