def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:

    def __init__(self,top,bottom):

        self.num = top
        self.den = bottom
   #the methods go here
    def show(self):
        print(self.num,"/",self.den)
    
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
#     def __add__(self,otherfraction):
# 
#      newnum = self.num*otherfraction.den + self.den*otherfraction.num
#      newden = self.den * otherfraction.den
# 
#      return Fraction(newnum,newden)
    def gcd(m,n):
        while m%n != 0:
            oldm = m
            oldn = n
    
            m = oldn
            n = oldm%oldn
        return n
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
    
        return firstnum == secondnum
   
myfraction = Fraction(3,5)
myfraction.show()
print(myfraction)
f1 = Fraction(1,4)
f2 = Fraction(1,2)
f = f1+f2
print f
print f1==f2


# print(gcd(20,10))


