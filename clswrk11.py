
# {key expresion : value expression itreater condation }
#  a = {i * 2 : i  + 10  for i in range(1, 5)}

# [expression itreater condation]
# question one :


a = ["name","age","number"]
b = ("moris",20,9805158520)

xy={a[i]:b[i] for i in range(3)}
print(xy)


# question 2:
a = "i am a python developer,who are you"
b = ["a","e","i","o","u"]
cd=[i for i in a if i not in b  ]
print(cd)  



# question 3:
a = ("age","place")
b=["21","chandigarh"]
fg={a[i]:b[i] for i in range(2)}
print(fg)



# question 4:
x="i am fantastic"
y=["a","t"]
tb=[i for i in x if i not in y]
print(tb)






