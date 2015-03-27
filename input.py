"""
Input

3/26/15
Albert Liang

Just a quick check to make sure input can be taken in from the user through the console.
On the side, it also tests conditionals.
"""
while(True):
    s = raw_input("Enter string to print: ")
    print s,"\n"
    if(s.lower() == "exit"):
        break
print "Exiting..."

