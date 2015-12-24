

from collections import deque
import numpy
start_x, start_y = [ int(i) for i in raw_input().strip().split() ]
end_x, end_y = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

grid = []
record={}

queue = deque([(start_x,start_y)])
queue1 = deque([(end_x,end_y)])
count =0

for i in xrange(0, r):
    grid.append(raw_input().strip().split())

lists=numpy.zeros((r,c))
path_x=numpy.zeros((r,c))
path_y=numpy.zeros((r,c))
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
				path_x[x][y+1]=x
				path_y[x][y+1]=y
				#print " path_x[x][y+1],path_y[x][y+1]",path_x[x][y+1],path_y[x][y+1]
		if x>0:
			#print (grid[x-1][y]=='-' ) , lists[x-1][y]==0
			if (grid[x-1][y]=='-' ) and  lists[x-1][y]==0:
				queue.append((x-1,y))
				lists[x-1][y]=1
				path_x[x-1][y]=x
				path_y[x-1][y]=y
				#print "path_x[x][y-1],path_y[x][y-1] ",path_x[x][y-1],path_y[x][y-1]
		if x<r-1:
			#print grid[x+1][y]=='-' , lists[x+1][y]==0
			if (grid[x+1][y]=='-' ) and lists[x+1][y]==0:
				queue.append((x+1,y))
				lists[x+1][y]=1
				path_x[x+1][y]=x
				path_y[x+1][y]=y
				#print "path_x[x+1][y],path_y[x+1][y] ",path_x[x+1][y],path_y[x+1][y]

		if y>0:
			#print grid[x][y-1]=='-' , lists[x][y-1]==0
			if (grid[x][y-1]=='-') and lists[x][y-1]==0:
				queue.append((x,y-1))
				lists[x][y-1]=1
				path_x[x][y-1]=x
				path_y[x][y-1]=y
				#print "path_x[x][y-1],path_y[x][y-1] ",path_x[x][y-1],path_y[x][y-1]


	#print queue
	#print lists
#print path_x
#print path_y

t_x,t_y=end_x,end_y
while 1:
	print queue1
	print path_x[t_x][t_y],path_y[t_x][t_y]
	queue1.append((path_x[t_x][t_y],path_y[t_x][t_y]))
	t_x=path_x[t_x][t_y]
	t_y=path_y[t_x][t_y]
	if t_x==start_x and t_y==start_y:
		queue1.append((start_x,start_y))
		break
print queue1
#print path_x[0.0][2.0], path_y[0.0][2.0]


	




