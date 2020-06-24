"""
Implement a function to determine the longest common string between
two given strings str1 and str2
"""

def check_common_longest(str1, str2):
    # Make the small string as str1
    if not len(str1)< len(str2):
        str1, str2 = str2, str1
    left_index=0
    right_index=0
    match_list = []
    while ( left_index < len(str1)):
        matches=""
        if str1[left_index] in str2:
            temp_right = str2.find(str1[left_index])
            temp_left = left_index
            while(str1[temp_left]==str2[temp_right]):
                matches+=str1[temp_left]
                temp_left+=1
                temp_right+=1
                if temp_left >= len(str1):
                    break
            match_list.append(matches)
        left_index+=1
    if not match_list:
        print("No match found")
    else:
        result = None
        for match in match_list:
            if not result:
                result = match
                continue
            if len(match) > len(result):
                result = match
        print("Match found is {}".format(result))
