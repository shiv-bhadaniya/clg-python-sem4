from datetime import date

name = input("Enter  name : ")
age = int(input("Enter age : "))


currentYear = date.today().year


bornYear = currentYear - age

userYearAfter100Year = bornYear + 100


print( name + " " + userYearAfter100Year + " after 100 year")

