import copy
class Polynomial(object):
    def __init__(self,coefficients):
        self.coeffs = coefficients
    def add(self,other):   
        longer = copy.copy(self.coeffs) if len(self.coeffs)-len(other.coeffs) >= 0 else (other.coeffs)
        shorter = other.coeffs if len(self.coeffs)-len(other.coeffs) >= 0 else (self.coeffs)
        start_index = len(longer) - len(shorter)
        count = 0
        for i in shorter:
          longer[start_index + count] = i + longer[start_index + count]
          count+=1
        return Polynomial(longer)
    def __add__(self, other):
        return self.add(other)
    #__radd__ doesnt work.also doesn't work for integer+polynomial multiplication
    def __repr__(self):  
        ret = ""
        num = 0
        for x in reversed(self.coeffs):
          if num == 0:
            ret+="{:.3f}".format(x)
          elif num == 1:
            ret = ("{:.3f}".format(x) + "z + ") + ret
          else:
            ret = ("{:.3f}".format(x) + " z**" + str(num) + " + ") + ret
          num+=1
        return ret
    def __str__(self):   
        return self.__repr__()
    def val(self, v):
          n=len(self.coeffs)-1
          tmp = 0
          for co in self.coeffs:
            tmp = tmp + float(co*(v**n)) 
            n -= 1 
          return tmp 
    def __call__(self, v):
        return self.val(v)    
    def roots(self):
        if len(self.coeffs) == 3:
          d = (((self.coeffs[1]**2) - (4*self.coeffs[0]*self.coeffs[2]) + 0j)**0.5)
          factor = (-1.0*self.coeffs[1])
          sol1=((factor+d)/(2.0*self.coeffs[0]))
          sol2=((factor-d)/(2.0*self.coeffs[0]))
          g=sol1.real if sol1==sol1.real else sol1
          f=sol2.real if sol2==sol2.real else sol2
          return [g,f]

        elif len(self.coeffs) == 2:
          return [((-float(self.coeffs[1]))/self.coeffs[0])]
        
        elif len(self.coeffs) == 1:
          return [0]
        
        else:
          print("Order too high to solve for roots")

    def mul(self, other):
        longer = self.coeffs if len(self.coeffs)-len(other.coeffs) >= 0 else other.coeffs    
        shorter = other.coeffs if len(self.coeffs)-len(other.coeffs) >= 0 else self.coeffs
        counter = 0
        ret =[counter]*(len(longer)+len(shorter)-1)
        temp_index = 0
        for i in reversed(longer):
          for j in reversed(shorter):
            ret[temp_index] += i*j
            temp_index+=1
          counter+=1
          temp_index = counter

    def intmul(self,i):
        l=self.coeffs
        for i in len(self.coeffs)-1:
            self.coeffs[i]=self.coeffs[i]*i   
        return Polynomial(list(reversed(l)))      

    def __mul__(self, other):    
        return self.mul(other)
    #__rmul__ doesn't work. also doesn't work for integer*polynomial multiplication
    
            
def main():
  p1 = Polynomial([1,2,3])
  print("p1:",p1)
  p2 = Polynomial([100,200])
  print("p2: ", p2)
  print("p1+p2: ", p1 + p2)
  print("value of p1 when v=1:",p1(1))
  print("value of p2 when v=-1:",p1(-1))
  print("value of p1+p2 when v=10:",(p1 + p2)(10))
  print("p1*p2: ",p1*p2)
  #print("p1*p2+p1: ",(p1*p2+p1))
  p3=Polynomial([3,2,-1])
  #print("roots of p1*p2:"),(p1*p2).roots()
  print("roots of p3:"),p3.roots()
  print("roots of p2:"),p2.roots()
  print(" roots of p1:"),p1.roots()
  #giving me floating point error, when i'm putting it into a list. doesn't give this error if i print it as a separatalety, like not in list
  #print("roots of p2+p3:"),(p2+p3).roots()
  #print(p1*8)

main()
