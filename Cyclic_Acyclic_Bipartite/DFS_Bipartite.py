import pdb


def depth_first_bipartite(node,dict_adj_list,visited_parent_node):
	
	global set_1
	global set_2
	
	for value in dict_adj_list[node]:
		if value not in visited_parent_node:
			if node in set_1:
				set_2.append(value)
			else:
				set_1.append(value)
			visited_parent_node.append(value)
			if (depth_first_bipartite(value,dict_adj_list,visited_parent_node)) == False:
				return False		
		elif value in set_1 and node in set_1 or value in set_2 and node in set_2:
			return False
	return True
			
	
if __name__ == '__main__':
	#Adj_Matrix = [[0,5,4,0,0,0,0],[5,0,0,0,0,0,0],[4,0,0,0,0,9,7],[0,0,0,0,0,0,1],[0,0,0,0,0,0,3],[0,0,9,0,0,0,0],[0,0,7,1,3,0,0]]
	#Adj_Matrix = [[0,21,0,0,0,0,0,0,29,0],[21,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,24,0],[0,0,0,0,16,0,0,0,0,10],[0,0,0,16,0,0,24,0,7,0],[0,0,0,0,0,0,5,0,23,8],[0,0,0,0,24,5,0,13,0,0],[0,0,0,0,0,0,13,0,13,0],[29,0,24,0,7,23,0,13,0,0],[0,0,0,10,0,8,0,0,0,0]]
	Adj_Matrix = [[0,0,0,16,12,20,18,10,0,0,18,0,0,0,28],[0,0,0,17,24,14,0,0,0,23,10,6,0,26,20],[0,0,0,0,19,0,0,0,0,0,0,0,26,14,0],[16,17,0,0,0,15,0,23,0,0,0,0,0,24,28],[12,24,19,0,0,0,0,0,0,0,21,0,9,29,0],[20,14,0,15,0,0,0,9,6,0,26,0,0,20,0],[18,0,0,0,0,0,0,0,0,0,13,15,0,0,5],[10,0,0,23,0,9,0,0,8,14,17,0,12,0,0],[0,0,0,0,0,6,0,8,0,0,0,29,22,0,28],[0,23,0,0,0,0,0,14,0,0,20,0,18,0,25],[18,10,0,0,21,26,13,17,0,20,0,0,11,22,16],[0,6,0,0,0,0,15,0,29,0,0,0,0,14,24],[0,0,26,0,9,0,0,12,22,18,11,0,0,0,22],[0,26,14,24,29,20,0,0,0,0,22,14,0,0,0],[28,20,0,28,0,0,5,0,28,25,16,24,22,0,0]]
	
	dict_adj_list = {}
	
	for i in range(0,len(Adj_Matrix)):
		adj_list = []
		for j in range (0,len(Adj_Matrix)):
			if Adj_Matrix[i][j]!=0:
				adj_list.append(j+1)
			dict_adj_list[i+1]=adj_list
	
	visited_parent_node = [1]
	set_1 = [1]
	set_2 = []
	
	if (depth_first_bipartite(1,dict_adj_list,visited_parent_node)) == True:
		print "The graph is Bipartite"
	else:
		print "The graph is not Bipartite"
	                                                      