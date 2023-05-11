def find(lst):
    k_lst=[]
    print('[검색]')
    v = input('장바구니에서 확인하고자 하는 상품은? ')
    for key in lst.keys():
        k_lst.append(key)

    if v not in k_lst:
        print(f'장바구니에 {v}은(는) 없습니다.')
    else:
        print(f'{v}은(는) {lst.get(v)}개 담겨 있습니다.')


def buy(lst):
    k = input(f'상품명? ')
    if k == '':
        return False
        
    v = int(input('수량은? '))
    lst[k] = v
    print(lst)

    print(f'장바구니에 {k}가 {v}개 담겼습니다.\n')

def show(lst):
    print('\n>>>장바구니 보기:', lst)



# 주 프로그램 작성
shopping_bag={}
print('[구입]')
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
