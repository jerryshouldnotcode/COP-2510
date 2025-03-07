'''
Name: Jeremiah Adeyemi
U-Number: U58971672
Description: using OOP concepts and string formatting to print out
             inputed inventory of retail items in a store.

'''

#retailitems.py

class Retailitem:

    def __init__(self, itemtype, amount, price):
        self.__itemtype = itemtype
        self.__amount = amount
        self.__price = price


    def __str__(self):
        return self.__itemtype.ljust(15) + self.__amount.center(15) + '$' + self.__price.rjust(15)


def main():
    num_items = int(input('How many items wil you add today?: '))

    while num_items < 1:
        print('Invalid input.' ,end = '')
        num_items = int(input('How many items wil you add today?: '))

    list_items = []

    for i in range(1, num_items+1):
        name = input(f'Name of item {i}: ')
        amount = input(f'Amount of item {i}: ')
        price = input(f'Price of item {i}: ')
        print(' ')
                     
        item_obj = Retailitem(name, amount, price)
        list_items.append(item_obj)

    print(' ')
    print('Here is a summary of the 3 items you added:')
    print(' ')

    x, y, z = 'Item', 'Amount',  'Price'

    print(f'{x.ljust(15)} {y.center(15)} {z.rjust(15)}')
    print(f'----------------------------------------------') #lol

    for obj in list_items:
        print(obj)
        
if __name__ == "__main__":
    main()
