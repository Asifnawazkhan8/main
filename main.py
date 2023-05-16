
def sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
num = [ 8,5,3,4,1,2,0,7,9,6 ]
sort(num)
print(num)