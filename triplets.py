"""
Implement python code to get the triplets such that their sum is 0
"""


l = [0, -1, 2, -3, 1]

sorted_l = sorted(l)

target_sum = -2
o_last_element = len(sorted_l)-1
o_first_element = 0

last_element = o_last_element
first_element = o_first_element

output_list = []

while(o_first_element<=(o_last_element+2)):
    for index in range(first_element+1, last_element):
        print("index {} first_element{} last_element {}".format(index,first_element,last_element))
        current_sum = l[first_element]+l[index]+l[last_element]
        if current_sum == target_sum:
            output_list.append([l[first_element],l[index],l[last_element]])
    iter_sum = l[o_first_element]+l[o_last_element]
    if iter_sum < target_sum:
        o_first_element+=1
        first_element = o_first_element
    else:
        o_last_element-=1
        last_element = o_last_element
    
print(output_list)
