# https://www.geeksforgeeks.org/find-k-closest-numbers-in-an-unsorted-array/
# Find k closest numbers in an unsorted array

from queue import PriorityQueue
from pdb import set_trace

def printKclosest(arr,n,x,k):
	pq = PriorityQueue()

	for i in range(n):
		# tHE reason (-) is added to implement max heap
		# https://stackoverflow.com/questions/41218860/how-to-use-queue-priorityqueue-as-maxheap-python
		pq.put(( -abs(arr[i] - x), arr[i]))
		if pq.qsize() > k:
			pq.get()  # to pop element

	while pq.qsize() > 0:
		a, b = pq.get()
		print(b)


#arr = [5, 6, 7, 8, 9]
#x, k = 7, 3
#arr = [-10,-50,20,17,80]
#x,k = 20,2
n = len(arr)
printKclosest(arr, n, x, k)