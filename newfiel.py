
# # 1st answer:-----------------------------------------------------------------------------

# a = [20,90,100,55,80,200,5000]
# # first_largest = second_largest = third_largest
# # print(max(a,key=lambda value: int(value)))
# # a = [2,5,6,7,9,8,10]
# n=0
# for i in range(n+1):
#     print("third larget number is:",a[n-3])
# # for num in a:
# #     if num > first_largest:
# #         third_largest=second_largest
# #         second_largest=first_largest
# #         first_largest=num
# #     elif num > second_largest and num!=first_largest:
# #         third_largest=second_largest
# #         second_largest=num
# #     elif num > third_largest and num!=second_largest:
# #         third_largest=num
# #     print("third largest number:",a[third_largest])
     
#     # 3rd question__________________________________________________________________________________
# a={"name":"kriss","age":20,"phone_Number":9805158520,"car":"BMW"}
# lst =[]
# lst1 = []
# for keys,values in a.items():
#     if keys != "phone_number":
#         lst.append(keys)
#         lst1.append(values)
#         # a.pop('phone_number')
# print("list of key :",lst)
# print("list of values :",lst1)


# # 2ndd answer==========================================================

#     # 0,1,22,3,4444,5,666666,7,88888888,9,10101010101010101010
# n=11
# series = []
# for i in range(n):
#     if i % 3 == 0:
#         series.append(i)
#     else:
#         series.append(int(str(i)*i))
# print (series)
 


    
# #*************** 4nd answer:************************************-------------------------------------------------------------------------------
# number = 912375781293812637398236
# number_str = str(number)
# digits_sum = 0
# for i in number_str:
#     if i.isdigit():
#         digits_sum += int(i)
        
# print("sum of digits:",digits_sum)


    
# # ********************* 5th answer:------------------------------------------------
# def generate_series(n):
#     series=[] 
#     term = 1
#     for i in range(n):
#         series.append(term)
#         term*=3
#     return series
# n = 6 
# result = generate_series(n)
# print(result)
          
    
    
    
#     #WASTE============================================ 
    
# # a={"name":"kriss","age":20,"phone_Number":9805158520,"car":"BMW"}
# # CONVERT INTO DICTIONARY
# # lst =["name","age","car"]
# # lst1=["kriss",20,"BMW"]
# # a=lst+lst1
# # dict=lst+lst1
# # dict=a
# # print(a)


# # a=[2,4,6,8,10]
# # # [expression itreater condation]

# # [i  for i in a if a==2 and a!=8 ]
# # # print a if a==2 but not print a==4
# # # if a==6 but not print a==8
# # replace
# # print(a)


# # ===========================================================================================================================





# # **********1st question___________________________________________________________________

# c = [20,90,100,55,80,200,5000,100,101,400,502,79]
# a = c[1]
# b = c[1]
# for i in c:
#     if a>i:
#         a=i
#     if b<i:
#         b=i
# print(a)
# print(b)
    
# *8888888888888888888888    if i<large_number
     
#     large_number=num
#     print("the largest number of the list:",a[largest_number])
# # #     elif num<=smallest_number
# # #     smallest_number=num
#     print("the smallest number of the list:",a[smallest_number])
#     # num>=smallest_number
#         # print("the smallest number of the list:",a[smallest_number])
        
        
        
# #****************2nd question======================================



# #4rth_======___======__======___======___======____=====_____________________________________________________

# a=10
# b=True+True
# print(a*10+a-b)




# # #5th =========================================rrr 
def has_unique_chars(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return False
        char_set.add(char)
        return True
        
        
A = ["Hello","Missisipi","Car","Airoplan","Bike","Verygood"]
for string in A:
    is_unique = True
    for i in range(len(string)):
        if string[i] in string[i*1:]:
            is_unique = False
            break
    if is_uniquea and len(string)>len(longet_unique_str):
        longest_unique_str = string
print(longest_unique_str) 
        
# longest_unique_str = ""
# for string in A:
#     if has_unique_chars(string) and len(string) > len(longest_unique_str):
#         longest_unique_str = string
# print(longest_unique_str)