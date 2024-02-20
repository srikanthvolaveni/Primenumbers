number = int(input("enter the num: "))
res = []
for i in range(2,number+1):
    count = 0
    for j in range(2,i):
        if(i%j == 0):
            count += 1
    if (count == 0):
        res.append(i)
print(res)