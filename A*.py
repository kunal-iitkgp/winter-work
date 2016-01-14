import Queue as Q
import numpy
from math import sqrt

start_x,start_y = [ int(i) for i in raw_input().strip().split()]
end_x,end_y = [ int(i) for i in raw_input().strip().split()]
r,c = [ int(i) for i in raw_input().strip().split()]

grid=[]
for i in xrange(0,r):
	grid.append(raw_input().strip().split())

visited=numpy.zeros((r,c))

grid=numpy.array(grid)

#print grid 
print visited
print grid

list_q=Q.PriorityQueue()

class node(object):
    def __init__(self, f_cost,g_cost,h_cost, (p_x,p_y),(c_x,c_y) ):
        self.f_cost = f_cost
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.parent = (p_x,p_y)
        self.location= (c_x,c_y)
        #print 'New Level:', description
        

    def __cmp__(self, other):
        return cmp(self.f_cost, other.f_cost)

#node_xy=numpy.empty((r,c), dtype=node)

def MoveCost((x_1,y_1),(x_2,y_2)):
	return int(sqrt((x_2-x_1)**2 + (y_2 - y_1)**2) * 10)

def heuristicCost(x,y):
	global end_x,end_y
	return abs(end_x - x) + abs(end_y - y)

start_node = node( heuristicCost(start_x,start_y) , 0 , heuristicCost(start_x,start_y) , (start_x,start_y),(start_x,start_y) )

#print start_node.f_cost
#p_x,p_y=start_node.parent
list_q.put(start_node)


while 1:
	current_node = list_q.get()
	x,y=current_node.location
	visited[x][y]=1
	temp_node = node(current_node.f_cost,current_node.g_cost,current_node.h_cost,current_node.location,current_node.parent)
	if current_node.location== (end_x,end_y):
		break

	else :
		if  y<c-1 :
			if (grid[x][y+1]!='%' ) :
				if visited[x][y+1]==0:
					#isited[x][y+1]=1
					temp_node.h_cost = heuristicCost(x,y+1)
					temp_node.g_cost = current_node.g_cost + MoveCost((x,y+1),(x,y))
					temp_node.f_cost = temp_node.h_cost + temp_node.g_cost
					temp_node.parent = current_node.location
					temp_node.location = (x,y+1)
					list_q.put(temp_node)
				    

				else :
					for item in list_q:
					    if item.location == (x,y) :
					    	upd_g = current_node.g_cost + MoveCost((x,y+1),(x,y))
					    	if  upd_g < item.g_cost:
					    		item.g_cost = upd_g
					    		item.f_cost = item.h_cost + item.g_cost
					    		item.parent =  current_node.location
					    		break
					    	else :
					    		break 




				

				
				
		if x>0:
			if (grid[x-1][y]!='%' ):  
				if visited[x-1][y]==0:
					#visited[x-1][y]=1
					temp_node.h_cost = heuristicCost(x-1,y)
					temp_node.g_cost = current_node.g_cost + MoveCost((x-1,y),(x,y))
					temp_node.f_cost = temp_node.h_cost + temp_node.g_cost
					temp_node.parent = current_node.location
					temp_node.location = (x-1,y)
					list_q.put(temp_node)

				else :
					for item in list_q:
					    if item.location == (x,y) :
					    	upd_g = current_node.g_cost + MoveCost((x,y-1),(x,y))
					    	if  upd_g < item.g_cost:
					    		item.g_cost = upd_g
					    		item.f_cost = item.h_cost + item.g_cost
					    		item.parent =  current_node.location
					    		break
					    	else :
					    		break 

				
				
			
				
		if x<r-1:
			if (grid[x+1][y]!='%' )  :
				if visited[x+1][y]==0:
					#visited[x+1][y]=1
					temp_node.h_cost = heuristicCost(x+1,y)
					temp_node.g_cost = current_node.g_cost + MoveCost((x+1,y),(x,y))
					temp_node.f_cost = temp_node.h_cost + temp_node.g_cost
					temp_node.parent = current_node.location
					temp_node.location = (x+1,y)
					list_q.put(temp_node)

				else :
					for item in list_q:
					    if item.location == (x,y) :
					    	upd_g = current_node.g_cost + MoveCost((x,y+1),(x,y))
					    	if  upd_g < item.g_cost:
					    		item.g_cost = upd_g
					    		item.f_cost = item.h_cost + item.g_cost
					    		item.parent =  current_node.location
					    		break
					    	else :
					    		break 

				
				

		if y>0:
			if (grid[x][y-1]!='%') :
				if visited[x][y-1]==0:
				    #visited[x][y-1]=1
				    temp_node.h_cost = heuristicCost(x,y-1)
				    temp_node.g_cost = current_node.g_cost + MoveCost((x,y-1),(x,y))
				    temp_node.f_cost = temp_node.h_cost + temp_node.g_cost
				    temp_node.parent = current_node.location
				    temp_node.location = (x,y-1)

				    list_q.put(temp_node)

				else :
					for item in list_q:
					    if item.location == (x,y) :
					    	upd_g = current_node.g_cost + MoveCost((x,y-1),(x,y))
					    	if  upd_g < item.g_cost:
					    		item.g_cost = upd_g
					    		item.f_cost = item.h_cost + item.g_cost
					    		item.parent =  current_node.location
					    		break
					    	else :
					    		break 

		if y<c-1 and x<r-1:
			if (grid[x+1][y+1]!='%' ):
			    if visited[x+1][y+1]==0:
				    ##visited[x+1][y-1]=1
				    temp_node.h_cost = heuristicCost(x+1,y-1)
				    temp_node.g_cost = current_node.g_cost + MoveCost((x+1,y-1),(x,y))
				    temp_node.f_cost = temp_node.h_cost + temp_node.g_cost
				    temp_node.parent = current_node.location
				    temp_node.location = (x+1,y-1) 

				    list_q.put(temp_node)

			else :
					for item in list_q:
					    if item.location == (x,y) :
					    	upd_g = current_node.g_cost + MoveCost((x+1,y-1),(x,y))
					    	if  upd_g < item.g_cost:
					    		item.g_cost = upd_g
					    		item.f_cost = item.h_cost + item.g_cost
					    		item.parent =  current_node.location
					    		break
					    	else :
					    		break 

		if x>0 and y>0 :
			if (grid[x-1][y-1]!='%'):
				if visited[x-1][y-1]==0:
				    #visited[x-1][y-1]=1
				    temp_node.h_cost = heuristicCost(x-1,y-1)
				    temp_node.g_cost = current_node.g_cost + MoveCost((x-1,y-1),(x,y))
				    temp_node.f_cost = temp_node.h_cost + temp_node.g_cost
				    temp_node.parent = current_node.location
				    temp_node.location = (x-1,y-1)

				    list_q.put(temp_node)

				else :
					for item in list_q:
					    if item.location == (x,y) :
					    	upd_g = current_node.g_cost + MoveCost((x-1,y-1),(x,y))
					    	if  upd_g < item.g_cost:
					    		item.g_cost = upd_g
					    		item.f_cost = item.h_cost + item.g_cost
					    		item.parent =  current_node.location
					    		break
					    	else :
					    		break 

		if x>0 and y<c-1 :
			if (grid[x-1][y+1]!='%' ):
			    if visited[x-1][y+1]==0:
				    #visited[x-1][y+1]=1
				    temp_node.h_cost = heuristicCost(x-1,y+1)
				    temp_node.g_cost = current_node.g_cost + MoveCost((x-1,y+1),(x,y))
				    temp_node.f_cost = temp_node.h_cost + temp_node.g_cost
				    temp_node.parent = current_node.location
				    temp_node.location = (x-1,y+1)

				    list_q.put(temp_node)

			else :
					for item in list_q:
					    if item.location == (x,y) :
					    	upd_g = current_node.g_cost + MoveCost((x-1,y+1),(x,y))
					    	if  upd_g < item.g_cost:
					    		item.g_cost = upd_g
					    		item.f_cost = item.h_cost + item.g_cost
					    		item.parent =  current_node.location
					    		break
					    	else :
					    		break 
	print visited 
	print current_node.location







				





		














	