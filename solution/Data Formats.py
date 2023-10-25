from Bio import Entrez
from Bio import SeqIO

# file_path = "dataset/test.txt"
file_path = "dataset/rosalind_frmt.txt"
with open(file_path, 'r') as f:
    s = f.readline().split()

Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.efetch(db="nucleotide", id=s, rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))

fasta_length = list(map(lambda x : len(x.seq), records))
min_index = fasta_length.index(min(fasta_length))

with open("example.fasta", "w") as output_handle:
    SeqIO.write(records[min_index], output_handle, "fasta")