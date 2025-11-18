'''
This program computes the nth Fibonacci number using recursion.
What is Fibonacci? Fibonacci is a sequence of numbers where each number is the sum of the 
two preceding ones, usually starting with 0 and 1. The sequence goes like this:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...    
In computer science, recursion is a programming technique where a function calls itself to 
solve smaller instances of the same problem.

The Fibonacci sequence is defined as follows:   
- fib(0) = 0
- fib(1) = 1  

Instructions:
1. Run the program and input different positive integers when prompted.
2. Modify the syntax so that it matches Interactive Practice 11.1
'''
def main():

    n = int(input("Enter a positive integer: "))
    result = fib(n)

    print(f"The {n}th Fibonacci number is: {result}")


def fib(n) :
   # Assumes n >= 0
   if n <= 2 :
      return n
   else :
      result1 = fib(n - 1)
      result2 = fib(n - 2)
      print (f"result1: {result1} + result2: {result2} = {result1 + result2}")
      return result1 + result2


main()