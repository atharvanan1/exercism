#Program to determine if the given year is leap year or not.
def is_leap_year(year):
    if(year%1 == 0):                            #First conditional to eliminate error conditions
        if(year%4 == 0):                        #Second conditional to factor in years divisible by 4
            if(year%100 == 0):                  #Third conditional to factor in years divisible by 100
                if(year%400 == 0):              #Fourth conditional to factor in years divisible by 400
                    return(True)                #years divisible by 400 are leap years
                else:
                    return(False)               #years not divisible by 400 but divisible by 100 are not leap
            else:
                return(True)                    #years normally divisible by 4 but not divisible by 100 are leap
        else:
            return(False)                       #years not divisible by 4 are not leap
    else:
        raise Exception("Not a whole number")   #exception for when input is not a number or integer number
