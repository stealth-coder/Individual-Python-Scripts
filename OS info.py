import os

# All_Info variable will hold all of your system information
All_Info = os.environ

#InfoDir is a directory
InfoDir = {}

# here we are updating our directory with the data collected about the system
InfoDir.update(All_Info)

# This "for" statement takes the key and vlue from the directory and prints it
# to the screen, with some formating in between
for key, value in InfoDir.items():
    print("====================\n"
          "{0} = {1}\n"
          "====================\n".format(key,value))
