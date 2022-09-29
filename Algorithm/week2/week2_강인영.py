import heapq
import sys

N = int(sys.stdin.readline()) #후보 수 입력
heap = []
dasom = 0
cnt = 0 #매수할 인간 수

for i in range(N):
    x = int(sys.stdin.readline()) #후보별 득표 수 입력
    if i==0: #기호 1번
        dasom = x #다솜이의 원래 득표 수
    else:
        if x >= dasom: #1번 득표 수 이상인 값만 저장 
        #주의!! heapq 라이브러리는 최소힙만 지원
            heapq.heappush(heap,-x) #음수로 저장해야 최대힙'처럼' 저장됨 

#print(heap)

while heap: 
    if dasom > -heap[0]: #다솜이가 최다 득표하면
        break #끝!
    else:
        max_now = heapq.heappop(heap) #현재 최다 득표 수 저장
        heapq.heappush(heap,max_now+1) #다솜이한테 한 표 뺏김
        dasom += 1 
        cnt += 1 #인간 매수 성공
 
#print(dasom) 
print(cnt) 