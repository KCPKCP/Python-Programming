# Keiland Pullen
# CSC 401 (Summer Session 2019)
# Assignment Three - Due 8/14


def createStudentDict():
    ''' Function to populate dictionary from .csv file '''

    try:
        fin = open('students.csv', 'r')
        fileContent = fin.readlines()
        fin.close
    except IOError:
        print('Sorry, there seems to be an issue with the file')

    studentDict = {}
    for line in fileContent:
        line = line.replace('\n', '')
        line = line.split(',')
        studentDict[line[0]] = [ str(line[1]), int(line[2]), str(line[3]) ]
        
    return studentDict

####

def searchStudentDictionary(studentDict):
    ''' Function to display dictionary keys and prompt user to select key '''

    while True:
        try:   
            for k in studentDict:
                print(k + '\t',end='')
        
            print('\n')

            userKey = input('Choose a key: ')
            studentDict[userKey]
            break
                
        except(KeyError):
            print('That student is not in the class.') 
    
    for i in studentDict:
        if userKey == i:
            print('Name: {}'.format(studentDict[i][0]) )
            print('Age: {} '.format(studentDict[i][1]) )
            print('Occupation: {} '.format(studentDict[i][2]) )
            print('')
                    
   
# Psuedocode for Problem 1

# Begin with opening Try Block
# Open the text file
# Read the text file into a List - use readlines()
# Close the file
# End the Try Block with EXCEPT on IOExeption
#      if EXCEPT, print statement
# Define Dictionary
# Begin Loop to read each List line
# Replace each newline character with a space
# Split each line at comma
# Add Key and Values into dictionary
# End Loop
# Return Dictionary

            
            

            






