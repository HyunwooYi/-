def read_single_digit(num) :
    if num == 1:
        return '일'
    if num == 2:
        return '이'
    if num == 3:
        return '삼'
    if num == 4:
        return '사'
    if num== 5:
        return '오'
    if num == 6:
        return '육'
    if num == 7:
        return '칠'
    if num== 8:
        return '팔'
    if num== 9:
        return '구'
    if num == 0:
        return '공'

    
def read_number(num):
    if num == 1:
        return '일'
    if num == 2:
        return '이'
    if num == 3:
        return '삼'
    if num == 4:
        return '사'
    if num== 5:
        return '오'
    if num == 6:
        return '육'
    if num == 7:
        return '칠'
    if num== 8:
        return '팔'
    if num== 9:
        return '구'
    if num == 0:
        return '공'
    


#주 프로그램
num = int(input('세 자리 정수 입력: '))
N = num

# 세 자리 정수
if num / 100 >=1:
    n1 = N//100
    N = N % 100
    result1 = read_number(n1)

    n2 = N//10
    N = N %10
    result2 =read_number(n2)

    n3 = N
    result3 = read_number(n3)
    print(result1, result2, result3)
    
# 두 자리 정수
elif num / 10 >=1:
    result1 = '공'
    n2 = N//10
    N = N %10
    result2 =read_number(n2)

    n3 = N
    result3 = read_number(n3)
    print(result1, result2, result3)

# 한 자리 정수
else:
    result1 = '공'
    result2 = '공'
    n3 = N
    result3 = read_single_digit(n3)
    print(result1, result2, result3)

    
    

