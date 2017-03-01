from datetime import datetime

def ask_time():
    """This function asks the user if they would like to know the time"""
    time = raw_input("Would you like to know the time? (Y/N)")
    if len(time) > 0 and time == "y" and time.isalpha():
        return right_now()
    elif time == "n":
        print "OK"
    else:
        return ask_time()

#Create a function to tell the current time
def right_now():
    """This function creates a variable to retrieve the current date and time"""
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day

    print 'Current date: %s/%s/%s - %s:%s' % (current_day, current_month, current_year, now.hour, now.minute)

ask_time()
