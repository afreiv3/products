# product記帳程式
products = []
while True:
	name = input('輸入商品名稱:')
	if name == 'q':
		break
	price = input('輸入價格:')
	products.append([name, price])



with open('product.csv', 'w') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')