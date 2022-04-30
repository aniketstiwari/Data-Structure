# https://www.geeksforgeeks.org/nearly-sorted-algorithm/

from pdb import set_trace
from heapq import heapify, heappush, heappop

def sort_k(arr: list, size: int, k: int):
    heap = arr[:k + 1]

    heapify(heap)

    target_index = 0
    for remaining_index in range(k + 1, size):
        arr[target_index] = heappop(heap)
        heappush(heap, arr[remaining_index])
        target_index += 1

    while heap:
        arr[target_index] = heappop(heap)
        target_index += 1

    print(*arr)



k = 3
arr = [2, 6, 3, 12, 56, 8]
n = len(arr)
sort_k(arr, n, k)

# The Min Heap based method takes O(k) + O((m) * log(k)) time where m = n – k and uses O(k) auxiliary space