import pdb


def depth_first_cyclic_acyclic(node,dict_adj_list,visited_parent_node,last_parent_node):
	
	for value in dict_adj_list[node]:
		if value in visited_parent_node:
			if value != last_parent_node:
				return True
		else :
			visited_parent_node.append(value)
			last_parent_node = node
			depth_first_cyclic_acyclic(value,dict_adj_list,visited_parent_node,last_parent_node)
	
if __name__ == '__main__':
	#Adj_Matrix= [[0,12,14,0,0,0,0,20],[12,0,10,6,28,0,0,0],[14,10,0,0,0,11,0,0],[0,6,0,0,0,0,19,0],[0,28,0,0,0,0,0,0],[0,0,11,0,0,0,0,0],[0,0,0,19,0,0,0,24],[20,0,0,0,0,0,24,0]]
	#Adj_Matrix = [[0,5,6,0,0,0],[5,0,0,7,8,9],[6,0,0,0,0,0],[0,7,0,0,0,0],[0,8,0,0,0,0],[0,9,0,0,0,0]]
	Adj_Matrix = [[0,0,24,0,0,0,0,0,5,0,17,0,24,0,0],[0,0,0,0,20,24,10,5,17,0,15,0,0,0,0],[24,0,0,0,0,0,0,0,28,0,0,14,10,0,0],[0,0,0,0,26,0,26,0,0,22,0,0,0,6,22],[0,20,0,26,0,0,0,0,26,0,0,17,0,0,11],[0,24,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,10,0,26,0,0,0,0,7,0,0,7,0,0,0],[0,5,0,0,0,0,0,0,0,18,20,16,0,0,0],[5,17,28,0,26,0,7,0,0,0,24,7,0,0,0],[0,0,0,22,0,0,0,18,0,0,0,0,0,19,0],[17,15,0,0,0,0,0,20,24,0,0,0,0,0,19],[0,0,14,0,17,0,7,16,7,0,0,0,0,0,0],[24,0,10,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,6,0,0,0,0,0,19,0,0,0,0,27],[0,0,0,22,11,0,0,0,0,0,19,0,0,27,0]]
	dict_adj_list = {}
	
	for i in range(0,len(Adj_Matrix)):
		adj_list = []
		for j in range (0,len(Adj_Matrix)):
			if Adj_Matrix[i][j]!=0:
				adj_list.append(j+1)
			dict_adj_list[i+1]=adj_list
	
	visited_parent_node = [1]
	last_parent_node = [1]
	
	if (depth_first_cyclic_acyclic(1,dict_adj_list,visited_parent_node,last_parent_node)) == True:
		print "Yes, the graph contains a circle"
	else:
		print "No, the graph doesn't contain circle"
	