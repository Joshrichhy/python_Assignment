from Bank.account import account


class bank:

    def __init__(self):
        self.accounts = []

    def create_account_for(self, full_name, pin, balance):
        account_number = len(self.accounts) + 1
        new_account = account(full_name, account_number, pin, balance)
        self.accounts.append(new_account)

    def get_numbers_of_accounts(self):
        return len(self.accounts)

    def find_account(self, account_number):
        return self.accounts[account_number - 1]

    def check_balance_for(self, account_number, pin):
        check_account = account
        check_account.get_balance(self.find_account(account_number), pin)

    def deposit_into(self, amount, account_number):
        account_to_deposit = account
        account_to_deposit = self.find_account(account_number)
        account_to_deposit.deposit(amount)

    def withdraw_from(self, amount, account_number, pin: int):
        account_from_account = account
        account_from_account.withdrawal(self.find_account(account_number), amount, pin)

    def transfer(self, amount, sender_account_number, receiver_account_number, pin: int):
        self.withdraw_from(amount, sender_account_number, pin)
        self.deposit_into(amount, receiver_account_number)

    def delete_account_for(self, account_number):
        account_to_be_deleted = account
        account_to_be_deleted = self.find_account(account_number)
        self.accounts.append(account_number, None)
        self.accounts.remove(account_to_be_deleted)

    def check_all_account(self):
        for acct in range(0, len(self.accounts)-1, 1):
            print(acct)
