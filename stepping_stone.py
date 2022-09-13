import sys

result = []

N = int(input())   #돌의 갯수 

height = list(map(int,input().split()))  #돌의 높이 입력

for i in range(N):                      #돌의 갯수만큼 비교
    count = 1
    test1 = height[i]
    for j in height[i:]:                #왼쪽에서 오른쪽 순서로 크키비교
        if test1 < j:
            test1 = j
        count += 1
    result.append(count)

print(max(result))