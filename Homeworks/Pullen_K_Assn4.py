# Keiland Pullen
# CSC 401 (Summer Session 2019)
# Assignment Four - Due 8/27


class Book(object):
    ''' A user-defined class for an actual library '''

    libraryName = 'DePaul Library'

    def __init__(self, title='unset', author='unset', edition=-1, checkedOut=False):
        ''' Initial function for Book class, and define instance variables '''
        self.title = title
        self.author = author
        self.edition = edition
        self.checkedOut = checkedOut

        
    def checkOut(self):
        ''' Function to check out the book '''
        self.checkedOut = True


    def returnBook(self):
        ''' Function to return book '''
        self.checkedOut = False
        

    def yesNoCheckInOut(self):
        ''' For checkedOut, change value from True/False to Yes/No '''
        if self.checkedOut == True:
            self.checkedOut = "Yes"
        else:
            self.checkedOut = "No"
        return self.checkedOut


    def __str__(self):
        ''' Print the object '''
        self.yesNoCheckInOut()
        book = '------ {} ------ \n\
    Title:\t{}\n\
    Author:\t{}\n\
    Edition:\t{}\n\
    Checked Out?  {}'.format(self.libraryName, self.title,
                                       self.author, self.edition, self.checkedOut)
        return book
    

    def __eq__(self, otherTitleAuthor):
        ''' Compare title and author, regardless of case (lower/upper)'''
        if self.title.lower() == otherTitleAuthor.title.lower() and\
           self.author.lower() == otherTitleAuthor.author.lower():
            return True
        else:
            return False
