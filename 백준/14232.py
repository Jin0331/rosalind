from sys import stdin as s

#s = open("/Users/jinoo/Desktop/rosalind/백준/test.txt","rt") 
N = int(s.readline().strip())
di = list()

# 약수 중 소수를 고른다
for value in range(2, int(N**0.5)+1):
    while N % value == 0:
        di.append(value)
        N //= value
if N != 1: 
    di.append(N)
print(str(len(di)) + "\n" + " ".join(map(str, di)))