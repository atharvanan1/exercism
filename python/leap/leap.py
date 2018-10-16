# Program to determine if the given year is leap year or not.
def is_leap_year(year):
    if(year % 1 == 0):                          # Eliminate error conditions
        if(year % 4 == 0):                      # Numbers divisible by 4
            if(year % 100 == 0):                # Numbers divisible by 100
                if(year % 400 == 0):            # Numbers divisible by 400
                    return(True)                # Leap year inner condition
                else:
                    return(False)               # Not leap year inner condition
            else:
                return(True)                    # Leap year outer condition
        else:
            return(False)                       # Not leap year outer condition
    else:
        raise Exception("Not a whole number")   # exception bad input
