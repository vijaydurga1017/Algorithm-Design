import operator
import copy
import random
import time

def dijkstras_shortest_path_source_dest(graph_matrix,start_vertex,end_vertex):
    dist={}
    nodes=len(graph_matrix)
    
    sample_matrix=[]
    for node in range(0,nodes):
        if node+1 == start_vertex :
            dist[start_vertex]=0
            sample_matrix.append(dist[start_vertex])                      
        else :
            dist[node+1]=9999
            sample_matrix.append(dist[node+1])

        

    marked_list = []
    marked_dict = {}
	
	Execution_Start_Time=time.time()
	
    for i in range(1,nodes):
        search_matrix = copy.copy(sample_matrix[(i-1)*nodes:((i-1)*nodes)+nodes])
        if marked_list:
            for ele in marked_list:
                search_matrix.remove(ele)
        marked_min_value=min(search_matrix)
        marked_list.append(marked_min_value)
        
        if start_vertex == 1:
            sample_matrix.append(0)
        else:
            sample_matrix.append(dist[nodes])

        marked_index = [z for z, x in enumerate(sample_matrix[(i-1)*nodes:((i-1)*nodes)+nodes]) if x == marked_min_value]
        prev_index_val = ""
        if len(marked_index) > 1:
            for element in marked_index:
                if prev_index_val == element:
                    marked_index.remove(prev_index_val)
        marked_index = marked_index[0]

        prev_index_val = marked_index
        for j in range(0,nodes-1):
            if graph_matrix[marked_index][j+1] != 0:
                var = marked_min_value+graph_matrix[marked_index][j+1]
            else:
                var = sample_matrix[((i-1)*nodes) + (j+1)]
            
            minimum_value=min(sample_matrix[((i-1) * nodes) + (j+1)],var)
            sample_matrix.append(minimum_value)
    
	Execution_Stop_Time=time.time()

    print("Time for calculating shortest path is %s")%(Execution_Stop_Time-Execution_Start_Time)
	
	rem_val = set(sample_matrix[(nodes-1)*nodes:(nodes*nodes)]) - set(marked_list)

    end_row=sample_matrix[(nodes-1)*nodes:(nodes*nodes)]
    print(end_row)
    cost_of_path=end_row[end_vertex-1]     
    cost_of_path_check=cost_of_path

    cost_index=sample_matrix[(nodes-1)*nodes:(nodes*nodes)].index(cost_of_path)
    mid_node = []

    k = cost_index
    index_pos = cost_index
    print"Index pos is", index_pos
    for j in range(nodes-1,-1,-1):
        if cost_of_path_check != sample_matrix[j*nodes+k]:
            value = marked_list[j]
            indexes = [z for z, x in enumerate(sample_matrix[i*nodes:(i*nodes)+nodes]) if x == value]
            index_pos = indexes[-1]
            if index_pos == 0:
                mid_node.append(start_vertex)
            else:
                mid_node.append(index_pos + 1)
            k = index_pos
            cost_of_path_check=value
    
    
    if end_vertex in mid_node:
        mid_node.reverse()
    else:
        mid_node.reverse()
        mid_node.append(end_vertex)
    return [cost_of_path,mid_node]

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
	#graph_matrix=Generate_Random_Matrix(N)
    #graph_matrix = [[0,10,5,0,0,0],[10,0,8,12,6,0],[5,8,0,0,12,0],[0,12,0,0,5,4],[0,6,12,5,0,6],[0,0,0,4,6,0]]
    graph_matrix = [[0,0,0,29,0,0,0,0],[0,0,0,0,0,11,11,0],[0,0,0,12,0,5,5,0],[29,0,12,0,5,0,13,0],[0,0,0,5,0,0,7,11],[0,11,5,0,0,0,0,17],[0,11,5,13,7,0,0,0],[0,0,0,0,11,17,0,0]]
    #graph_matrix = [[0,11,14,0,8,0,29,28,0,0,14,0],[11,0,12,0,6,0,0,0,0,0,0,0],[14,12,0,18,13,13,0,0,25,0,0,16],[0,0,18,0,0,0,27,17,9,25,0,0],[8,6,13,0,0,0,0,0,0,0,0,22],[0,0,13,0,0,0,0,15,5,0,0,0],[29,0,0,27,0,0,0,0,0,0,0,0],[28,0,0,17,0,15,0,0,5,9,0,0],[0,0,25,9,0,5,0,5,0,0,25,0],[0,0,0,25,0,0,0,9,0,0,0,0],[14,0,0,0,0,0,0,0,25,0,0,0],[0,0,16,0,22,0,0,0,0,0,0,0]]
    first_vertex = raw_input("Enter Start Vertex: ")
    second_vertex = raw_input("Enter End Vertex: ")
    if first_vertex > second_vertex:
        start_vertex = int(second_vertex)
        end_vertex = int(first_vertex)
        flag = 1
    else :
        start_vertex = int(first_vertex)
        end_vertex = int(second_vertex)
        flag=0
    result=dijkstras_shortest_path_source_dest(graph_matrix,start_vertex,end_vertex)
    path_cost=result[0]

    if flag:
        path_traversed=result[1]
        path_traversed.reverse()
        
    else:
        path_traversed=result[1]

    print ("The shortest path cost from %s to %s is %s" % (first_vertex,second_vertex,path_cost))
    print ("The path is %s" %(path_traversed))
  

if __name__ == "__main__":
   main()