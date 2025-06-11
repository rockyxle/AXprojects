# 1. Estimate vlue after exchange
def exchange_money(budget, exchange_rate):
    # Return value of exchanged currency
    exchanged_money_value = budget/exchange_rate
    return exchanged_money_value

def get_change(budget, exchanging_value):
    change = budget - exchanging_value
    return change


def get_value_of_bills(denomination, number_of_bills):
    bill_value = denomination * number_of_bills
    return int(bill_value)

def get_number_of_bills(amount, denomination):
    if amount%denomination == 0:
        number_of_bills = amount/denomination
        return number_of_bills
    elif amount%denomination != 0:
        remainder = amount%denomination
        rounded_amount = amount - remainder
        number_of_bills = rounded_amount/denomination
        return int(number_of_bills)

def get_leftover_of_bills(amount, denomination): 
   leftover_of_bills = amount % denomination
   return leftover_of_bills

def exchangeable_value(budget, exchange_rate, spread, denomination):
    percent_fee = float(spread/100) * exchange_rate # calculate spread as percentage of exchange rate
    # calculate new exchange rate
    total_exchange_rate = exchange_rate + percent_fee
    # calculate how much total value after new exchange rate
    max_currency = budget / total_exchange_rate
    # get how many bills
    number_of_bills = max_currency // denomination # floor division
     # get total rounded value of money after exchange
    max_value = int(number_of_bills) * denomination
    return max_value

print(exchange_money(127.5, 1.2))
print(get_change(127.5, 120))
print(get_value_of_bills(5,128))
print(get_number_of_bills(127.5, 5))
print(get_leftover_of_bills(127.5, 20))
print(exchangeable_value(127.25, 1.20, 10, 20))
print(exchangeable_value(127.25, 1.20, 10, 5))
