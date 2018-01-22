import math

n=input('Please enter a number')
if n<0:
   print("Sorry, value is negative")
else:
   print(math.sqrt(n))
   
#############################
#############################
score = input('Please enter a number')
if score >= 90:
   print('A')
else:
   if score >=80:
      print('B')
   else:
      if score >= 70:
         print('C')
      else:
         if score >= 60:
            print('D')
         else:
            print('F')
           
if score >= 90:
   print('A')
elif score >=80:
   print('B')
elif score >= 70:
   print('C')
elif score >= 60:
   print('D')
else:
   print('F')   
            
            
            