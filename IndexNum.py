def find_element_in_list(element,list_element):
    for idx,val in enumerate(list_element):
        if int(element)==val:
            return idx
    return -1

list=[1,2,3,4,5,44,33,56,22,34,223,45,45,22,12,45,56,78,66]
num=input("Enter the number to be indexed: ")
print(num)
result=find_element_in_list(num,list)
print(result)