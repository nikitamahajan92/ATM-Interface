class BankAccount:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Amount Deposited: +${amount}')
            return f'Deposit successful. New Balance: ${self.balance}'
        return "Deposit amount must be greater than 0."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Amount Withdrawn: -${amount}')
            return f'Withdrawal successful. New Balance: ${self.balance}'
        return "Withdrawal amount is invalid or exceeds your balance."

    def display_transaction_history(self):
        if not self.transaction_history:
            return "No transactions yet."
        return '\n'.join(self.transaction_history)

    def transfer(self, recipient_account, amount, all_accounts):
        recipient_account = all_accounts.get(recipient_account)
        if recipient_account:
            if amount > 0 and self.balance >= amount:
                self.balance -= amount
                recipient_account.balance += amount
                self.transaction_history.append(f'Amount transferred to {recipient_account.account_number}: ${amount}')
                recipient_account.transaction_history.append(f'Amount received from {self.account_number}: ${amount}')
                return f'Transfer successful. New Balance: ${self.balance}'
            return "Transfer amount is invalid or exceeds your balance."
        return "Recipient account does not exist."

    def quit(self):
        return "Thank you for using the ATM. Have a great day!"

def main():
    account_numbers = ["363123", "384234", "785567", "123456", "654321", "789012"]
    pin_store = [234, 345, 567, 111, 222, 333]
    balances = [1000, 2000, 3267, 500, 1200, 2500]

    accounts = {num: BankAccount(num, pin, bal) for num, pin, bal in zip(account_numbers, pin_store, balances)}

    account_no = input("Enter your account number: ")
    account_pin = int(input("Enter your account pin: "))

    current_account = accounts.get(account_no)

    if current_account and current_account.pin == account_pin:
        while True:
            print("\n-----ATM OPERATIONS AVAILABLE------")
            print("1. Deposit funds")
            print("2. Withdraw funds")
            print("3. View transaction history")
            print("4. Transfer funds to another account")
            print("5. Quit")
            choice = int(input("Please select an option (1-5): "))

            if choice == 1:
                print("\n-----DEPOSIT FUNDS------")
                amount = float(input("Enter the amount to deposit: $"))
                print(current_account.deposit(amount))
                print("\n" + "-" * 40 + "\n")
            elif choice == 2:
                print("\n-----WITHDRAW FUNDS------")
                amount = float(input("Enter the amount to withdraw: $"))
                print(current_account.withdraw(amount))
                print("\n" + "-" * 40 + "\n")
            elif choice == 3:
                print("\n-----TRANSACTION HISTORY------")
                print(current_account.display_transaction_history())
                print("\n" + "-" * 40 + "\n")
            elif choice == 4:
                print("\n-----TRANSFER FUNDS------")
                recipient_account_no = input("Enter the recipient account number: ")
                amount = float(input("Enter the amount to transfer: $"))
                print(current_account.transfer(recipient_account_no, amount, accounts))
                print("\n" + "-" * 40 + "\n")
            elif choice == 5:
                print(current_account.quit())
                print("\n" + "-" * 40 + "\n")
                break
            else:
                print("Invalid choice! Please select a number between 1 and 5.")
                print("\n" + "-" * 40 + "\n")
    else:
        print("Account not found or incorrect PIN. Please check your account number and PIN.")
        print("\n" + "-" * 40 + "\n")
        return

if __name__ == "__main__":
    main()
