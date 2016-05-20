import math
position_1 = []
position_2 = []

def checkCollison (position_1, position_2):
    a = position_1[0] - position_2[0] # x coord
    b = position_1[1] - position_2[1] # y coord
    distance = position_2[2] + position_1[2]
    actual_distance = math.sqrt(math.pow(a,2) + math.pow(b, 2))
    print("actual_distance :", actual_distance)
    if actual_distance <= distance:
        return True
    else:
        return False

print('Type 2 ponits with radius')
x= int(input('Type x :'))
position_1.append(x)
y= int(input('Type y :'))
position_1.append(x)
d= int(input('Type d :'))
position_1.append(x)
x= int(input('Type x :'))
position_2.append(x)
y= int(input('Type y :'))
position_2.append(x)
d= int(input('Type d :'))
position_2.append(x)
if checkCollison(position_1, position_2):
    print('Too close ==> C')
else:
    print('OK')