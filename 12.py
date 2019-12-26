#500개 이상의 약수를 갖는 가장 작은 삼각수는?

#삼각수를 i로 나누면, 삼각수/i도 약수기 때문에 250개만 세어도 된다.

def counting_divisors(triangle_number):
    divisors = []
    for i in range(1, triangle_number+1):
        if triangle_number % i == 0:
            divisors.append(i)
        elif i**2 > triangle_number or triangle_number/i <i:
            break
    return len(divisors)

stopper = True
triangle_number = 0
number_to_add = 1

while stopper:
    triangle_number += number_to_add
    number_to_add += 1
    divisor_count = counting_divisors(triangle_number)
    if divisor_count >= 250:
        stopper = False
    print(triangle_number, divisor_count)
print(triangle_number)