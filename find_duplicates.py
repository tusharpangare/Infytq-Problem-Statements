# python set 2
# assign 6.6
#lex_auth_01269443477535129681

def find_duplicates(list_of_numbers):
    duplicate_list=[]
    for i in list_of_numbers:
        if list_of_numbers.count(i)>1:
            if i not in duplicate_list:
                duplicate_list.append(i)
    return duplicate_list        

    #start writing your code here

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)