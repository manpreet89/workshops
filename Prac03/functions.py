__author__ = 'manpreet'
def inch_to_meter(inch):
    return inch * 0.0254
print(inch_to_meter(48))

tax = 0
income = float(input("income:"))
if income > 16000:
    tax = (income-16000)*0.3
print(tax)

