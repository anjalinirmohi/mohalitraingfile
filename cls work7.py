# # polymorphism:
# # poly:-many
# # morphism:-forms


# # types of polymorphism:-
# # method overloading
# # ...... overloading




# class cls1:

#     def mthd1(self,a,b,c):
#         d=a+b+c
#         print(d)
        
#         # if (a!=none and b!=none and c!=None)
    
#     def mthd2(self,a,b):
#         c=a+b
#         print(c)
        
#     def mthd3(self,a):
#         print(a)  
        
          
#     # obj=cls1
#     # obj.mth
#     # print(40)
#     #  def methd2(self):
#     # #     print("mma")#
    
#     # # def mthd3(self):
#     # #     print("anjali")
        
# obj=cls1
# obj.mthd3
# print(10)


# method overridding:-
# age=20
# age=200

# print(age)

# class cls1:
#     def anjali(self):
#         print("i am anjali 1")
        
#     def ashish(self):
#         print("i am ashish")
        
# class cls2(cls1):
#     def oppo(self):
#         print("i am a brand")
    
#     def anjali(self):
#         print("i am anjali 2")
        
# obj=cls2
# obj.anjali

# print(cls2)
        






# PolyMorphism : 
    
#     poly :  many
    
#     morphism : forms


# 1) Compile time polymorphism
#     operator overloading
#     method overloading

# 2) Run time polymorphism
#     method overriding
#     interfaces

# duck typing 


# operator overloading :

class cls1:
    def sumthis(self, a, b, c):
        d = a + b + c
        print(d)
    
    def sumthis(self, a, b):
        c = a + b
        print(c)
    
    def sumthis(self, a):
        c = a
        print(c)

obj = cls1()
obj.sumthis(12)


        
    
class cls1:
    def sumthis(self, a = None, b = None, c = None):
        if a != None and b != None and c != None:
            zx = a + b + c
            print(zx)
        
        elif a != None and b != None:
            zx = a + b
            print(zx)
        
        elif a != None:
            zx = a
            print(zx)
        
        else:
            print("Enter something..")
    
obj = cls1()
obj.sumthis(12, 100, 1)
   
   
# method overrriding : 

# age = 18


# age = 90


# print(age)

# class cls1:
#     def showme(self):
#         print("i am from class 1")
    
#     def ok(self):
#         print("i am ok//....")

# class cls2(cls1):
#     def no(self):
#         print("noooooooooo")
    
#     def showme(self):
#         print("i am from class 2...")
    
# obj = cls2()   

# obj.showme()





      
        
        
        
        

