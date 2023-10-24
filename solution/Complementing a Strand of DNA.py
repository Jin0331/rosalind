file_path = "dataset/rosalind_revc.txt"
with open(file_path, 'r') as f:
    s = f.readline().strip()

# A <-> T
# G <-> C

s_t = [value for value in s]
rs = list()

for value in s_t:
    if value == "A":
        rs.append("T")
    elif value == "T":
        rs.append("A")
    elif value == "G":
        rs.append("C")
    elif value == "C":
        rs.append("G")

print("".join(rs)[::-1])



