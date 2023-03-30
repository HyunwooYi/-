def get_fixed_price(discount_price) :
    
    rate = discount_rate * 0.01
    num = float(1 - rate)
    result = float(discount_price / num)
    
    return int(result)
    

discount_rate = float(input('할인율은? '))
A_discount_price = float(input('A 상품의 할인된 가격은? '))
B_discount_price = float(input('B 상품의 할인된 가격은? '))

result_A = int(get_fixed_price(A_discount_price))
result_B = int(get_fixed_price(B_discount_price))

print('A 상품의 정가는', result_A, '원')
print('B 상품의 정가는', result_B, '원')

