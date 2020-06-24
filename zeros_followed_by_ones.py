#l = [1, 1, 0, 0, 0, 1, 0]

l = [ 1, 1, 0, 1, 1, 1, 0]
zero_index = 0
one_index = len(l)-1

for index in range(len(l)):
    print(index)
    print(zero_index)
    print(one_index)
    if zero_index+1 == one_index:
        break
    if zero_index<=one_index:
        if l[index]==0:  
            l[zero_index],l[index]=l[index],l[zero_index]
            zero_index+=1
        else:
            l[one_index],l[index]=l[index],l[one_index]
            one_index-=1
    print(l)
    if l[zero_index]>l[one_index]:
        l[zero_index], l[one_index] = l[one_index],l[zero_index]
print(l)
