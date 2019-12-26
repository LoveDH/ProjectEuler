#1부터 1000까지 영어로 썼을때의 글자수

number_set = ['','one','two','three','four','five','six','seven','eight','nine']
def cal(num):
    sentence = ''
    hundred = num//100
    for i in range(0,10):
        if hundred == 0:
            continue
        elif hundred == i:
            sentence += number_set[i] + ' hundred'
    num = num%100
    ten = num//10
    if sentence.endswith('red'):
        sentence += ' and '

    if ten == 2:
        sentence += 'twenty'
    elif ten == 3:
        sentence += 'thirty'
    elif ten == 4:
        sentence += 'forty'
    elif ten == 5:
        sentence += 'fifty'
    elif ten == 6:
        sentence += 'sixty'
    elif ten == 7:
        sentence += 'seventy'
    elif ten == 8:
        sentence += 'eighty'
    elif ten == 9:
        sentence += 'ninety'

    if sentence.endswith('red'):
        sentence+=' and '

    for i in range(0, 10):
        if num//10 == 1:
            break
        num = num%10
        if sentence.endswith('ty'):
            sentence+='-'
        if num == i:
            sentence += number_set[i]


    if sentence.endswith('red'):
        sentence+=' and '

    if num == 10 :
        sentence += 'ten'
    elif num == 11 :
        sentence += 'eleven'
    elif num == 12 :
        sentence += 'twelve'
    elif num == 13:
        sentence += 'thirteen'
    elif num == 14:
        sentence += 'fourteen'
    elif num == 15:
        sentence += 'fifteen'
    elif num == 16:
        sentence += 'sixteen'
    elif num == 17:
        sentence += 'seventeen'
    elif num == 18:
        sentence += 'eighteen'
    elif num == 19:
        sentence += 'nineteen'

    if sentence.endswith('-') :
        sentence = sentence[:-1]
    elif sentence.endswith('and '):
        sentence = sentence[:-4]

    sentence = sentence.strip()
    if '-' in sentence:
        sentence = sentence.replace('-', '')
    count_chr = 0
    print(sentence)
    words = sentence.split()
    for word in words :
        count_chr += len(word)

    return count_chr

count = 0
for i in range(1,1000):
    count += cal(i)

count = count+len('onethousand')
print(count)