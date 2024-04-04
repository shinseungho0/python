# 약수구하기
#cnt, hab = 0, 0

#num = int(input("숫자를 입력하세요: "))
#for i in range(1, num +1):
#    if num % i == 0:
#        print(i, end = ' ')
#        cnt += 1
#        hab += i
#print()
#print("약수의 합:", hab)
#print("약수의 개수: ", cnt)

# 소수구하기

# 1. 소수는 약수가 2개이다.
"""

num = int(input("숫자를 입력하세요: "))
cnt = 0

for i in range(1,num+1):
    if num % i == 0:
        cnt += 1
if cnt == 2:
    print(f"{num}은 소수입니다.")
else:
    print("{0}은 소수가 아닙니다.".format(num))
# 2. 피제수를 제수로 나누었을 때 나머지가 0이될때까지 나누어서 피제수와 제수가 같으면 소수이다. ex) 5를 2부터 나눈다 2, 3, 4 5  5로나누면 나머지 0 /2, 3, 4는 0이안된
   # 다.

for i in range(2, num +1):
    if num % i == 0:
        break; #루프(for, while)을 빠져나간다.

if num == i:
    print(f"{num}은 소수입니다.")
else:
    print(f"{num}은 소수가 아닙니다.")

# 3 최대 최소

max, min = 1, 10
for i in range(1, 6):
    num = int(input("%d번째 숫자: "%i))
    if max < num:
        max = num
    if min > num:
        min = num
print(f"최대: {max} 최소:{min}")


num = int(input("1번째 숫자:"))
max = min = num
for i in range(2, 6):
    num = int(input("%d번째 숫자:"%i))
    if max < num:
        max = num
    if min > num:
        min = num
print("최대값: ", max, " 최소값: ", min)
"""

sum = 0
i = 1
while i <= 10:
    sum += i
    i+=1
print("1 ~ 10 사이의 합은 ", sum)

dan = int(input("단으 입력하세요: "))
num = 1
while num < 10:
    res = dan * num
    print("%d x %d = %d" %(dan, num, res))
    num+=1

dan = 2
while dan <= 9:
    num = 1
    while num <= 9:
        res = dan * num
        print("%d x %d = %d" %(dan, num, res))
        num+=1
    print()
    dan += 1
