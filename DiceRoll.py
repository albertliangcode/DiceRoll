"""
Dice Roll

3/26/15
Albert Liang

Simulates the rolling of any number of six-sided dice.
User selects how many dice to roll at the start of each iteration.
The dice are rolled and recorded as a list, which is then printed to the console.
The program loops until the user enters "q" instead of a dice count.
"""
from random import *

# Main Program =================================================================
def main():
    print "Welcome to Dice Roll!\n"
    wFile_name = raw_input( "Please enter name of file to save results to: " )
    print ""

    while(True):
        count = raw_input( "How many dice? (\"q\" to quit): " )
        if( count.lower() == 'q' ):
            break
        elif( not( StringRepInt(count) ) ):
            print( "Please enter an integer count, or q.\n" )
        elif( int(count) < 1 ):
	    print( "Please enter a dice count greater than zero.\n" )
        else:
            result = []
            for i in range( int(count) ):
	        roll = randint(1,6)
	        result.append(roll)
	    print "Results: ", result, "\n"
	    with open( wFile_name,'w+') as writeFile:
		writeFile.write('Results of last dice roll:\n')
		writeFile.write('====================================\n')
		for num in result:
		    writeFile.write( str(num) + '\n' )

    print ("Exiting...\n\n")

# Check if String Represents an Integer ========================================
# (From Stackoverflow)
def StringRepInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# ==============================================================================
# Run ==========================================================================
main()

