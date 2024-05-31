while True:
        sq = input("press q for quit and s for start : ")
    
        if sq == "q":
            break
        elif sq == "s":
            print("**********calculator************")
        
            num1 = int(input(" enter the first num:"))
        num2 = int(input("enter the second num:"))
        
        print("""
              select one of them....
              1.addition
              2.subtraction
              3.multiplication
              4.division
            """) 
        choice = input("enter what you want to do : ")
        if choice =="1":
            print("the add is : ", num1 +num2)
        elif choice == "2" :
            print("the sub is : ", num1-num2)
        elif choice == "3" :
            print("the mul is : " ,num1*num2)
        elif choice == "4" :
            print("the div is: ", num1/num2)
            
        else:
            print("enter something valid ")
    
            print("enter valid word......")
             
             
            