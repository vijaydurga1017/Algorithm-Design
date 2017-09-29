import operator
import copy
import random
import time


def floyd_shortest_path_One_D(graph_matrix,start_vertex,end_vertex) :

    Nodes=len(graph_matrix)
    floyd_OneD_Matrix=[]
    floyd_Path_OneD=[]
	
	Execution_Start_Time=time.time()

    for i in range(Nodes):
        for j in range(Nodes):
            floyd_Path_OneD.append(j)
            if(i==Nodes-1 & j==Nodes-1):
                continue
            floyd_Path_OneD[i*(i-1)/2+j] = j

    for i in range(Nodes):
        for j in range(Nodes):
            floyd_OneD_Matrix.append(0)
            if graph_matrix[i][j] == 0:
                floyd_OneD_Matrix[i*(i-1)/2+j]=9999
                
            else:
                floyd_OneD_Matrix[i*(i-1)/2+j]=graph_matrix[i][j]
    
	Execution_Stop_Time=time.time()

    print("Time for Adjacency Matrix Creation is %s")%(Execution_Stop_Time-Execution_Start_Time)
    
    Execution_Start_Time=time.time()	

    for k in range(Nodes) :
        for m in range(len(graph_matrix)) :
            for n in range(len(graph_matrix)) :
                if (m==n | (m==Nodes-1 & n==Nodes-1) | (m==Nodes-1 & k==Nodes-1) | (n==Nodes-1 & k==Nodes-1)):
                    continue
                if floyd_OneD_Matrix[m*(m-1)/2+n] > floyd_OneD_Matrix[m*(m-1)/2+k] + floyd_OneD_Matrix[k*(k-1)/2+n]:
                    print "Value of m is %s, n is %s, k is %s"%(m,n,k)
                    floyd_OneD_Matrix[m*(m-1)/2+n] = floyd_OneD_Matrix[m*(m-1)/2+k] + floyd_OneD_Matrix[k*(k-1)/2+n]
                    print "Min value is %s"%(floyd_OneD_Matrix[m*(m-1)/2+n])
                    floyd_Path_OneD[m*(m-1)/2+n]=floyd_Path_OneD[m*(m-1)/2+k]
                        

    cost_of_path=floyd_OneD_Matrix[start_vertex-1][end_vertex-1]
	
	Execution_Stop_Time=time.time()

    print("Time for calculating shortest path is %s")%(Execution_Stop_Time-Execution_Start_Time)

    return cost_of_path,floyd_Path_OneD

def Traversed_Path(next, start, end) :
    if next[start-1][end-1] == None :
        return []
    path = [start]
    start=start-1
    end=end-1
    while start != end :
        start = next[start][end]
        path.append(start+1)
    return path

def Generate_Random_Matrix(N):
    matrix=[]
    for i in range(0,N):
        matrix.append([])
        for j in range(0,N):
            matrix[i].append(0)
    for i in range(0,N):
        for j in range(0,N):
            if i != j:
                out=random.randint(0,50)
                matrix[i][j]=matrix[j][i]=out
            
    return matrix


def main():
    #N = int(input("Enter the number of nodes for the matrix: "))
    first_vertex = int(input("Enter Start Vertex: "))
    second_vertex = int(input("Enter End Vertex: "))
    
    #graph_matrix=Generate_Random_Matrix(N)
    #graph_matrix = [[0,10,5,0,0,0],[10,0,8,12,6,0],[5,8,0,0,12,0],[0,12,0,0,5,4],[0,6,12,5,0,6],[0,0,0,4,6,0]]
    graph_matrix = [[0,0,0,29,0,0,0,0],[0,0,0,0,0,11,11,0],[0,0,0,12,0,5,5,0],[29,0,12,0,5,0,13,0],[0,0,0,5,0,0,7,11],[0,11,5,0,0,0,0,17],[0,11,5,13,7,0,0,0],[0,0,0,0,11,17,0,0]]
    #graph_matrix = [[0,11,14,0,8,0,29,28,0,0,14,0],[11,0,12,0,6,0,0,0,0,0,0,0],[14,12,0,18,13,13,0,0,25,0,0,16],[0,0,18,0,0,0,27,17,9,25,0,0],[8,6,13,0,0,0,0,0,0,0,0,22],[0,0,13,0,0,0,0,15,5,0,0,0],[29,0,0,27,0,0,0,0,0,0,0,0],[28,0,0,17,0,15,0,0,5,9,0,0],[0,0,25,9,0,5,0,5,0,0,25,0],[0,0,0,25,0,0,0,9,0,0,0,0],[14,0,0,0,0,0,0,0,25,0,0,0],[0,0,16,0,22,0,0,0,0,0,0,0]]
    
    #print graph_matrix

    result=floyd_shortest_path_One_D(graph_matrix,first_vertex,second_vertex)

    path_cost=result[0]

    path_traversed = Traversed_Path(result[1],first_vertex,second_vertex)
    
    print ("The shortest path cost from %s to %s is %s" % (first_vertex,second_vertex,path_cost))
    print ("The path is %s" %(path_traversed))


if __name__ == "__main__":
   main()