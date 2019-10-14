#this code helps check if a year is a leap year or not
#Concpets covered: Functions, if loop, logical operators 

def leap_check(year):
    leap=False
    if(year>=1900 & year<=10**5):
        if (year%400==0):
            leap=True
        if(year%100!=0 & year%4==0):
            leap=True
    return leap
            
  
year = int(input())
print(leap_check(year))
