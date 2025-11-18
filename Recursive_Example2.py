'''
The recursion winds up (or "goes down") and then winds down (or "comes back up"). 
These are the two classic phases of a recursive function call.

1. The "winding up" phase (the descent)
   The function keeps calling itself with smaller and smaller inputs, 
   building up a stack of unfinished calls. Each call is paused, waiting 
   for the deeper call to return.
2. The "winding down" phase (the ascent)
   Once the base case is finally reached, the calls start returning one by one, 
   finishing the work they had paused earlier.

The factorial of a number n (written n!) is:
n! = n × (n−1) × (n−2) × … × 1
and 0! = 1 (or 1! = 1) is the base case.
'''

def factorial(n):
    if n <= 1:          # base case
        return 1
    else:
        result = factorial(n - 1)
        return n * result

print(factorial(5))
    
'''
Let’s compute factorial(5) and watch the two phases clearly:

Phase 1: Winding up (descending – the function keeps calling itself)

factorial(5) → 5 * factorial(4)
                factorial(4) → 4 * factorial(3)
                                 factorial(3) → 3 * factorial(2)
                                                   factorial(2) → 2 * factorial(1)
                                                                     factorial(1) → returns 1   ← base case!
At the deepest point, the call stack looks like this (most recent call on top):  
factorial(1)  ← just returned 1
factorial(2)  ← waiting
factorial(3)  ← waiting
factorial(4)  ← waiting
factorial(5)  ← waiting      

Phase 2: Winding down (ascending – results bubble back up)
factorial(1) returns 1
    → factorial(2) now computes 2 * 1 = 2  and returns 2
        → factorial(3) computes 3 * 2 = 6  and returns 6
            → factorial(4) computes 4 * 6 = 24 and returns 24
                → factorial(5) computes 5 * 24 = 120 and returns 120

So the recursion first winds up all the way to the base case 
(building a tall stack of pending multiplications), then winds down, 
doing all the actual multiplications on the way back up.
This “wind-up-then-wind-down” pattern is exactly the same in every recursive 
function — whether it’s factorial, Fibonacci, tree traversal, or the square-area 
example we saw earlier.
'''