import heapq
import pdb

arr = [5, 1, 4, 2, 7]

heapq.heapify(arr)
#print (list(arr))

heapq.heappush(arr, 8)

#print(list(arr))

heapq.heappop(arr)
heapq.heappop(arr)

#print(list(arr))

li1 = [5, 7, 9, 4, 3]
  
# initializing list 2
li2 = [5, 7, 9, 4, 3]
 
#print (heapq.heappushpop(li1, 6))

#print(li1)

#print (heapq.heapreplace(li2, 2))

print(heapq.nlargest(3, li1))

print(heapq.nsmallest(3, li1))
