# храним баланс
Balance = 0

# записываем в словарь название покупки и их стоимость
SHOP = {}

#храним баланс
def updait_balance(balance):
   global Balance
   Balance +=balance
   return Balance

def shop_apdeit(name,cost):
  global Balance
  if Balance>=cost:
    Balance -= cost
    SHOP[name] =cost
    return True
  return False

# получить баланс
def get_balance():
  return  Balance

# получить список покупок
def history_shop():
  return SHOP

# функция печати
def print_tekst():
    print('\n1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход\n')

def bank_account():

    while True:
        print_tekst() # печатаем стандартый текст
        choice = input('Выберите пункт меню ')
        if choice == '1':
            balance= int(input("На какую сумму будем пополнять? "))
            updait_balance(balance)
        elif choice == '2':
            cost = int(input("Сумма покупки? "))
            if get_balance() >= cost: # если баланса хватает, то заносим в словарь
                Name_shop = input("название  покупки ")
                shop_apdeit(Name_shop,cost)
            else:
                print("не достаточно денег")
        elif choice == '3':
            k=history_shop()
            for key, value in k.items():
                print(f'покупка {(key)} за {value} рублей')
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

# если здесь запущена программа, то выполнять код основной
if __name__ == "__main__":
    bank_account()