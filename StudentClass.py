from datetime import date

class Student:
    def __init__(self,student_id,name,dob,classification):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__classification = classification
        self.__age = 0
        self.__register = ''

    # Calculate age based on date of birth
    def calc_age(self):
        today = date.today()
        dob = self.__dob.split('/') #split the dob string into a list by '/'
        dob_year = int(dob[2]) #get the year from the list and convert it to an integer
        self.__age = today.year - dob_year

    # Determine registration dates based on classification
    def registration(self):
        if self.__classification.lower() == 'senior':
            self.__register = '11/1 thru 11/3'
        elif self.__classification.lower() == 'junior':
            self.__register = '11/4 thru 11/6'
        elif self.__classification.lower() == 'sophomore':
            self.__register = '11/7 thru 11/9'
        elif self.__classification.lower() == 'freshman':
            self.__register = '11/10 thru 11/12'
        else:
            self.__register = 'Classification not found'

    def return_age(self):
        return self.__age

    def return_registration(self):
        return self.__register