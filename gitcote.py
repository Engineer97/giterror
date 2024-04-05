



# 백준 1436 영화감독 숌
# 솔루션 : result 값에 '666'이 포함하는지를 판단하여 
#'666'이 포함되어 있을 경우 cnt 변수를 1씩 증가

#print("this is test code")

#print("this is test code number 2")

'''
n = int(input())
cnt = 0
result = 666

while True:
        if '666' in str(result):
                cnt += 1
        
        if n == cnt:
                break

        result += 1

print(result)

'''

# 백준 1676 팩토리얼 0의 개수


'''


n = int(input())
li = []
facto = 1

for i in range(n):
        facto = facto * n
        n = n -1


li = list(str(facto))
li = li[::-1]
answer = 0
for i in li:
        if i != '0':
                break
        if i == '0':
                answer += 1

print(answer)


'''


# 백준 7568 덩치
# 그리디 알고리즘?????
# 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1
# 두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 
#x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다


'''
n = int(input())
li = []
rank = []

for _ in range(n):
        mom, ki = map(int, input().split())
        li.append((mom, ki))

for i in range(n):
        cnt = 0
        for j in range(n):
                if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
                        cnt += 1

        rank.append(cnt + 1)

for i in rank:
        print(i,end=" ")

'''




# 백준 11651 좌표 정렬하기 2


'''


n = int(input())
li = []

for i in range(n):
        x, y = map(int, input().split())
        li.append((x, y))


li.sort(key=lambda item: (item[1], item[0]))

for i in li:
        print(i[0], i[1])

# y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력


'''




# 백준 11650 좌표 정렬하기

# 좌표를 x좌표가 증가하는 순으로, 
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성


'''


n = int(input())
li = []

for i in range(n):
        x, y = map(int, input().split())
        li.append((x, y))

li.sort(key=lambda item: (item[0], item[1]))

for i in li:
        print(i[0], i[1])


'''




# 백준 11866 요세푸스 문제

'''


import sys
from collections import deque

li = []

n, k = map(int, input().split())

circle = list(range(1, n+1))

dq = deque(circle)


while dq:
        for _ in range(k-1):
                a = dq.popleft()
                dq.append(a)
        li.append(dq.popleft())

        if len(dq) == 1:
                li.append(dq[0])
                dq.popleft()





print("<", end="")
for i in range(n-1):
        print(li[i], end=", ")
print(li[n-1], end="")
print(">", end="")



'''



# 백준 1920 수 찾기


'''

n = int(input())
li_a = list(map(int, input().split()))
m = int(input())
li_b = list(map(int, input().split()))

answer = []

for i in li_b:
        if i in li_a:
                answer.append(1)
        else:
                answer.append(0)

for i in answer:
        print(i)

'''

#-------------------------------------- 시간 초과 발생!!!!!!!!!!! -----------------------------------------------


'''



import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort() # 탐색의 대상인 리스트는 반드시 정렬을 해줘야 한다!!!!!

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
# b 리스트는 탐색 대상이 아니므로 정렬을 해줄 필요가 없다!!!!


for i in b:
        left = 0
        right = n-1

        while left <= right:
                mid = (left + right) // 2
                if i > a[mid]:
                        left = mid + 1
                elif i < a[mid]:
                        right = mid - 1
                else:
                        left = mid
                        right = mid
                        break
        
        if left == mid and right == mid:
                print(1)
        else:
                print(0)

                

'''




# 백준 2164 카드2


'''


import sys
from collections import deque

n = int(input())
li = list(range(1, n+1))
dq = deque(li)

#print(len(dq))


while len(dq) > 1: # 조건을 그냥 while dq: 이렇게 쓰지 말 것!
        dq.popleft()
        dq.append(dq.popleft())  # 굳이 tmp 변수를 쓰지 말 것!

print(dq[0]) # while 문 안에서 지랄하지 말고 그냥 while 문 밖에서 하나 남은거 출력!



'''




# 백준 2839 설탕 배달


'''


n = int(input())
bong = 0

while n >= 0:
        if n % 5 == 0:
                bong += (n // 5)
                print(bong)
                break
        n -= 3
        bong += 1
else:
        print(-1)



'''




# 백준 9012 괄호
# 스택 자료구조 사용!!!


'''


t = int(input())

for i in range(t):
        stack = []
        target = input()

        for j in target:
                if j == '(':
                        stack.append(j)
                elif j == ')':
                        if len(stack) != 0: # 아까 집어넣은 ( 가 스택 안에 있다면
                                stack.pop() # ) 랑 스택 안에 있는 ( 가 1대1 대응으로 소멸!!!!
                        else:
                                print("NO")
                                break
        else:
                if len(stack) == 0:
                        print("YES")
                else:
                        print("NO")



'''



# 백준 18110 solved.ac


'''



import sys

def banoll(x):
        if x - int(x) >= 0.5:
                return int(x) + 1
        else:
                return int(x)



n = int(sys.stdin.readline())

if n:
        li = []

        for _ in range(n):
                li.append(int(sys.stdin.readline().strip()))
        
        cnt = banoll(n * 0.15)
        li.sort()

        if cnt > 0: # 제외되는 사람의 수가 1 이상
                print(banoll(sum(li[cnt:n-cnt])/len(li[cnt:n-cnt])))
        else: # 제외되는 사람의 수가 0 일때
                print(banoll(sum(li)/len(li)))
else: # 투표가 0일 때
        print(0)
        



'''






# 백준 10773 제로


'''


k = int(input())
li = []
stack = []

for i in range(k):
        li.append(int(input()))


for i in li:
        if i != 0:
                stack.append(i)
        
        if i == 0:
                stack.pop()
        
print(sum(stack))




'''






# 너 실력이 많이 늘었구나






# 백준 10816 숫자 카드 2

'''

n = int(input())
li_n = list(map(int, input().split()))

m = int(input())
li_m = list(map(int, input().split()))

answer = []

for i in li_m:
        if i in li_n:
                answer.append(li_n.count(i))
        else:
                answer.append(0)

for i in answer:
        print(i, end=" ")


'''


# -------------------------------------------- 시간 초과 ---------------------------------------------------

'''

import sys

n = int(sys.stdin.readline())
li_n = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
li_m = list(map(int, sys.stdin.readline().split()))

answer = []

for i in li_m:
        if i in li_n:
                answer.append(li_n.count(i))
        else:
                answer.append(0)

for i in answer:
        print(i, end=" ")



'''






# 백준 2108 통계학




import sys
input=sys.stdin.readline

n=int(input())
arr=[]

for i in range(n):
    arr.append(int(input()))

arr.sort()#중앙값을 구하기 위해 정렬

print(round(sum(arr)/len(arr)))#1) 산술평균
print(arr[len(arr)//2])#2) 중앙값

#최빈값
dic=dict()
for i in arr:#빈도수 구하기
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
        
mx=max(dic.values())#빈도수 중 최대값 구하기
mx_dic=[]#최빈값 숫자를 저장할 배열

for i in dic:#빈도수 딕셔너리에서
    if mx==dic[i]:#최빈값의 key저장
        mx_dic.append(i)

if len(mx_dic)>1:#최빈값이 여러개라면
    print(mx_dic[1])#두번째로 작은 값  3)최빈값
else:#하나라면
    print(mx_dic[0])#해당 값 출력  3)최빈값
    
print(max(arr)-min(arr))#4) 범위








































































