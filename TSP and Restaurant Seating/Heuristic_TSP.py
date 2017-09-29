import pdb
import operator
import copy
import random
import time

def heuristic_TSP(Adj_Matrix,dict_adj_list,start_node,next_node):
	visited_nodes = [start_node]
	path = [start_node]
	node_value_list = []
	for dist in dict_adj_list[start_node]:
			node_value_list.append(dist)
	min_dist = min(i for i in node_value_list if i > 0)
	index_min_dist = node_value_list.index(min_dist)
	cost = min_dist
	while len(visited_nodes) != len(Adj_Matrix) :
		next_node=index_min_dist+1
		visited_nodes.append(next_node)
		minimum_dist = []
		node_value_list = []
		
		for node_dist in dict_adj_list[next_node]:
			node_value_list.append(node_dist)
			index=dict_adj_list[next_node].index(node_dist)
			if index+1 not in visited_nodes:
				minimum_dist.append(node_dist)
		if not minimum_dist:
			return [visited_nodes,cost]
		min_dist = min(i for i in minimum_dist if i > 0)
		cost = cost + min_dist
		index_min_dist = node_value_list.index(min_dist)
	
	
	
def main():
	#Adj_Matrix = [[0,23,15,26],[23,0,25,19],[15,25,0,11],[26,19,11,0]]
	Adj_Matrix = [[0,0,0,0,14,13,12,0,6],[0,0,0,16,26,6,22,26,10],[0,0,0,11,13,7,0,23,14],[0,16,11,0,10,9,0,0,9],[14,26,13,10,0,28,20,0,0],[13,6,7,9,28,0,23,0,25],[13,22,0,0,20,23,0,10,21],[0,26,23,0,0,0,10,0,20],[6,10,14,9,0,25,21,20,0]]
	
	dict_adj_list = {}
	start_node=4
	next_node=4
	for i in range(0,len(Adj_Matrix)):
		adj_list = []
		for j in range (0,len(Adj_Matrix)):
			adj_list.append(Adj_Matrix[i][j])
			dict_adj_list[i+1]=adj_list
	final_path = []
	path_dist = heuristic_TSP(Adj_Matrix,dict_adj_list,start_node,next_node)
	path = path_dist[0]
	last_node = path[-1]
	cost = path_dist[1]
	dist = Adj_Matrix[start_node-1][last_node-1]
	path.append(start_node)
	final_cost=cost+dist
	
	print "The TSP path is %s with a total distance of %s" %(path,final_cost)

if __name__ == "__main__":
	main()