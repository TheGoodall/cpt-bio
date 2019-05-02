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



def c(i, j):
    if seq1[i] == seq2[j]:
        return {"A":4, "C":3, "G":2, "T":1}[seq1[i]]
    else:
        return -3

x = len(seq1)
y = len(seq2)
scoring_matrix = [["" for i in range(x)] for j in range(y)]
backtrack_matrix = [["" for i in range(x)] for j in range(y)]

for i in range(x):
    scoring_matrix[0][i] = -2*i
    backtrack_matrix[0][i] = "L"
for i in range(y):
    scoring_matrix[i][0] = -2*i
    backtrack_matrix[i][0] = "U"
backtrack_matrix[0][0] = "END"



for i in range(1,x):
    for j in range(1,y):

        ma = c(i, j) + scoring_matrix[j-1][i-1]

        mb = scoring_matrix[j][i-1]-2
        mc = scoring_matrix[j-1][i]-2

        maxsize = ma
        biggest = 1
        if mb>ma:
            maxsize = mb
            biggest = 2
        if mc > maxsize:
            maxsize = mc
            biggest = 3
        scoring_matrix[j][i] = maxsize

        if biggest == 1:
            backtrack_matrix[j][i] = "D"
        elif biggest == 2:
            backtrack_matrix[j][i] = "L"
        else:
            backtrack_matrix[j][i] = "U"



best_score = scoring_matrix[y-1][x-1]

a = ""
b = ""

i = x-1
j = y-1


while 1:
    letter = backtrack_matrix[j][i]
    if letter == "U":
        a = " " + a
        b = seq2[-1] + b
        seq2 = seq2[:-1]
        j -= 1
    elif letter == "D":
        a = seq1[-1] + a
        b = seq2[-1] + b
        seq1 = seq1[:-1]
        seq2 = seq2[:-1]
        i -= 1
        j -= 1
    elif letter == "L":
        a = seq1[-1] + a
        b = " " + b
        seq1 = seq1[:-1]
        i -= 1




    elif letter == "END":
        break
    

best_alignment= [a, b]





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

