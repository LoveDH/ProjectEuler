#세자리수를 곱해 만들 수 있는 가장 큰 대칭수
a = list()
for i in range(100,1000) :
    for j in range(100,1000):
        b = str(i*j)
        if str(i*j) == str(i*j)[::-1] :
            a.append(i*j)
print(max(a))