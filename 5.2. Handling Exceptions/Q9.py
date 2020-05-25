def change(subtotal, paid):
    return paid - subtotal
def change_num(subtotal, paid):
    bills = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
    money = change(subtotal, paid)
    ans = 0
    for bill in bills:
        add = int(money/bill) 
        ans += money//bill
        money %= bill
    return ans
print(change_num(8998, 10000))