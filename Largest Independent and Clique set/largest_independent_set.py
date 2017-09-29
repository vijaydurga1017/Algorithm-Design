import pdb
import operator
import copy
import random
import time


def largest_independent_set(node,dict_adj_list,Adj_Matrix):
		global independent_set_values
		temp_nodes = Adj_Matrix
		unvisited_nodes = range(1,len(Adj_Matrix)+1)
		while (unvisited_nodes):
			for values in dict_adj_list[node]:
				if values in temp_nodes:
					temp_nodes.remove(values)
					unvisited_nodes.remove(values)
			unvisited_nodes.remove(node)
			if unvisited_nodes:
				node = unvisited_nodes[0]
		independent_set_values.append(temp_nodes)
		return

def Generate_Random_Matrix(N):
    matrix=[]
    for i in range(0,N):
        matrix.append([])
        for j in range(0,N):
            matrix[i].append(0)
    for i in range(0,N):
        for j in range(0,N):
            if i != j:
                out=random.randint(0,1)
                matrix[i][j]=matrix[j][i]=out
    return matrix
			
def main():

	Execution_Start_Time=time.time()
	N = int(input("Enter the number of nodes for the matrix: "))
	Adj_Matrix=Generate_Random_Matrix(N)
	#Adj_Matrix= [[0,0,1,0,0,1,0,1,1,0,0],[0,0,1,1,1,0,0,1,1,0,1],[1,1,0,1,1,0,1,0,1,0,1], [0,1,1,0,1,0,1,1,1,0,0],[0,1,1,1,0,1,1,0,1,1,0],[1,0,0,0,1,0,1,1,1,1,1],[0,0,1,1,1,1,0,1,1,0,0],[1,1,0,1,0,1,1,0,1,0,1],[1,1,1,1,1,1,1,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1],[0,1,1,0,0,1,0,1,1,1,0]]
	#Adj_Matrix = [[0,1,0,1,1,0,0],[1,0,1,1,0,1,0],[0,1,0,1,1,1,1],[1,1,1,0,1,1,0],[1,0,1,1,0,1,0],[0,1,1,1,1,0,0],[0,0,1,0,0,0,0]]
	
	dict_adj_list = {}
	
	for i in range(0,len(Adj_Matrix)):
		adj_list = []
		for j in range (0,len(Adj_Matrix)):
			if Adj_Matrix[i][j]!=0:
				adj_list.append(j+1)
			dict_adj_list[i+1]=adj_list
	
	all_nodes = range(1,len(Adj_Matrix)+1)
	for node in all_nodes:
		largest_independent_set(node,dict_adj_list,range(1,len(Adj_Matrix)+1))
	
	previous_count = 0
	for list in independent_set_values:
		count = 0
		for value in list:
			count = count + 1
		
		if count > previous_count:
			previous_count = count
			largest_set = list
		else:
			previous_count = count
			
	print "Largest Independent Set is %s" %(largest_set)
	Execution_Stop_Time=time.time()
	print("Time for calculating Largest Independent Set is %s")%(Execution_Stop_Time-Execution_Start_Time)

if __name__ == "__main__":
	independent_set_values = []
	main()