# A sorting porgram, sorting a list

num_arr = list()
print('Enter 10 elements: \n')
valid_arr =True
NUM_ARR_LEN = 3


def handleMax(list):
    #cur = list[0]
    list.pop(1)
    print('After pop list[1] at handleMax:  ', list)
    #for i range(0, )
    return


for i in range(0, NUM_ARR_LEN):
    n = input("num :" )
    try:
        num_arr.append(int(n))
    except ValueError:
        print('Error input')
        valid_arr = False
        break;
if valid_arr:
            print("Array is :" , num_arr)
            handleMax(list)
            print('After deleted list[0] at main:  ', list)

