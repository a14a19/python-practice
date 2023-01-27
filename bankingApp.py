class Bank:
    def __init__(self, initial_amount = 0.00):
        self.balance = initial_amount

    def log_transaction(self, transactions):
        with open('transactions.txt', 'a') as file:
            file.write(f'{transactions}')

    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.log_transaction(f'Debited: ${amount}\t\t\tBalance: ${self.balance}\n')

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.log_transaction(f'Credited: ${amount}\t\t\tBalance: ${self.balance}\n')
    
new_account = Bank(0.00)
while True:
    try:
        userInput = input('Please choose, Withdrawal(w), Deposit(d) or help?\n')
        userInput = userInput.lower()
    except KeyboardInterrupt:
        print('\nLeaving the ATM\n')
        break
    if userInput in ['w', 'd', 'withdrawal', 'deposit', 'exit', 'view', 'passbook', 'help']:
        if userInput == 'w' or userInput == 'withdrawal':
            amount = input(f'How much do you want to withdraw?\n') 
            new_account.withdrawal(amount)
            print(f'Your balance is: ${new_account.balance}')
        elif userInput == 'd' or userInput == 'deposit':
            amount = input('How much do you want to deposit?\n')
            new_account.deposit(amount)
            print(f'Your balance is: ${new_account.balance}')
        elif userInput == 'view' or userInput == 'passbook':
            with open('transactions.txt', 'r') as file:
                file = file.read()
            print(f'Passbook: \n{file}')
        elif userInput == 'help':
            print('\nw, withdrawal: To withdraw amount\nd, deposit: To deposit amount\nview, passbook: To view the transaction log\nexit: To exit\nhelp: help\n')
        elif userInput == 'exit':
            break
        
    else:
        print('Please enter a valid input.\n')
