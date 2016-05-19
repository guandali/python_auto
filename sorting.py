# A sorting porgram, sorting a list

num_arr = list()
print('Enter 10 elements: \n')
valid_arr =True
NUM_ARR_LEN = 10
num_arr = []
ans_arr = []


def handleMax(num_arr):
    cur_max = num_arr[0]
    max_index = 0
    for i in range (1,len(num_arr) ):
        if num_arr[i] > cur_max:
            cur_max = num_arr[i]
            max_index = i

    num_arr.pop(max_index)
    print('After pop list[1] at handleMax:  ', num_arr)
    #for i range(0, )
    return [cur_max]


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
            length = len(num_arr)
            for i in range (0,length ):
                max_val = handleMax(num_arr)
                #print('cur_max is  :',max )
                ans_arr.append(max_val)
                #print('After deleted list[0] at main:  ', num_arr)

            print('sorted arr is :',ans_arr)