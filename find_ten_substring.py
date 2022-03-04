#Infytq assignment on exception handeling

#python set 2
#assignment  6.5

#lex_auth_01269442545042227276

def find_ten_substring(num_str):
    result_list=[]
    for i in range(0,len(num_str)):
        sum=0
        num=""
        for j in range (i,len(num_str)):
            sum=sum+int(num_str[j])
            if sum<10:
                num=num+num_str[j]
            elif sum==10:
                num=num+num_str[j]
                result_list.append(num)
            else:
                break
    return result_list

num_str="3005002002"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)



 