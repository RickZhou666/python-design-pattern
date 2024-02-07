class BankAccount:
    def __init__(self, name, timestamp=0, balance = 0) -> None:
        self.name = name
        self.timestamp = 0
        self.balance = balance

class BankSystem:
    def __init__(self) -> None:
        self.account_mapper = {}

    def create_account(self, account):
        acct = BankAccount(account)
        self.account_mapper[account] = acct
        return 'true'

    def deposit(self, account, amount):
        if account in self.account_mapper:
            acct = self.account_mapper[account]
            acct.balance += int(amount)
            return str(acct.balance)
        

    def pay(self, account, amount):
        if account in self.account_mapper:
            acct = self.account_mapper[account]
            acct.balance -= int(amount)
            return str(acct.balance)

if __name__ == '__main__':
    queries = [
        ['create_account', 'acct1'],
        ['deposit', 'acct1', '2000'],
        ['pay', 'acct1', '100'],
        ['pay', 'acct1', '200'],
        ['deposit', 'acct1', '100'],
    ]
    bs = BankSystem()
    
    ans = []
    for query in queries:
        if query[0] == 'create_account':
            ans.append(bs.create_account(query[1]))
        elif query[0] == 'deposit':
            ans.append(bs.deposit(query[1], query[2]))  
        elif query[0] == 'pay':
            ans.append(bs.pay(query[1], query[2]))

    print(ans)