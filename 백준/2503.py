from sys import stdin as s

s = open("test.txt","rt") 
N = int(s.readline().strip())
hint = [list(map(int,s.readline().split())) for _ in range(N)]
answer = 0

# 민혁이의 정답 가능 범위 모두
for x in range(1, 10):
    for y in range(1,10):
        for z in range(1,10):

            # 서로 다른 수
            if x == y or x == z or y == z:
                continue

            # 서로 다른 수의 예비정답 3개 나옴,, xzy --> solution,, hint -> number
            # hint와 비교
            cnt = 0
            for number, strike, ball in hint:
                ball_count, strike_count = 0, 0
                number_s, solution = str(number), "{}{}{}".format(x,y,z)
                
                for index in range(3):
                    if number_s[index] == solution[index]:
                        strike_count += 1
                    elif number_s[index] in solution:
                        ball_count += 1
                
                if strike == strike_count and ball == ball_count:
                    cnt += 1

            if cnt == N:
                print(solution, number_s)
                answer += 1

print(answer)