# Encapsulation is basically addind "__" in the beginning

class Car:
    
    __colour = ""
    __style = ""
    __type = ""
    __MaxSpeed = ""
    __price = ""

    def __init__(self):
        self.__updateSoftware()
        self.__colour = "Green"
        self.__style = "Sports"
        self.__type = "Super Car"
        self.__MaxSpeed = "300Mph"
        self.__price = "£100,000"



    def Set_Details(self, Colour, Style, Type, MaxSpeed, Price):
        self.__colour = Colour
        self.__style = Style
        self.__type = Type
        self.__MaxSpeed = MaxSpeed + "Mph"
        self.__price = "£" + Price



    def Show_Details(self):     
        print("Colour: {0}\n"
              "Style: {1}\n"
              "Type: {2}\n"
              "Max Speed: {3}\n"
              "Price: {4}\n"
              "===================\n".format(self.__colour, self.__style,
                                  self.__type, self.__MaxSpeed,
                                  self.__price))


        
    # This function cannot be changed 
    def __updateSoftware(self):
        print("Software up to date\n" +
              "===================\n")

    

Lambo = Car()
def question1():
    Q1 = input("Would you like to see the current details?\n")
    Q1 = Q1.lower()

    if Q1 in("yes", "y"):
        print("Current Details")
        Lambo.Show_Details()
        pass
    elif Q1 in("no", "n"):
        print("Okay\n")
        pass
    else:
        print("Please say 'yes' or 'no'.")
        question1()

    def question2():
        Q2 = input("Would you like to update the details?\n")
        Q2 = Q2.lower()

        if Q2 in("yes", "y"):
            Colour = input("Colour: ")
            Style = input("Style: ")
            Type = input("Type: ")
            MaxSpeed = input("Max Speed: ")
            Price = input("Price: ")
            
            Lambo.Set_Details(Colour, Style, Type, MaxSpeed, Price)
            print("===================\n"
                "Details updated\n")
            Lambo.Show_Details()
            
        elif Q2 in("no", "n"):
            print("Okay, goodbye")

        else:
            print("Please say 'yes or 'no'.\n")
            question2()
    question2()
        


question1()



#Blue_Car.__updateSoftware() is not accessible from the object,
#it will print an error
