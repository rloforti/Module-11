'''
The direct formula is simply sideLength ** 2
The following function is supposed to use recursion to compute the area of a square from the 
length of its sides. 
For example, squareArea(3) should return 9.
Call the function and use 3 as the argument.
'''

def squareArea(sideLength) :
   if sideLength == 1 :
      return 1
   else :
      pass
    
    

'''
What line of code should replace `pass` to achieve this goal?
return squareArea(sideLength - 1)
return 2 * squareArea(sideLength - 1)
return 2 * sideLength + squareArea(sideLength - 1)
return 2 * (sideLength - 1) + squareArea(sideLength - 1)
'''