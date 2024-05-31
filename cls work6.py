# properties of encapsulation:
# getter
# setter
# deleter
    # use of getter

# def abc(self,a,b):
#     self.name=a
#     self.age=b
    

# def __init__(self, a, b):
#     self.__name = a
#     self.age = b
#     @property
#     def deleter (self)




# Encapsulation : 


# class cls1:
#     def __init__(self, x, y):
#         self.a = x
#         self.b = y

#     def __mthd1(self):
#         print("ok")
    
#     def methd2(self):
#         print("car")
    
#     def mthd3(self):
#         print("arioplain")
        
# class cls2(cls1):
#     def xyz(self):
#         print(self.a)


# obj = cls2(10, 20)

# obj.xyz()
# public 
# private 
# protected


# property
# getter          it is used to get the data
# setter           set nd update
# deleter          delete

# abc = map(function, itterater)

class cls1:
    def __init__(self, x, y):
        self.name = x
        self.age = y
    
    def xyz_name(self):
        return self.name
    
    def setter_x(self, new_age): #setter is use to update nd set the data
        self.age = new_age
        
    def delter(self):
        del self.age
    
    def __str__(self):
        return f"username is {self.name} and age is {self.age}"


obj = cls1("sunita", 20)
print(obj.xyz_name())
obj.setter_x(21)
# obj.delter()                  #it is use to delete the data or change the data
print(obj)

class cls1:
    def __init__(self, x, y):
        self.name = x
        self.age = y
    
    def age(self):
        return self.age
    
    def __str__(self):
        return f"username is {self.name} and age is {self.age}"
       
       
       
obj = cls1("anjali nirmohi", 21)


print(obj)


class cls1:
    def __init__(self, x, y):
        self.name = x
        self._age = y
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self._age = new_age 
        else:
            return "please enter valid age..."
    
    def __str__(self):
        return f"username is {self.name} and age is {self._age}"
       
obj = cls1("dixit", 22)

obj.age = 25

print(obj)




#mangling concept


