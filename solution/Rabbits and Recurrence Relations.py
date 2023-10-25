# file_path = "dataset/test.txt"
file_path = "dataset/rosalind_fib.txt"
with open(file_path, 'r') as f:
    s = f.readline().split()

def rabbit(m,p):
	total=[]
	a=1
	for i in range(0,m):
		if i<2:
			total.append(a)
		if i>1:
			a=total[i-1]+(total[i-2]*p)
			total.append(a)
	return(a)

rabbit(int(s[0]), int(s[1]))