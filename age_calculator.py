import datetime
from datetime import date


try:
    #Get date input from user
    user_date_string = input('Enter a date in dd/mm/yyyy format: ')
    
    #Convert to date
    user_date = datetime.datetime.strptime(user_date_string, '%d/%m/%Y')
    
    #Get today’s date
    today = date.today()
    
    #Calculate age
    age = today.year - user_date.year - ((today.month, today.day) < (user_date.month, user_date.day))
    
    #Print Age
    print("User's age: " + str(age))
    
    #Check birthday
    if(today.month==user_date.month and today.day==user_date.day):
        print("Happy birthday!")
except:
        print("Incorrect data format, date format should be dd/mm/yyyy")