from Bio.Seq import Seq
# file_path = "dataset/test.txt"
file_path = "dataset/rosalind_ini.txt"
with open(file_path, 'r') as f:
    s = f.readlines()

my_seq = Seq(s[0])
print(my_seq.count("A"), my_seq.count("C"), my_seq.count("G"), my_seq.count("T"))