#a+b+c = 1000인 피타고라스 수 a,b,c  axbxc?

a = 1
while a:
    for i in range(1,999):
        for j in range(i,999):
            k = 1000-i-j
            if k <= 0:
                break
            b=list([i,j,k])
            b.sort()
            if b[0] ** 2 + b[1] ** 2 == b[2] ** 2:
                print(b)
                print(b[0]*b[1]*b[2])
                a=0
                break