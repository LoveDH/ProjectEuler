#600851475143의 소인수 중에서 가장 큰 수

a = 600851475143
i=2
while i <= a :
    if a % i == 0 :
        a = a/i
        print(i)
        i = 2
    elif a ==1 :
        break
    else :
        i+=1


