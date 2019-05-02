#!/usr/bin/python
import time
import sys


# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix



# ------------------------------------------------------------



# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 

scoring_matrix = [["" for j in range(len(seq2)+1)] for i in range(len(seq1)+1)]
backtrack_matrix = [["" for j in range(len(seq2)+1)] for i in range(len(seq1)+1)]

def bt(i, j, x):
    pass

def c(i, j):
    if seq1[i] == seq2[j]:
        return 2
    else:
        return -1

def s(i, j):
    print(i,j)
    if i == 0:
        return 2*j
    elif j == 0:
        return 2*i
    ma = c(i,j) + s(i-1, j-1)
    mb = s(i-1, j)-2
    mc = s(i, j-1)-2

    print( ma, mb, mc)

    if ma > mb and ma > mc:
        bt(i,j, "D")
        return ma
    elif mb > ma and mb > mc:
        bt(i, j, "U")
        return mb
    else:
        bt(i, j, "L")
        return mc



best_score = s(len(seq1)-1, len(seq2)-1)


best_alignment= ["AATT", "AATT"]


#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

