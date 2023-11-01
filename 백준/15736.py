from sys import stdin as s
import statistics

s = open("/Users/jinoo/Desktop/rosalind/백준/test.txt","rt") 
N = int(s.readline().strip())
anwser = int(N ** 0.5)

print(anwser)