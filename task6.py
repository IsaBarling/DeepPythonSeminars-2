TAX_THRESHOLD = 5000000  # Пороговое значение для начисления налога
WITHDRAWAL_FEE_PERCENTAGE = 1.5  # Процент комиссии за снятие
WITHDRAWAL_FEE_MIN = 30  # Минимальная комиссия за снятие
WITHDRAWAL_FEE_MAX = 600  # Максимальная комиссия за снятие
INTEREST_RATE = 0.03  # Процент начисления процентов

def atm_program():
    balance = 0
    withdrawal_count = 0
    deposit_count = 0
    tax_collected = 0
    fee_collected = 0

    print("Добро пожаловать в банкомат компании Tencent's")
    print("============================================")

    while True:
        print("Выберите действие:")
        print("1. Пополнить счет")
        print("2. Снять со счета")
        print("3. Выйти")
        
        choice = input("Введите номер действия: ")

        if choice == "1":
            deposit_amount = int(input("Введите сумму для пополнения: "))
            if deposit_amount % 50 != 0:
                print("Сумма пополнения должна быть кратной 50 у.е.")
                continue

            balance += deposit_amount
            deposit_count += 1

            if deposit_count % 3 == 0:
                interest = balance * INTEREST_RATE
                balance += interest

            if balance >= TAX_THRESHOLD:
                tax = balance * 0.1
                tax_collected += tax
                balance -= tax

        elif choice == "2":
            withdrawal_amount = int(input("Введите сумму для снятия: "))
            if withdrawal_amount % 50 != 0:
                print("Сумма снятия должна быть кратной 50 у.е.")
                continue

            withdrawal_fee = withdrawal_amount * WITHDRAWAL_FEE_PERCENTAGE / 100
            withdrawal_fee = max(withdrawal_fee, WITHDRAWAL_FEE_MIN)
            withdrawal_fee = min(withdrawal_fee, WITHDRAWAL_FEE_MAX)
            withdrawal_amount += withdrawal_fee

            if withdrawal_amount > balance:
                print("Недостаточно средств на счете")
                continue

            balance -= withdrawal_amount
            withdrawal_count += 1

            if withdrawal_count % 3 == 0:
                interest = balance * INTEREST_RATE
                balance += interest

            if balance >= TAX_THRESHOLD:
                tax = balance * 0.1
                tax_collected += tax
                balance -= tax

            fee_collected += withdrawal_fee

        elif choice == "3":
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")

        print(f"Текущий баланс: {balance} у.е.")
    
    print("============================================")
    print("Мини-чек:")
    print(f"Сумма налогов: {tax_collected} у.е.")
    print(f"Сумма комиссий: {fee_collected} у.е.")
    print("Спасибо за использование банкомата компании Tencent's!")

atm_program()
