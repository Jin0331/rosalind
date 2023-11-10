from sys import stdin as s

S = []
answer = []
tmp = ""
with open("/Users/jinoo/Desktop/rosalind/dataset/rosalind_cons.txt","rt") as f:    
    t = f.readlines()
    for x in t:
        if x.startswith(">") == False:
            tmp += x.strip()
        elif x.startswith(">"):
            S.append(tmp)
            tmp = ""
S.append(tmp)

def a_count(arr):
    try:
        return arr[i]
    except:
        return "0"
        

A,T,G,C = [], [], [], []
for i in range(max(map(lambda x : len(x), S[1:]))):
    l = list(map(a_count, S[1:]))
    A.append(l.count("A"))
    C.append(l.count("C"))
    G.append(l.count("G"))
    T.append(l.count("T"))

acid_str = "ACGT"
for i in range(len(A)):
    tmp = [A[i], C[i], G[i], T[i]]
    answer.append(acid_str[tmp.index(max(tmp))])

print("".join(answer))
print("A:", " ".join(map(str,A)))
print("C:", " ".join(map(str,C)))
print("G:", " ".join(map(str,G)))
print("T:", " ".join(map(str,T)))