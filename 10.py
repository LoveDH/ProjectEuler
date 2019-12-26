#이백만 이하의 소수의 합은?
#못 품... 이건 답
#에라토스테네스의 체

nl = []
NUM = 2000000
for i in range(NUM):
    nl.append(True)

total = 2

for i in range(3,NUM,2):
    if nl[i]:
        total += i
        print(i)
        for j in range(i,NUM,i):
            nl[j] = False

print(total)