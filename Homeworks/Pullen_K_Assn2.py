# Keiland Pullen
# CSC 401 (Summer Session 2019)
# Assignment Two - Due 8/7


def countLinesWithString(word):
    ''' short function to return number of occurences of a string in a file'''
    
    try:
        infile = open('shakespeare_short.txt', 'r', encoding='utf-8')

        word = word.lower()

        fileContent = infile.readlines()

        infile.close
        
        numLines = len(fileContent)
        # print(numLines) - prints total number of lines in the file.
        
        occurrence = 0

        num = 0
        
        for line in fileContent:
            line = line.lower()
            # print(line) - prints entire file line by line
            num = line.count(word) #    should be ... if line.count(string) != 0   
            occurrence = occurrence + num

        statement = 'Testing with {} - should be {}'.format(word, occurrence)
        return statement

        
    except(FileNotFoundError):
        print ('Sorry there is no file by that name')

########################################       

def getMonthlySales(name, sales):
    ''' short function to read file and grab sales data'''

    try:
        infile = open('widget_sales_with_id.txt', 'r', encoding = 'utf-8')

        name = name.lower()

        fileContent = infile.readlines()

        infile.close()
        
        numLines = len(fileContent)
        
        nameFound = False  #Boolean to determine if the name is found in the file
        
        # print(sales) - for testing to ensure the values are being passed into function correctly
        # print(name)
        
        for i in fileContent:
            values = i.split(',')
            if (values[0].lower() == name):
                #print(values[0])  - for testing to ensure the name and values are split and assigned correctly
                #print(values[int(sales)])
                nameFound = True 
                statement = "Testing with {} and {}, should be {}".format(values[0], sales, values[int(sales)]) 
        
        if (nameFound):
            return (statement)
        #elif (nameFound != True):  # Just testing with elif and else
        else:
            falseStatement = "Testing with {} and {}, should be not return anything".format(name, sales) 
            return(falseStatement)
       
        
    except(FileNotFoundError):
        print ('The file is simply not here...')



def monthlySales(salesperson, month):

    saleperson = salesperson.lower()
    try:
        fin = open('widget_sales_with_id.csv','r')
        lines = fin.readlines()
        fin.close()
    except (FileNotFoundError):
        print(Could not find that file')

    for line in lines:    # holding an entire line of the document
        line = line.split(',') #line is holding a LIST of STRINGS from the initial line
        if line[0].lower() == salesperson:
              return(int(line[month]))
