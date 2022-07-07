# Keiland Pullen
# CSC 401 (Summer Session 2019)
# Assignment One - Due 7/31


def firstLastHigher(lstNumbers):
    ''' Function to compare first and last numbers in a list then display the highest number'''

    num1 = lstNumbers[0]
    num2 = lstNumbers[-1]
    if num1 > num2:
        return num1
    else:
         print ('Sorry but the last or second number is larger')
         return num2


def circleGeometry(diam):
    ''' Function to accept diameter of circle and return string that is area of circle 
     Formula for area of a circle is pi * radius**2'''

    import math
    pi= math.pi
    radius = diam/2
    area = pi * (radius**2)
    string = ('The area is ' + str(area) )
    return area
    #return string # This will, hopefully, return a string for - print(circleGeometry(3)
                   # but, I'm unsure how to make the returns separately.... 


def isStringLengthEven(aWord):
    ''' Function to accept argument and determine if argument is even.
    Return Boolean -True- or -False- '''

    x = len(aWord)
    if x%2 == 0:
        return True
    else:
        return False


def checkStringLength(aNumber, listStrings):
    ''' Function to accept two arguments (integer and list of strings) and return -True-
    if each string is longer than the integer '''

    #For this function, each the number of items in the list was found, then the length of
    #each word in the list was compared with the integer. A new list was created to store
    #the boolean value. The second or new list was then checked to see if it contained any
    #value of False - if so, then end.
    #
    #I'm thinking that there has to be an easier solution, looking forward to seeing it.

    numStrings = len(listStrings)

    listValString = []
    
    for word in listStrings:
        if (len(word)) > aNumber:
            val = True
            listValString.append(True)
            #print (word + ' ' + str(val) )
        else:
            val = False
            listValString.append(False)
            #print (word + ' ' + str(val) )

    for valTorF in listValString: 
        if(valTorF == False):
            return False
        else:
            return True
            
   
     
    


       

