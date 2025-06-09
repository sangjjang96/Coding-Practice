import sys

num = int(input())

questions = []

for _ in range(num):
    questions.append(list(map(int, sys.stdin.readline().split())))
    
print(questions)