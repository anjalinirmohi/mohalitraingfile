# def xyz(n):
#     for i in range(n):
#         yield i
# pq = xyz(6)
# print(next(pq))
# print(next(pq))
# print(next(pq))
# print(next(pq))
# print(next(pq))
# print(next(pq))
# print(next(pq))
# print(next(pq))




# def anjali(n):
#     for i in range(n):
#         yield i 
# tr = anjali(4)
# print(next(tr))
# print(next(tr))
# print(next(tr))
# print(next(tr))



class MyIterators:
    # def __init__(self,start,end):
    #     self.start=start
    #     self.end=end
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <=10:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass = MyIterators()
myiter = iter(myclass)
for x in myiter:
    print(x)
    
    
