def bubblesort(input_list):
    len_input = len(input_list)
    i = 0
    while(i<len_input):
        j = i+1
        while(j<len_input):
            print("Processing {0} and {1}".format(i,j))
            if input_list[i]>input_list[j]:
                # swap i and j
                temp = input_list[i]
                input_list[i]=input_list[j]
                input_list[j]=temp
            j=j+1
        i+=1
    print("Bubble sorted array is {}".format(input_list))
