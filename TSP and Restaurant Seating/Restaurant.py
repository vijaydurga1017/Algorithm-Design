import pdb
import operator
import copy
import random
import time

def restaurant_seating_arrangement(family_size,table_size):

	table_arrangement=[]
	
	family_length=len(family_size)
	table_length=len(table_size)
	
	for i in range(0,family_length):
		table_arrangement.append([])
		for j in range(0,table_length):
			table_arrangement[i].append(0)
	
	temp = []
	for values in table_size:
		temp.append(values)
			
	family_index=0
	for family_len in family_size:
		unvisited_tables=[]
		unvisited_index=[]
		for j in range(0,table_length):
			table=temp[j]
			unvisited_tables.append(table)
			unvisited_index.append(j)
		#print unvisited_tables
		while (unvisited_tables):
			if family_len > 0:
				max_table_size=max(unvisited_tables)
				#print max_table_size
				#index_max_table=table_size.index(max_table_size)
				index_max_table=[i for i, x in enumerate(temp) if x == max_table_size]
				for k in index_max_table:
					if k in unvisited_index and family_len > 0:
						table_arrangement[family_index][k] = 1
						family_len=family_len-1
						unvisited_tables.remove(max_table_size)
						#print unvisited_tables
						if not unvisited_tables and family_len > 0:
							print "Seating not possible"
							return
						temp[k] = temp[k] - 1
						if temp[k] < 0:
							print "Seating not possible"
							return
						unvisited_index.remove(k)
			else:
				break;

		family_index=family_index+1
	
	for val in table_arrangement:
		print val
	
	
def main():

	#family_size=[3, 2, 2]
	#table_size=[1,1,3,2]
	
	#family_size = [4, 3, 1, 9, 8]
	#table_size =[5, 6, 7, 1, 2, 9]
	
	#family_size=[3,3,2]
	#table_size=[4,2,1,3]
	
	family_size = [8,8,5,5,3,2,7]
	table_size = [5,7,2,8,1,6,2,5,3]
	
	
	
	restaurant_seating_arrangement(family_size,table_size)	

if __name__ == "__main__":
	main()