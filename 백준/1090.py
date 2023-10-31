from sys import stdin as s

s = open("test.txt","rt") 
N = int(s.readline().strip())
checker = [list(map(int,s.readline().split())) for _ in range(N)]
answer = dict()

# 모든 좌표 탐색
for x in range(14, 17):
    for y in range(14, 17):

        # N개의 체커 좌표 최소값 구하기
        temp = list()
        for A,B in checker:
            cnt = 0
            print(A, B)
            while True:
                if x == A and y == B:
                    temp.append(cnt)
                    break

                if x != A and x < A:
                    A -= 1
                elif x != A and x > A:
                    A += 1
                elif y != B and y < B:
                    B -= 1
                elif y != B and y > B:
                    B += 1
                cnt += 1
        answer["{}_{}".format(x,y)] = temp
        
            
            

            
