import math
anumber = input('Input a number, please:\n')
math.sqrt(abs(anumber))

try:
       print(math.sqrt(anumber))
except:
       print("Bad Value for square root")
       print("Using absolute value instead")
       print(math.sqrt(abs(anumber)))
# print(math.sqrt(anumber))
if anumber < 0:
    raise RuntimeError("You can't use a negative number")
    raise YError("You can't use a negative number")
    raise XError("You can't use a negative number")

else:
    print(math.sqrt(anumber))