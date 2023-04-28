def search(f):
    if f not in shopping_bag:
        print(f'{f}은 없는 물건입니다.')
    else:
        print(f'{f}은(는) {shopping_bag.get(f)}개 담겨 있습니다.')
        

# 주 프로그램 작성
shopping_bag={}
print('[구입]')
while True:
    item = input(f'상품명? ')
        
    if item == '':
        break
        
    num = int(input('수량은? '))

    shopping_bag[item] = num
    print(f'장바구니에 {item}가 {num}개 담겼습니다.\n')

print('\n>>>장바구니 보기:', shopping_bag)

print('[검색]')
find = input('장바구니에서 확인하고자 하는 상품은? ')
search(find)
