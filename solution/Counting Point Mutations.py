# file_path = "dataset/test.txt"
file_path = "dataset/rosalind_hamm.txt"
with open(file_path, 'r') as f:
    s = f.readlines()

s_zip = list(zip(s[0], s[1]))
rs = 0
for idx in range(len(s_zip)):
    if s_zip[idx][0] != s_zip[idx][1]:
        rs += 1
