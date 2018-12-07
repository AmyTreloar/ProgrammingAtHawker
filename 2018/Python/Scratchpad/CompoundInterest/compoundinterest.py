inflation = [0.0233, 0.0444, 0.0174, 0.0289, 0.0333, 0.0171, 0.0248, 0.0251, 0.0151, 0.0093, 0.0064]
average_inflation = sum(inflation)/len(inflation)
present_value = 500_000
rate = 0.09
number = 10

future_value = present_value * (1 + rate)**number

print(future_value)
repayment = future_value-present_value
print(repayment)


current_value = present_value

for i in inflation:
    current_value = current_value + current_value*i
print(current_value, future_value/(current_value+(repayment/2)))

current_value=present_value

for i in inflation:
    current_value = current_value + current_value*average_inflation

print(current_value, future_value/current_value)
