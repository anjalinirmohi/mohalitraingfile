import threading

class distribution:
    def mma(self):
        for i in range(20):
            print("yesssss")
        
    def mom(self):
        for i in range(20):
            print("nooooooooooo")

obj = distribution()

thread1 = threading.Thread(target = obj.mma)
thread2 = threading.Thread(target = obj.mom)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("i am  runnninggg...")

print("new process")

print("this is importnt code")


print("done.")





















