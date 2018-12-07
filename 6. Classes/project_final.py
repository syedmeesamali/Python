import copy

class Polynomial(object):
    def __init__(self,coefficients):
     # This is the constructor. everytime a new polynomial is made, this method is called.    
        self.coeffs=coefficients
    def add(self,other):
          # gets A COPY of the longer of the two lists (because we cannot modify the original Polynomials)
        longer = copy.copy(self.coeffs) if len(self.coeffs)-len(other.coeffs) >= 0 else (other.coeffs)
        # gets the shorter of the two lists
        shorter = other.coeffs if len(self.coeffs)-len(other.coeffs) >= 0 else self.coeffs
        # since the lists contain the coefficients in descending order in terms of exponential degree, 
        # we may need to start the addition of the coefficients by an offset
        start_index = len(longer) - len(shorter)
        # count keeps track of how many things we've added and moves the indexes up by one every time 
        # theres a new sum
        count = 0
        for i in shorter: #element in the shorter list
         longer[start_index+count]+=i #longer element+ shorter element
         count+=1 #next element of the the shorter list
        return Polynomial(longer) #return the final sum 
    def __add__(self, other):
        if isinstance(other,int): #if an integer is provided
            other=Polynomial([other]) #convert to polynomial
    # This is the method called when the + sign is used for 
    # instances of Polynomial. It calls the "add" method.
        return self.add(other) #call the add method above
    def __radd__(self,other): #for integer+polynomial addition
        return self.__add__(other)  #adds using __add__ method


    def sub(self,other): #special case, for subtraction
          # gets A COPY of the longer of the two lists (because we cannot modify the original Polynomials)
        longer = copy.copy(self.coeffs) if len(self.coeffs)-len(other.coeffs) >= 0 else (other.coeffs)
        # gets the shorter of the two lists
        shorter = other.coeffs if len(self.coeffs)-len(other.coeffs) >= 0 else self.coeffs
        # since the lists contain the coefficients in descending order in terms of exponential degree, 
        # we may need to start the addition of the coefficients by an offset
        start_index = len(longer) - len(shorter)
        # count keeps track of how many things we've subtracted and moves the indexes up by one every time 
        # theres a new difference
     #same methodology as add      
        count = 0
        for i in shorter:
         longer[start_index+count]-=i#subract by the element of shorter
         count+=1
        return Polynomial(longer)
    def __sub__(self,other): #operator overloading for subtract
        if isinstance(other,int):
            other=Polynomial([other])
        return self.sub(other)
    def __rsub__(self,other): #runs when integer-polynomial given
        return self.__sub__(other)
    
        
        
    def __repr__(self):
        # repr is a method that returns a basic string representation of a Polynomial.
        # since the document specified only 1 way to represent Polynomial, I decided 
        # to make repr and str be the same.
        ret = ""
        num = 0
        # ret initializd the return string. It's initialized out here in case a Polynomial has no
        # coefficients, in which case it returns the empty string.
        for x in reversed(self.coeffs):
          if num == 0:
        # this is basically saying that format the number x such that it displays three 
        # digits after the decimal point and turn it into a string      
            ret+="{:.3f}".format(x)
          elif num == 1:
            ret = ("{:.3f}".format(x) + "z + ") + ret
          else:
            ret = ("{:.3f}".format(x) + " z**" + str(num) + " + ") + ret
            
          num+=1
          
        return ret
    def __str__(self):
    # this returns a detailed string representation of Polynomial.
    # it calls repr to do so.    
        return self.__repr__()
    def val(self, v):
          n=len(self.coeffs)-1
          tmp = 0
          for co in self.coeffs:
            tmp = tmp + float(co*(v**n)) #co is number, #v is the provided value for x, #n is the number of times v must be multiplied itself
            n -= 1 #reduces, i.e does backward iteration of the list
          return tmp #the final answer
    def __call__(self, v):
        return self.val(v)    
    
    def roots(self):
    # case if 3 coefficients
        if len(self.coeffs) == 3:
          # initialize the return array
          # next two lines calculate both sides of the formula for finding the roots of a quadratic
          d = (((self.coeffs[1]**2) - (4*self.coeffs[0]*self.coeffs[2])+0j)**0.5)
          factor = (-1.0*self.coeffs[1])
          # next two lines calculate the two roots.
          sol1=((factor+d)/(2.0*self.coeffs[0]))
          sol2=((factor-d)/(2.0*self.coeffs[0]))
          
          #condtions to see if complex or not.remove the complex part of the number if it is 0
          g=sol1.real if sol1==sol1.real else sol1
          f=sol2.real if sol2==sol2.real else sol2
          #return the two roots in a list
          print "[",g,",",f,"]"
          return [g,f]
        # case if 2 coefficients
        elif len(self.coeffs) == 2:
          return [((-float(self.coeffs[1]))/self.coeffs[0])]
        # case if 1 coefficient
        elif len(self.coeffs) == 1:
          return [0]
        # case if 0 or more than 3 coefficients
        else:
          print "Order too high to solve for roots"
    def mul(self, other):
    # gets the longer of the two lists
        longer = self.coeffs if len(self.coeffs)-len(other.coeffs) >= 0 else other.coeffs
        # gets the shorter of the two lists
        shorter = other.coeffs if len(self.coeffs)-len(other.coeffs) >= 0 else self.coeffs
        # initializes the array in which we will store the new polynomial in. [counter] or[0] means an array
        # containing one 0, multiplying it by (len(longer)+len(shorter)-1) means to make the array
        # the size of length of the polynomials added together minus one. This is how multiplying
        # polynomials works.
        counter = 0
        ret =[counter]*(len(longer)+len(shorter)-1)
        # counter keeps track of which coefficient in the longer array we are multiplying with
        # the coefficients in the shorter array
        
        # temp_index keeps track of which array cell in ret we want to put the products
        # of certain coefficients in
        temp_index = 0
        for i in reversed(longer):
          for j in reversed(shorter):
            ret[temp_index] += i*j
            temp_index+=1
          # counter+=1 is saying now that we have finished multiplying a coefficient from 
          # longer with every coefficient in shorter, lets move the index from which we will multiply
          # the next coefficient every coefficient in shorter by one, because the next coefficient
          # in longer will be a degree smaller than the one we just did
          counter+=1
          # the following line is so that 
          temp_index = counter
          # return a new Polynomial containing "ret" but reversed, cuz we build it in reversed order, 
          # and I just have to have the list() there cuz of a python thing
        return Polynomial(list(reversed(ret)))      
    def __mul__(self, other):
        if isinstance(other,int):
            other=Polynomial([other])
        # This is the method called when the * sign is used for 
        # instances of Polynomial. It calls the "mul" method.
        return self.mul(other)      
    def __rmul__(self, other): #when polynomial*integer given
            return self.__mul__(other)

    
            
def main():
  #this main method is only here to test the sample inputs
  p1 = Polynomial([1,2,3])
  p2 = Polynomial([100,200])
  print "p1:",(p1)
  print "p2:",(p2)
  print  "integer*polynomial:",p1*2
  print "subtracting:", p1-p2
  print "subracting integer-poly:", p2-50
  print "p1+p2: ",(p1 + p2)
  print "polynomial+integer:", p1+2  
  print "value of p1 when v=1:",(p1(1))
  print "value of p2 when v=-1:",(p1(-1))
  print "value of p1+p2 when v=10:",((p1 + p2)(10))
  print "p1*p2: ",(p1 * p2)
  print "p1*p2+p1: ",(p1 * p2 + p1)
  p3=Polynomial([3,2,-1])
  print "roots of p1*p2:",(p1*p2).roots()
  print "roots of p3:",p3.roots()
  print "roots of p2:",p2.roots()
  print " roots of p1:",p1.roots() #giving me floating point error
  print "roots of p2+p3:",(p2+p3).roots()
main()
