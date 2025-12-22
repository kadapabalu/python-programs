balance=1000
def deposite(amount):
    global balance
    balance+=amount
def withdraw(amount):
    global balance
    if amount<=balance:
        balance-=amount
    else:
        printf("insufficient balance")
deposite(500)
withdraw(400)
print("Balance:",balance)
