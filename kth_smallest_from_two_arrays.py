def kth_smallest_element(k):
    s1 = [200,300,400,900]
    s2 = [100,500,600,700]
    len_s1 = len(s1)
    len_s2 = len(s2)
    if k > (len_s1+len_s2):
        print("k value is out of bounds")
    i = 0
    j = 0
    result_value = None
    result_index = 0
    while(i<len_s1 and j<len_s2):
        if s1[i]>s2[j]:
            result_value = s2[j]
            j = j+1
        else:
            result_value = s1[i]
            i = i+1
        result_index = result_index + 1
        if(k==result_index):
            return result_value
    while i<len_s1:
        result_value = s1[i]
        i = i+1
        result_index = result_index + 1
        if(k==result_index):
            return result_value
    while j<len_s2:
        result_value = s2[i]
        j = j+1
        result_index = result_index + 1
        if(k==result_index):
            return result_Value

