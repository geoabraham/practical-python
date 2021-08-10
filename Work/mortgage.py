# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000.0
months_extra_payment = 12
total_paid = 0.0

while principal > 0:
    if months_extra_payment != 0:
        principal = principal * (1 + rate / 12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        months_extra_payment -= 1
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment

print('Total paid', total_paid)
