from sys import stdin as s

s = open("/Users/jinoo/Desktop/rosalind/백준/test.txt","rt") 
N = list(map(int, s.readline().split()))
rs = 0

start, end = N
ran = range(start, end+1)
two_divisor = [value for value in ran if value % 2 == 0]

rs += len(ran) - len(two_divisor)

# 모든 약수구하기
for R in two_divisor:
    cnt = 0
    while R % 2 == 0:
        cnt += 1
        R //= 2     
    rs += 2 ** cnt

print(rs)