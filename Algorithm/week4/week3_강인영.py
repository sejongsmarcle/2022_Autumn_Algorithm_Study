import heapq
import sys
#import numpy 

N = int(sys.stdin.readline()) 
max_heap = []
min_heap = []

for i in range(N):
    x = int(sys.stdin.readline()) 
    if i % 2 == 0:
        heapq.heappush(max_heap, -x) #최대힙으로 저장
    else: 
        heapq.heappush(min_heap, x) #최소힙으로 저장

    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        max_heap_max = -heapq.heappop(max_heap)
        min_heap_min = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min_heap_min)
        heapq.heappush(min_heap, max_heap_max)
    if max_heap:
        median = -max_heap[0]
    print(median)