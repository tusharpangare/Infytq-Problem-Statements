#lex_auth_0127382206342184961397

# def check_anagram(data1,data2):
     
        
    # data1_list=[i for i in data1.lower()]
    # data2_list=[i for i in data2.lower()]
    # print(data1_list)
    # print(data2_list)
     
    # count=0
    # # for (i,j) in zip(data1_list,data2_list):
    # for i in data1_list:
    #     for j in data2_list:
    #         if i==j and data1_list.count(i)==data2_list.count(j) and data1_list.index(i)!=data2_list.index(j):
    #             print(data1_list.index(i),i)
    #             print(data2_list.index(j),j)
    #             count+=1
    #             data1_list.remove(i)
    #             data2_list.remove(j)
    #             print(f"{count=}")

    # if len(data1_list)==len(data1_list) and len(data1_list)==count:
    #     return True   
    # else:
    #     return False           
                
def check_anagram(data1,data2):
    x=data1.lower()
    y=data2.lower()
    count=0
    if len(data1)==len(data2):
        for i in range(0,len(data1)):
            if x[i]!=y[i]:
                count+=1
    if count==len(data1)  and sorted(data1.lower())==sorted(data2.lower()):
        return True
    else:
        return False    

    
print(check_anagram("silent","listen"))