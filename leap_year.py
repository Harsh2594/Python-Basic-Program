year = int(input("Enter the year "))

def leap_year(year):
  """Check given year is leap year or not"""
  if year%4 == 0:
    if year%100 == 0:
      if year%400 == 0:
        print("leap year!")
      else:
        print("Not a leap year")
    else:
      print("leap year!")     
  else:
    print("Not a leap year!") 

leap_year(year)       
      
