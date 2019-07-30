# Checks if the file exists, it does not
def Main_Function():
    try:
        f = open("Doc","r")
    except:
        Error_Log("File does not exist")


# this will open a file called Error_Log and append the error to it
# the error is passed over from Main_Function
def Error_Log(self):
    f = open("Error_log","a")
    f.write("[*]{0}\n".format(self))
    f.close()

Main_Function()
