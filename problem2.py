'''
1. Define the main() function to then call the function mystery with a positive integer argument n.
2. Write an input statement to get the value of n from the user.
3. The prompt should be: "Enter a positive integer: "
4. Enter, 1, 4, and -5 in response to the prompt and observe the output.
5. Modify the argument to n - 1 and remove the syntax `smaller = n - 1`

The way this function works is similar to the Fibonacci function in problem1.py.
Instead of adding the two previous values together, it adds the square of n to the result of 
calling mystery with n - 1.

'''

def mystery(n) :
   if n <= 0 :
      return 0
   else :
      smaller = n - 1
      return mystery(smaller) + n * n
   
