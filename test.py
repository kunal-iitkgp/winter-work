import heapq

heap = []
heapq.heappush(heap, (1, (2,5)))
heapq.heappush(heap, (10, (5,4)))
heapq.heappush(heap, (5,(7,8)))
heapq.heappush(heap,(2,(3,7)))

for x in range(0,len(heap)):
	(a,(b,c)) = heap[0]
	print a,b,c


