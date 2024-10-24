
count = 0
for i in range(100,501):
    i1 = i%10 #первая цифра
    i = i//10
    i2 = i%10 #вторая цифра 
    i3 = i//10 #третья цифра
    if i1+i2+i3==15:
        count+=1

print(count)
