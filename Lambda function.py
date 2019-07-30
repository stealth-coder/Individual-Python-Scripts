# Lambda function is used to create a small anonymous functions

# the a, b, c takes the passed variables, anything after ":" is the activity
# we want to perform 
x = lambda a, b, c : a + b + c
print(x(5, 8, 2))
# or
numbers = x(5, 8, 2)
print(numbers)


# another example
y = lambda name, surname: name + surname
variable = y("Bob ", "Rob")

print (variable)
