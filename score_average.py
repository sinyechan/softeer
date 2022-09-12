import sys

result = []

N, K = map(int,input().split())   # 학생수와 구간수 입력

score = list(map(int,input().split()))  # 점수 입력

for i in range(K):                  #구간 입력받고 평균 계산후 결과저장
    a,b = map(int,input().split())
    cal = sum(score[a-1:b])/(b-a+1)
    result.append(round(cal,2))

for i in result:
    print(i)