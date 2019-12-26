#1부터 100까지 합의 제곱과 제곱의 합의 차이

sum1 = 0
sum2 = 0
for i in range(1,101) :
    sum1 += i**2
    sum2 += i
    sum22 = sum2**2

print(sum22-sum1)