from sys import stdin as s

s = open("/Users/jinoo/Desktop/rosalind/백준/test.txt","rt") 
N = int(s.readline().strip())
primer = list(map(int,s.readline().split()))
cnt = 0
def is_prime_num(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(n**0.5)+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False
    return True
            
for value in primer:
    if is_prime_num(value):
        cnt += 1
        
print(cnt)