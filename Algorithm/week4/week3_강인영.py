import heapq
import sys
#import numpy 

N = int(sys.stdin.readline()) #N개의 줄
heap = []

for i in range(N):
     cardNum = int(sys.stdin.readline()) #카드 묶음 개수
     heapq.heappush(heap, cardNum)

comp = 0 #2개씩 비교할 때 비교 횟수
compSum = 0 #최종 출력 값 (최소 비교 횟수)

if N == 1:
    compSum = 0 
else:   
    for i in range(N-1): #2개씩 비교하므로, 예를 들어 4개의 뭉치면 3번씩 비교하게 됨
        comp = heapq.heappop(heap) #입력된 카드 뭉치의 개수 중 최솟값(5) 일단 out
        if heap:  
            comp += heapq.heappop(heap) #그 다음 두번째로 작은 값(6) out
        #print(comp)

        heapq.heappush(heap, comp) #비교횟수(5+6) 다시 힙에 push
        compSum += comp #누적횟수에 비교횟수 추가
    #print(heap)
#print(heap)
print(compSum)


'''
input example
4
5
6
7
8

4
3
3
3
3
'''
