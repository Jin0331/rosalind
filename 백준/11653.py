from sys import stdin as s

s = open("/Users/jinoo/Desktop/rosalind/백준/test.txt","rt") 
N = int(s.readline().strip())
di = list()
cnt = 0
answer = list()

def is_prime_num(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5)+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False
    return True


# 약수 중 소수를 고른다
for value in range(1, int(N**0.5)+1):
    if N % value == 0:
        di.append(value)
        di.append(N//value)
di_prime = [value for value in di if is_prime_num(value)]

while N > 1:
    for value in di_prime:
        if N % value == 0:
            answer.append(value)
            N /= value       

answer.sort()
print(" ".join(map(str, answer)))