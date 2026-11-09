#My solution
price = 1_000_000
is_good_credit = True

down_payment = 0

if is_good_credit:
  down_payment = price * 0.1

else:
  down_payment = price * 0.2


print(f'''Down Payment: ${down_payment}''')

#Mosh Solution
price = 1000000
has_good_credit = True

if has_good_credit:
  down_payment = 0.1 * price
else:
  down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")