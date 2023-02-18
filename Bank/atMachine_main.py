from Bank.bank import bank

if __name__ == '__main__':
    atm = bank()
    atm.create_account_for("Josh" "1234", "1", 0)
    atm.create_account_for("Ayo" "1234", "2", 0)
    mybank = int(input("much to deposit"))
    atm.deposit_into(mybank, 1)

    atm.transfer(500, 1, 2, 1234)
    atm.withdraw_from(1000, 1, 1234)
    print(atm.find_account(1))
