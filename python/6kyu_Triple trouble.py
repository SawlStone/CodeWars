def triple_double(num1, num2):
    # code me ^^
    list_num1 = [int(x) for x in str(num1)]
    list_num2 = [int(x) for x in str(num2)]

    res_list1 = []
    res_list2 = []

    step1 = 0
    while step1 < len(list_num1):
        for i in range(len(list_num1)-1):
            if list_num1[i-1] == list_num1[i] or list_num1[i] == list_num1[i+1]:
                res_list1.append(list_num1[i])
            step1 += 1

    step2 = 0
    while step2 < len(list_num2):
        for j in range(len(list_num2)-1):
            if list_num2[j-1] == list_num2[j] or list_num2[j] == list_num2[j+1]:
                res_list2.append(list_num2[j])
            step2 += 1

    if len(res_list1) >= 1 and len(res_list2) >= 1:
        return 1
    else:
        return 0