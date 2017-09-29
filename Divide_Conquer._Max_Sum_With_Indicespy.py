
N = [-20,13,-9,45,9,12,-200,15,40,32,44,43,41]

def find_maximum_sum(n):

    max_sum = max(n)
    i = j = n.index(max_sum)

    #print(i)
    sum = max_sum

    right_index = i+1
    if i == len(n)-1:
        right_index = len(n)
    left_index = 1

    for ind in range(i,0,-1):
        sum = sum + n[ind-1]
        if (sum >= max_sum):
            max_sum = sum
            left_index = ind
        if left_index == 1:
            left_index = i+1
    
    sum = max_sum
    for ind in range(j+1,len(n)):
        sum = sum + n[ind]
        if (sum > max_sum):
            max_sum = sum
            right_index = ind+1

    
    return(max_sum,left_index,right_index)

def find_mid_sum(left_sum,c,left_j,right_j):
    sum = left_sum
    max_mid_sum = left_sum
    mid_max_j = left_j
    for y in range(left_j,right_j):
        #print("c[y] is", c[y])
        sum = sum + c[y]
        if sum > max_mid_sum:
            max_mid_sum = sum
            mid_max_j = y+1
    return(max_mid_sum,mid_max_j)


def main():
    N=[-20,13,-9,45,9,12,-200,15,40,32,44,43,41]
    val = 0
    for i in range(0,len(N)):
        if N[i] > 0:
            val = 1


    if val == 0:
        print("All numbers are negative")
        max_sum = max(N)
        print("Maximal Sub array",max_sum,"Index i",N.index(max_sum)+1,"Index j",N.index(max_sum)+1)
        exit()

    val = 0
    for i in range(0,len(N)):
        if N[i] < 0:
            val = 1


    sum = 0
    if val == 0:
        print("All numbers are positive")
        for i in range(0,len(N)):
            sum = sum + N[i]
        print("Maximal Sub array",sum,"Index i",1,"Index j",len(N))
        exit()
        

    length = len(N)
    mid_val = round(len(N)/2)

    list1 = N[0:mid_val]
    list2 = N[mid_val:length]

    left_max_val,left_i,left_j = find_maximum_sum(list1)

    right_max_val,right_i,right_j = find_maximum_sum(list2)
    right_i = right_i + mid_val
    right_j = right_j + mid_val

    mid_max_sum,mid_j = find_mid_sum(left_max_val,N,left_j,right_j) 
    mid_i = left_i

    if max(left_max_val,right_max_val,mid_max_sum)==left_max_val:
        print ("Maximal Sub array",left_max_val,"Index i",left_i,"Index j",left_j)

    if max(left_max_val,right_max_val,mid_max_sum)==right_max_val:
        print ("Maximal Sub array",right_max_val,"Index i",right_i,"Index j",right_j)

    if max(left_max_val,right_max_val,mid_max_sum)==mid_max_sum:
        print ("Maximal Sub array",mid_max_sum,"Index i",mid_i,"Index j",mid_j)

main()