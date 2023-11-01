from sys import stdin as s
import statistics

s = open("/Users/jinoo/Desktop/rosalind/백준/test.txt","rt") 
N = int(s.readline().strip())
checker = [list(map(int,s.readline().split())) for _ in range(N)]
answer = dict()

x_max = max(map(lambda x : x[0], checker))
y_max = max(map(lambda x : x[1], checker))
x_min = min(map(lambda x : x[0], checker))
y_min = min(map(lambda x : x[1], checker))
x_mid = statistics.median(range(x_min, x_max + 1))
y_mid = statistics.median(range(y_min, y_max + 1))

x_range = list(set([(x, y_mid) for x in range(x_min, x_max + 1)]
y_range = [(x_mid, y) for y in range(y_min, y_max + 1)]

# 모든 좌표 탐색
for x, y in ex_range:
    # N개의 체커 좌표 최소값 구하기
    temp = list()
    for A,B in checker:
        cnt = 0
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
    temp.sort()
    answer["{}_{}".format(x,y)] = temp
        

answer_list = [0]
for index in range(2,N+1):
    min_value = 1_000_000
    for items in answer.values():
        comp_value = sum(items[:index])
        if min_value > comp_value:\
            min_value = comp_value
    answer_list.append(min_value)

print(" ".join(map(str, answer_list)))