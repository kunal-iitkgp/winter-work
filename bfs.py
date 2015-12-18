

from collections import deque
import numpy
start_x, start_y = [ int(i) for i in raw_input().strip().split() ]
end_x, end_y = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

grid = []

queue = deque([(start_x,start_y)])
count =0

for i in xrange(0, r):
    grid.append(raw_input().strip().split())

lists=numpy.zeros((r,c))
lists[start_x][start_y]=1


while len(queue)!=0:

	x,y=queue.popleft()
	#print count
	print x,y
	if end_x==x and end_y==y:
		#print "cool"
		break
	

	else :
		if  y<c-1 :
			#print grid[x][y+1]=='-' , lists[x][y+1]==0
			if (grid[x][y+1]=='-' ) and lists[x][y+1]==0:
				queue.append((x,y+1))
				lists[x][y+1]=1
		if x>0:
			#print (grid[x-1][y]=='-' ) , lists[x-1][y]==0
			if (grid[x-1][y]=='-' ) and  lists[x-1][y]==0:
				queue.append((x-1,y))
				lists[x-1][y]=1
		if x<r-1:
			#print grid[x+1][y]=='-' , lists[x+1][y]==0
			if (grid[x+1][y]=='-' ) and lists[x+1][y]==0:
				queue.append((x+1,y))
				lists[x+1][y]=1
		if y>0:
			#print grid[x][y-1]=='-' , lists[x][y-1]==0
			if (grid[x][y-1]=='-') and lists[x][y-1]==0:
				queue.append((x,y-1))
				lists[x][y-1]=1

	#print queue
	#print lists


