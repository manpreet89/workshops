__author__ = 'JC443852'
instruction = "welcome to our program.\nInputnegative number into number of items to quit"
print(instruction)
numOfitems = 1
while numOfitems > 0:
    numOfitems = int(input(" please input the number of items :"))
    costPeritem = float(input("the shipping cost per item :$ "))

    totalShipcost = numOfitems * costPeritem
    if totalShipcost > 100:
        totalShipcost = totalShipcost * 0.9
    print(" the total cost of delevering your product is :", totalShipcost)