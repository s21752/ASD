
def sort_mine(data):
    lower_sign = data[0]
    left = 0
    right = len(data) - 1
    
    lower_check = False
    
    print(data)
    
    while (left < right) :
        if (data[left] != data[right]):
            if lower_check == False:
                lower_check = True
                if data[left] < lower_sign or data[right] < lower_sign:
                    if data[left] < data[right]:
                        lower_sign = data[left]
                    else:
                        lower_sign = data[right]
                    left = 0
                    right = len(data) - 1
                continue
            else:
                if (data[left] != lower_sign):
                    data[left],data[right] = data[right],data[left]
            left += 1
            right -= 1
        else:
            if (data[left] == lower_sign):
                left += 1
            else:
                right -= 1
    
    print(data)
    

data = [4,3,3,3,3,3,3,3,3,3,4,3,4,4,4,3,4,3,3,3,4,3,4,3,4,4,4,4,3,3,4,3,4,3,3,4,3,4,3,4,4,4]
data2 = [4,3,3,3,3,4,3,4,3,3,4,4,4,4,4,3,3,3,4,3,4,3,4,3,4]

data4 = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,4]

data3 = [2,1,2,1,2,1,2,1,1,1,1,1,1]

sort_mine(data4)
