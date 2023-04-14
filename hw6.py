#2단 ~ 5단까지 한 뭉치
def gugudan(n) :
    for h in range(1,10,1):

        for i in range(n,n+4,1):
            print(f'{i} x {h} = {i*h:2d}', end='   ')

        print()
    print()



# 주 프로그램
gugudan(2)
gugudan(6)
