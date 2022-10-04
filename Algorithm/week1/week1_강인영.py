import sys

N, F = map(int, sys.stdin.readline().split()) # 총 음의 갯수, 프렛의 수
temp = [[] for _ in range(6)] # 빈 이중리스트 선언
sol = 0 # 해답, 즉 손가락을 가장 적게 움직일 수 있는 수

for _ in range(N): # N번 반복
    s, f = map(int, sys.stdin.readline().split()) # 줄의 번호, 프렛의 번호
    s -= 1 # 리스트의 인덱스 기준을 맞추기 위해 -1씩 해줌
    if temp[s] == [] or temp[s][-1] < f: # 줄을 담당하는 리스트에서 원소를 아직 넣지 않은 상태거나, 줄 리스트의 맨 마지막 원소가 해당하는 프렛보다 작은 경우 
        temp[s].append(f) # 줄 리스트에 원소(프렛)를 추가
        sol += 1 # 움직인 횟수도 추가
    else:
        while temp[s] != [] and temp[s][-1] > f: # 줄 리스트가 빈 상태가 아니면서, 줄 리스트의 마지막 원소가 해당하는 프렛보다 큰경우 계속 반복
            temp[s].pop() # 줄 리스트에서 원소를 꺼낸다
            sol += 1 # 움직인 횟수 추가

        if temp[s] != [] and temp[s][-1] == f: # 줄 리스트가 빈 상태가 아니면서, 줄 리스트의 마지막 원소가 해당하는 프렛과 같은 경우라면
            continue # 아래의 코드들을 건너뛴다

        temp[s].append(f) # 해당하는 프렛보다 큰 경우를 모두 빼냈으니, 줄 리스트에 원소(프렛)을 추가한다
        sol += 1 # 추가 했으니 움직인 횟수도 추가한다

print(sol) # 반복문이 모두 끝난후 해답을 출력한다