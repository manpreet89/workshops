__author__ = 'JC443852'
def tax_return(income):
    if income <= 16000:
        return 0
    else:
        return(income-16000) * 0.30
print(tax_return(15000))