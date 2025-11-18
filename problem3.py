## Finds the position of the first occurrence of a substring.
#  @param string a string
#  @param sub the substring to search for
#  @return the first position of sub in string, or -1 if it doesn't occur
#
'''
Suppose we want to find the position of the first occurrence of a substring in a potentially 
very long string. For example, we may want to find the first occurrence of the string 
"Cheshire cat" within the text of “Alice in Wonderland.” Let’s solve the problem with recursion.

Instructions:
1. Define a main() function
2. Rearrange the code to solve Interactive Problem 3 on page 524.
3. Write an input() with prompt ("Enter a phrase: ")
4. Write an input() with prompt ("Enter a substring: ")
5. Test the syntax using the following phrase and substring:
    phrase: All the world's a stage, and all the men and women merely players; They have their exits
    sub: and women
6. Print the result.

else:
if pos == -1:
return 0
return -1
if string.startswith(sub):
return pos + 1
pos = indexOf(string[1:], sub)
else:
elif len(sub) > len(string) :
return -1
def indexOf(string,sub) :
'''
