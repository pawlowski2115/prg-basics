def f(amount_to_pay):
    five = amount_to_pay //5
    amount_to_pay = amount_to_pay % 5
    two = amount_to_pay // 2
    amount_to_pay = amount_to_pay % 2
    one = amount_to_pay // 1
    return five + two + one
