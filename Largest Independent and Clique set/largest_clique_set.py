import pdb
import operator
import copy
import random
import time


def largest_clique_set(node,dict_adj_list,Adj_Matrix):
	
	node_value_list = []
	
	
	for value in dict_adj_list[node]:
		node_value_list.append(value)
	
	for val in node_value_list:
		value_val_list = []
		for value_key in dict_adj_list[val]:
			value_val_list.append(value_key)
		clique_set = []
		for nodes in node_value_list:
			
			for value_node in value_val_list:
				
				if nodes == value_node :
					if value_node not in clique_set:
						if clique_set:
							flag = 0
							for clique_node in clique_set:
								if value_node not in dict_adj_list[clique_node]:
									flag = 1
							if flag == 0:
								clique_set.append(value_node)
						else:
							clique_set.append(value_node)
		
				
		clique_set.append(node)
				
		clique_set.append(val)			
		#print "Clique set is %s" %(clique_set)
	return clique_set
		

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
	#Adj_Matrix = [[0,1,0,1,1,0,0],[1,0,1,1,0,1,0],[0,1,0,1,1,1,1],[1,1,1,0,1,1,0],[1,0,1,1,0,1,0],[0,1,1,1,1,0,0],[0,0,1,0,0,0,0]]
	#Adj_Matrix= [[0,0,1,0,0,1,0,1,1,0,0],[0,0,1,1,1,0,0,1,1,0,1],[1,1,0,1,1,0,1,0,1,0,1], [0,1,1,0,1,0,1,1,1,0,0],[0,1,1,1,0,1,1,0,1,1,0],[1,0,0,0,1,0,1,1,1,1,1],[0,0,1,1,1,1,0,1,1,0,0],[1,1,0,1,0,1,1,0,1,0,1],[1,1,1,1,1,1,1,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1],[0,1,1,0,0,1,0,1,1,1,0]]
	
	dict_adj_list = {}
	
	for i in range(0,len(Adj_Matrix)):
		adj_list = []
		for j in range (0,len(Adj_Matrix)):
			if Adj_Matrix[i][j]!=0:
				adj_list.append(j+1)
			dict_adj_list[i+1]=adj_list
	
	clique_final_set = []
	all_nodes = range(1,len(Adj_Matrix)+1)
	for node in all_nodes:
		clique_final=largest_clique_set(node,dict_adj_list,range(1,len(Adj_Matrix)+1))
		clique_final_set.append(clique_final)
	
	
	previous_count = 0
	for list in clique_final_set:
		count = 0
		for value in list:
			count = count + 1
		
		if count > previous_count:
			previous_count = count
			largest_set = list
		else:
			previous_count = count
			
	print "Largest Clique Set is %s" %(largest_set)
	Execution_Stop_Time=time.time()
	print("Time for calculating Largest Clique Set is %s")%(Execution_Stop_Time-Execution_Start_Time)

if __name__ == "__main__":
	independent_set_values = []
	main()