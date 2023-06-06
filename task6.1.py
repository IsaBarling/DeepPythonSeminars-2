import datetime

TAX_THRESHOLD = 5000000  # Пороговое значение для начисления налога
WITHDRAWAL_FEE_PERCENTAGE = 1.5  # Процент комиссии за снятие
WITHDRAWAL_FEE_MIN = 30  # Минимальная комиссия за снятие
WITHDRAWAL_FEE_MAX = 600  # Максимальная комиссия за снятие
INTEREST_RATE = 0.03  # Процент начисления процентов
LOG_FILE = "atm_logs.txt"

class ATM:
    def __init__(self):
        self.balance = 0
        self.withdrawal_count = 0
        self.deposit_count = 0
        self.tax_collected = 0
        self.fee_collected = 0

    def deposit(self, amount):
        if amount % 50 != 0:
            print("Сумма пополнения должна быть кратной 50 у.е.")
            return

        self.balance += amount
        self.deposit_count += 1

        if self.deposit_count % 3 == 0:
            self.calculate_interest()

        if self.balance >= TAX_THRESHOLD:
            self.collect_tax()

        self.log_operation(f"Пополнение на {amount} у.е.")

    def withdraw(self, amount):
        if amount % 50 != 0:
            print("Сумма снятия должна быть кратной 50 у.е.")
            return

        withdrawal_fee = amount * WITHDRAWAL_FEE_PERCENTAGE / 100
        withdrawal_fee = max(withdrawal_fee, WITHDRAWAL_FEE_MIN)
        withdrawal_fee = min(withdrawal_fee, WITHDRAWAL_FEE_MAX)
        withdrawal_amount = amount + withdrawal_fee

        if withdrawal_amount > self.balance:
            print("Недостаточно средств на счете")
            return

        self.balance -= withdrawal_amount
        self.withdrawal_count += 1

        if self.withdrawal_count % 3 == 0:
            self.calculate_interest()

        if self.balance >= TAX_THRESHOLD:
            self.collect_tax()

        self.fee_collected += withdrawal_fee

        self.log_operation(f"Снятие {amount} у.е.")

    def calculate_interest(self):
        interest = self.balance * INTEREST_RATE
        self.balance += interest

    def collect_tax(self):
        tax = self.balance * 0.1
        self.tax_collected += tax
        self.balance -= tax

    def display_balance(self):
        print(f"Текущий баланс: {self.balance} у.е.")

    def print_receipt(self):
        print("============================================")
        print("Мини-чек:")
        print(f"Сумма налогов: {self.tax_collected} у.е.")
        print(f"Сумма комиссий: {self.fee_collected} у.е.")
        print("Спасибо за использование банкомата компании Tencent's!")

    def log_operation(self, operation):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp}: {operation}\n"
        with open(LOG_FILE, "a") as file:
            file.write(log_entry)

    def transaction_history(self, num_lines):
        with open(LOG_FILE, "r") as file:
            lines = file.readlines()
            num_lines = min(num_lines, len(lines))
            last_operations = lines[-num_lines:]
            print("История операций:")
            for operation in last_operations:
                print(operation.strip())

def atm_program():
    atm = ATM()

    print("Добро пожаловать в банкомат компании Tencent's")
    print("============================================")

    # Функция проверки PIN-кода
    def check_pin(pin):
        stored_pin = "1234"  # Здесь должен быть ваш хранимый PIN-код
        return pin == stored_pin

    # Функция выбора языка интерфейса
    def select_language():
        languages = {
            "1": "English",
            "2": "Русский"
        }

        print("Выберите язык:")
        for key, value in languages.items():
            print(f"{key}. {value}")

        language_choice = input("Введите номер языка: ")
        language = languages.get(language_choice)

        if language is None:
            print("Некорректный выбор. Установлен английский язык по умолчанию.")
            return "English"

        return language

    # Функция перевода средств между счетами
    def transfer_funds():
        from_account = input("Введите номер счета, с которого нужно перевести средства: ")
        to_account = input("Введите номер счета, на который нужно перевести средства: ")
        transfer_amount = int(input("Введите сумму перевода: "))

        if transfer_amount > atm.balance:
            print("Недостаточно средств на счете")
            return

        atm.balance -= transfer_amount
        atm.deposit_count += 1

        if atm.deposit_count % 3 == 0:
            atm.calculate_interest()

        if atm.balance >= TAX_THRESHOLD:
            atm.collect_tax()

        atm.log_operation(f"Перевод средств на счет {to_account}: {transfer_amount} у.е.")
        print("Перевод средств выполнен успешно")

    # Авторизация пользователя
    pin = input("Введите PIN-код: ")
    if not check_pin(pin):
        print("Неверный PIN-код. Доступ запрещен.")
        return

    # Выбор языка
    language = select_language()
    print(f"Выбран язык: {language}")

    while True:
        print("Выберите действие:")
        print("1. Пополнить счет")
        print("2. Снять со счета")
        print("3. Перевести средства")
        print("4. Посмотреть баланс")
        print("5. История операций")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            deposit_amount = int(input("Введите сумму для пополнения: "))
            atm.deposit(deposit_amount)

        elif choice == "2":
            withdrawal_amount = int(input("Введите сумму для снятия: "))
            atm.withdraw(withdrawal_amount)

        elif choice == "3":
            transfer_funds()

        elif choice == "4":
            atm.display_balance()

        elif choice == "5":
            num_lines = int(input("Введите количество последних операций для отображения: "))
            atm.transaction_history(num_lines)

        elif choice == "6":
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")

        atm.display_balance()

    atm.print_receipt()


atm_program()
