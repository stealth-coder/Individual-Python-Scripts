import os


# Method 1
# Executes the command, the output is in the terminal
Command = "dir"
os.system(Command)


# Method 2
# Executes the command, the output is assigned to a variable
# and printed in python
Command2 = os.popen("dir").read()
print(Command2)
