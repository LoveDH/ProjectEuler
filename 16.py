#2^1000의 각 자리수를 모두 더하면?

a = str(2**1000)
sum = 0
for i in a :
    sum += int(i)

print(sum)