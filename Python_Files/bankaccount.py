Balance=1000
while True:
    print("\n====Bank Manu====")
    print("1.check Balance")
    print("2.deposit Money")
    print("3.withdraw Money")
    print("4. Exit")
    choice=int(input("enter your choice :"))
    if choice ==1:
        print('your balance is',Balance)
    elif choice==2:
        amount=float(input('enter your deposit amount :'))
        Balance+=amount
        print("deposit successful")
    elif choice==3:
     amount=float(input('enter your withdraw amount :'))
     if amount > Balance:
        print("Insufficient Balance!")
     else:
        Balance-=amount 
        print('withdraw successful')
     
    elif choice==4:
        print('Thank you for using bank system')
    elif choice >4:
        print('invailed choice')
    else:
        print('balance not avalible')
    

        
               
        


     
  

        

    
        
        
    
        
        
    