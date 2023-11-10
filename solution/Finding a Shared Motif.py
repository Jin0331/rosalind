from sys import stdin as s

S = []
tmp = ""
with open("/Users/jinoo/Desktop/rosalind/dataset/rosalind_lcsm.txt","rt") as f:    
    t = f.readlines()
    for x in t:
        if x.startswith(">") == False:
            tmp += x.strip()
        elif x.startswith(">"):
            S.append(tmp)
            tmp = ""
S.append(tmp)
S = S[1:]

# 최소 길이의 문자열에서 모든 가능한 수
tmp = []
min_str = min(S)
min_str_index = S.index(min(S))

for i in range(len(min_str)):
    for j in range(i, len(min_str)):
        tmp.append(min_str[i:j])
tmp2 = [x  for x in tmp if len(x) > 1]
p_str = list(set(tmp2))
p_str.sort(reverse=True, key=lambda x : len(x))

flag = -1
for p in p_str:
    # answer.append(list(map(lambda x : p in x, S)))
    for i in range(len(S)):
        if p not in S[i]:
            flag = -1
            break
        flag = 1

    if flag == 1:
        answer = p
        break

print(answer)