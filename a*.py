from collections import deque
import heapq
import numpy
from math import sqrt
import time

start_x,start_y = [ int(i) for i in raw_input().strip().split()]
end_x,end_y = [ int(i) for i in raw_input().strip().split()]
r,c = [ int(i) for i in raw_input().strip().split()]

grid_1=[]
for i in xrange(0,r):
	grid_1.append(raw_input())
grid = numpy.empty((r,c), dtype = str )

for i in range(0,r):
	for j in range(0,c):
		grid[i][j] = grid_1[i][j]

visited=numpy.zeros((r,c))
h_cost = numpy.zeros((r,c))
f_cost = numpy.zeros((r,c))
g_cost = numpy.zeros((r,c))
parent = numpy.empty((r,c), dtype = tuple )

#grid=numpy.array(grid)

#print grid 
print visited
print grid

def MoveCost((x_1,y_1),(x_2,y_2)):
	return int(sqrt((x_2-x_1)**2 + (y_2 - y_1)**2) * 10)

def heuristicCost(x,y):
	global end_x,end_y
	return abs(end_x - x) + abs(end_y - y)

h_cost[start_x][start_y] = heuristicCost(start_x,start_y)
g_cost[start_x][start_y] = 0
f_cost[start_x][start_y] = h_cost[start_x][start_y]
parent[start_x][start_y] = (start_x,start_y)
heap = []
heapq.heappush(heap, ( f_cost[start_x][start_y] , (start_x,start_y) ) )
visited[start_x][start_y]=1


while 1:
	print heap
	
	#print visited 

	(fcost,(cord_x,cord_y)) = heapq.heappop(heap)
	#print fcost , cord_x , cord_y
	
	#heapq.heappush(heap , (fcost ,(cord_x,cord_y) ) )
	
	if (cord_x == end_x and cord_y == end_y ):
		break

	else :
		if  cord_y<c-1 :
			if (grid[cord_x][cord_y+1]!='%' ) :
				#print cord_x , cord_y+1 
				if visited[cord_x][cord_y+1]==0:
					visited[cord_x][cord_y+1]=1
					
					#print "v=0", cord_x,cord_y+1
					h_cost[cord_x][cord_y+1] = heuristicCost(cord_x,cord_y+1)
					g_cost[cord_x][cord_y+1] = g_cost[cord_x][cord_y] + MoveCost((cord_x,cord_y+1),(cord_x,cord_y))
					f_cost[cord_x][cord_y+1] = h_cost[cord_x][cord_y+1] + g_cost[cord_x][cord_y+1]
					parent[cord_x][cord_y+1] = (cord_x,cord_y)
					heapq.heappush( heap, ( f_cost[cord_x][cord_y+1], (cord_x,cord_y+1) ) )
					

				else :
					up_gcost = g_cost[cord_x][cord_y] + MoveCost((cord_x,cord_y+1),(cord_x,cord_y))
					#print "v=1", cord_x,cord_y+1
					if up_gcost < g_cost[cord_x][cord_y+1]  :
						#print "update"
						parent[cord_x][cord_y+1] = (cord_x,cord_y)
						g_cost[cord_x][cord_y+1] = up_gcost
						f_cost[cord_x][cord_y+1] = h_cost[cord_x][cord_y+1] + g_cost[cord_x][cord_y+1]

					else :
						pass


		



		if cord_x>0:
			if (grid[cord_x-1][cord_y]!='%' ):
				#print cord_x-1 , cord_y
				if visited[cord_x-1][cord_y]==0:
					visited[cord_x-1][cord_y]=1
					
					#print "v=0", cord_x-1,cord_y
					h_cost[cord_x-1][cord_y] = heuristicCost(cord_x-1,cord_y)
					g_cost[cord_x-1][cord_y] = g_cost[cord_x][cord_y] + MoveCost((cord_x-1,cord_y),(cord_x,cord_y))
					f_cost[cord_x-1][cord_y] = h_cost[cord_x-1][cord_y] + g_cost[cord_x-1][cord_y]
					parent[cord_x-1][cord_y] = (cord_x,cord_y)
					heapq.heappush( heap, ( f_cost[cord_x-1][cord_y],(cord_x-1,cord_y) ) )
					

				else :
					up_gcost = g_cost[cord_x][cord_y] + MoveCost((cord_x,cord_y-1),(cord_x,cord_y))
					#print "v=1", cord_x,cord_y-1
					if up_gcost < g_cost[cord_x][cord_y-1]  :
						#print "update"
						parent[cord_x][cord_y-1] = (cord_x,cord_y)
						g_cost[cord_x][cord_y-1] = up_gcost
						f_cost[cord_x][cord_y-1] = h_cost[cord_x][cord_y-1] + g_cost[cord_x][cord_y-1]

					else :
						pass
					

				
				
			
				
		if cord_x<r-1:
			if (grid[cord_x+1][cord_y]!='%' )  :
				#print cord_x+1 , cord_y
				if visited[cord_x+1][cord_y]==0:
					visited[cord_x+1][cord_y]=1
					
					#print "v=0", cord_x,cord_y
					h_cost[cord_x+1][cord_y] = heuristicCost(cord_x+1,cord_y)
					g_cost[cord_x+1][cord_y] = g_cost[cord_x][cord_y] + MoveCost((cord_x+1,cord_y),(cord_x,cord_y))
					f_cost[cord_x+1][cord_y] = h_cost[cord_x+1][cord_y] + g_cost[cord_x+1][cord_y]
					parent[cord_x+1][cord_y] = (cord_x,cord_y)
					heapq.heappush( heap, ( f_cost[cord_x+1][cord_y],(cord_x+1,cord_y) ) )
					

				else :
					up_gcost = g_cost[cord_x][cord_y] + MoveCost((cord_x+1,cord_y),(cord_x,cord_y))
					#print "v=1", cord_x+1,cord_y
					if up_gcost < g_cost[cord_x+1][cord_y]  :
						prin#t "update"
						parent[cord_x+1][cord_y] = (cord_x,cord_y)
						g_cost[cord_x+1][cord_y] = up_gcost
						f_cost[cord_x+1][cord_y] = h_cost[cord_x+1][cord_y] + g_cost[cord_x+1][cord_y]

					else :
						pass
					

				
				

		if cord_y>0:
			if (grid[cord_x][cord_y-1]!='%') :
				#print cord_x , cord_y-1
				if visited[cord_x][cord_y-1]==0:
					visited[cord_x][cord_y-1]=1
					
					#print "v=0", cord_x,cord_y-1
					h_cost[cord_x][cord_y-1] = heuristicCost(cord_x,cord_y-1)
					g_cost[cord_x][cord_y-1] = g_cost[cord_x][cord_y] + MoveCost((cord_x,cord_y-1),(cord_x,cord_y))
					f_cost[cord_x][cord_y-1] = h_cost[cord_x][cord_y-1] + g_cost[cord_x][cord_y-1]
					parent[cord_x][cord_y-1] = (cord_x,cord_y)
					heapq.heappush( heap, ( f_cost[cord_x][cord_y-1],(cord_x,cord_y-1) ) )
				    
				else :
					up_gcost = g_cost[cord_x][cord_y] + MoveCost((cord_x,cord_y-1),(cord_x,cord_y))
					#print "v=1", cord_x,cord_y-1
					if up_gcost < g_cost[cord_x][cord_y-1]  :
						#print "update"
						parent[cord_x][cord_y-1] = (cord_x,cord_y)
						g_cost[cord_x][cord_y-1] = up_gcost
						f_cost[cord_x][cord_y-1] = h_cost[cord_x][cord_y-1] + g_cost[cord_x][cord_y-1]

					else :
						pass
					

		

'''		if cord_y<c-1 and cord_x<r-1:
			if (grid[cord_x+1][cord_y+1]!='%' ):
			    if visited[cord_x+1][cord_y+1]==0:
			    	visited[cord_x][cord_y-1]=1
			    	h_cost[cord_x+1][cord_y+1] = heuristicCost(cord_x,cord_y)
			    	g_cost[cord_x+1][cord_y+1] = g_cost[cord_x][cord_y] + MoveCost((cord_x+1,cord_y+1),(cord_x,cord_y))
			    	f_cost[cord_x+1][cord_y+1] = h_cost[cord_x+1][cord_y+1] + g_cost[cord_x+1][cord_y+1]
			    	parent[cord_x+1][cord_y+1] = (cord_x,cord_y)
			    	heapq.heappush( heap, ( f_cost[cord_x+1][cord_y+1],(cord_x+1,cord_y+1) ) )
				    

			else :
				up_gcost = g_cost[cord_x][cord_y] + MoveCost((cord_x+1,cord_y+1),(cord_x,cord_y))
				if up_gcost < g_cost[cord_x+1][cord_y+1]  :
						parent[cord_x+1][cord_y+1] = (cord_x,cord_y)
						g_cost[cord_x+1][cord_y+1] = up_gcost
						f_cost[cord_x+1][cord_y+1] = h_cost[cord_x+1][cord_y+1] + g_cost[cord_x+1][cord_y+1]

				else :
						pass
					

		
		if cord_x>0 and cord_y>0 :
			if (grid[cord_x-1][cord_y-1]!='%'):
				if visited[cord_x-1][cord_y-1]==0:
					visited[cord_x][cord_y-1]=1
					h_cost[cord_x-1][cord_y-1] = heuristicCost(cord_x,cord_y)
					g_cost[cord_x-1][cord_y-1] = g_cost[cord_x][cord_y] + MoveCost((cord_x-1,cord_y-1),(cord_x,cord_y))
					f_cost[cord_x-1][cord_y-1] = h_cost[cord_x-1][cord_y-1] + g_cost[cord_x-1][cord_y-1]
					parent[cord_x-1][cord_y-1] = (cord_x,cord_y)
					heapq.heappush( heap, ( f_cost[cord_x-1][cord_y-1],(cord_x-1,cord_y-1) ) )
				    

				else :
					up_gcost = g_cost[cord_x][cord_y] + MoveCost((cord_x-1,cord_y-1),(cord_x,cord_y))
					if up_gcost < g_cost[cord_x-1][cord_y-1]  :
						parent[cord_x-1][cord_y-1] = (cord_x,cord_y)
						g_cost[cord_x-1][cord_y-1] = up_gcost
						f_cost[x-1][cord_y-1] = h_cost[cord_x-1][cord_y-1] + g_cost[cord_x-1][cord_y-1]

					else :
						pass
					

		if cord_x>0 and cord_y<c-1 :
			if (grid[cord_x-1][cord_y+1]!='%' ):
			    if visited[cord_x-1][cord_y+1]==0:
			    	visited[cord_x][cord_y-1]=1
			    	h_cost[cord_x-1][cord_y+1] = heuristicCost(cord_x,cord_y)
			    	g_cost[cord_x-1][cord_y+1] = g_cost[cord_x][cord_y] + MoveCost((cord_x-1,cord_y+1),(cord_x,cord_y))
			    	f_cost[cord_x-1][cord_y+1] = h_cost[cord_x-1][cord_y+1] + g_cost[cord_x-1][cord_y+1]
			    	parent[cord_x-1][cord_y+1] = (cord_x,cord_y)
			    	heapq.heappush( heap, ( f_cost[cord_x-1][cord_y+1],(cord_x-1,cord_y+1) ) )
				    

			else :
				up_gcost = g_cost[cord_x][cord_y] + MoveCost((cord_x-1,cord_y+1),(cord_x,cord_y))
				if up_gcost < g_cost[cord_x-1][cord_y+1]  :
						parent[cord_x-1][cord_y+1] = (cord_x,cord_y)
						g_cost[cord_x-1][cord_y+1] = up_gcost
						f_cost[cord_x-1][cord_y+1] = h_cost[cord_x-1][cord_y+1] + g_cost[cord_x-1][cord_y+1]

				else :
						pass


		if cord_x<r-1 and cord_y>0 :
			if (grid[cord_x+1][cord_y-1]!='%' ):
			    if visited[cord_x+1][cord_y-1]==0:
			    	visited[cord_x][cord_y-1]=1
			    	h_cost[cord_x+1][cord_y-1] = heuristicCost(cord_x,cord_y)
			    	g_cost[cord_x+1][cord_y-1] = g_cost[cord_x][cord_y] + MoveCost((cord_x+1,cord_y-1),(cord_x,cord_y))
			    	f_cost[cord_x+1][cord_y-1] = h_cost[cord_x+1][cord_y-1] + g_cost[cord_x+1][cord_y-1]
			    	parent[cord_x+1][cord_y-1] = (cord_x,cord_y)
			    	heapq.heappush( heap, ( f_cost[cord_x+1][cord_y-1],(cord_x+1,cord_y-1) ) )
				    

			else :
				up_gcost = g_cost[cord_x][cord_y] + MoveCost((cord_x+1,cord_y-1),(cord_x,cord_y))
				if up_gcost < g_cost[cord_x+1][cord_y-1]  :
						parent[cord_x+1][cord_y-1] = (cord_x,cord_y)
						g_cost[cord_x+1][cord_y-1] = up_gcost
						f_cost[cord_x+1][cord_y-1] = h_cost[cord_x+1][cord_y-1] + g_cost[cord_x+1][cord_y-1]

				else :
						pass'''

    
					
	
#print visited

#print parent

queue1 = deque([(end_x,end_y)])
t_x,t_y=end_x,end_y
while 1:
	#print queue1
	#print path_x[t_x][t_y],path_y[t_x][t_y]
	if t_x==start_x and t_y==start_y:
		#queue1.append((start_x,start_y))
		break
	queue1.append(parent[t_x][t_y])
	t_x,t_y = parent[t_x][t_y]
	


print len(queue1)-1

for i in range(0,len(queue1)):
	p,q=queue1.pop()
	print int(p),int(q)

				





		














	