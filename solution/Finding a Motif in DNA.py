from sys import stdin as s

s = open("/Users/jinoo/Desktop/rosalind/dataset/rosalind_subs.txt","rt") 
S = s.readline().strip()
T = s.readline().strip()
t_len = len(T)

answer = []


for index in range(len(S) - t_len + 1):
    if S[index:index+t_len] == T:
        answer.append(str(index + 1))

print(" ".join(answer))