##fibnums = [1,1]
##for x in range(2,100):
##	fibnums.append(fibnums[x-1] + fibnums[x-2])
##print(fibnums)

##fibnums = list(range(0,20))
##fibnums[0] = fibnums[1] = 1
##print(fibnums)
##
##for y in range(2,20):
##    fibnums[y] = (fibnums[y-1] + fibnums [y-2])
##
##print(fibnums)
##size = len(fibnums)
##del(fibnums[size - 1])
##print(fibnums)

shopping_list = ['apples', 'bananas', 'straberries', 'cookies', 'Jesus', 'Rama','asfljsk',]
size = len(shopping_list)

for x in range (0,size):
	 print('Item %s in shopping list is %s' % (x+1,shopping_list[x]))
	 
itemnumber = 1
for item in shopping_list:
	 print('Item %s in shopping list is %s' % (itemnumber,item))
	 itemnumber = itemnumber + 1
	 
jesus = ['Apples','Oranges', 'bananas', 'straberries', 'cookies', 'Jesus', 'Rama']
shooty = len(jesus)

for y in range (0,shooty):
    print('Item %s in jesus is %s' % (y+1, jesus[y]))
