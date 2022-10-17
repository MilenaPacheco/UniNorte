import math 
def conver_seg(num):
    seg=num%60
    if num/60 >= 60:
        hor=(num/60)/60
        min=(num/60)%60
    else:
        min=num%60
        hor=0
    return str(math.trunc(hor)) + ':' + str(math.trunc(min)) + ':' + str(math.trunc(seg))
print(conver_seg(98240))