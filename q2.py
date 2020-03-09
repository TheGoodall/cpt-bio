import sys, time
from graphviz import Digraph



def UPGMA(fileName):

    #starting timer
    start = time.time()

    #Opening file
    with open(fileName, 'r') as file1:
        matrix_string = file1.read()

    #converting matrix into 2 dimensional array
    matrix = matrix_string.split("\n")
    matrix = [digit.split(" ") for digit in matrix]

    distance_up = {}

    #creating graph

    dot = Digraph()
    top = Digraph()
    top.attr(rank="same")

    for species in matrix[0][1:]:
        top.node(species)
        distance_up[species] = 0
    dot.subgraph(top)

    


    #Main Loop
    while len(matrix) > 2:

        # Find smallest non-zero distance
        min_i = 1
        min_j = 1
        minsize = int(matrix[1][1])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix)):
                if (int(matrix[j][i]) < minsize and int(matrix[j][i]) != 0 ) or minsize == 0:
                    minsize = int(matrix[j][i])
                    min_i = i
                    min_j = j

        node1 = matrix[0][min_i]
        node2 = matrix[min_j][0]
        nodename = ''.join(sorted(node1+node2))
        distance_up[nodename] = minsize/2

        #create node/edges
        dot.node(nodename)
        dot.edge(nodename, node1, str(minsize/2-distance_up[node1]))
        dot.edge(nodename, node2, str(minsize/2-distance_up[node2]))


        # add new node to the matrix
        matrix.append([nodename]+[((int(matrix[i][min_i])*len(node1))+int((matrix[i][min_j]))*len(node2))/len(nodename) for i in range(1, len(matrix))])
        for i in range(len(matrix)-1):
            matrix[i].append(matrix[-1][i])
        matrix[-1].append(0)

        #remove the old nodes from the matrix
        to_be_removed = [min_i, min_j]

        #ensure that deletion is done downwards so that indexes dont change
        to_be_removed.sort(reverse=True)

        for i in to_be_removed:
            del matrix[i]
            for j in range(len(matrix)):
                del matrix[j][i]
        
        for i in matrix:
            for j in i:
                tbp = str(j)
                pad = 8-len(tbp)
                print(tbp+' '*pad, end='')
            print()
        print("-----------")

        

    dot.render("q2", format="png")
    stop = time.time()
    time_taken=stop-start

    print("time taken: "+str(time_taken))
UPGMA("matrix2.txt")