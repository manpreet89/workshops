__author__ = 'jc443852'

color_names = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "blue1": "#0000ff", "brown1": "#ff4040",
               "brown4": "#8b2323", "cadetblue2": "#8ee5ee", "chartreuse1": "#7fff00","coral4": "#8b3e2f",
               "cornsilk4": "#8b8878", "darkgreen": "#006400"}

color = input("Enter the color name: ")
while color != "":
    if color in color_names:
        print(color_names[color])
    else:
        print("Invalid color name")
    color = input("Enter right color name: ")

for key in color_names:
    print(key,'is', color_names[key])
   # print('{} is {}'.format(key,STATE_NAMES[key]))