lower = 40
upper = 100
#print("Enter a number (" + str(lower) + "-" + str(upper) + "):")
str = "enter a number {} - {}:".format(lower,upper)
print(str)
for i in range(lower,upper):
          print("{:>6} {:>6}".format(i, chr(i)))
