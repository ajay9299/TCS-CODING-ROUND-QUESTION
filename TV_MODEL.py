
# TCS EXAM QUESTION--------->
import numpy as np
Tv_Brand_Model_Price = [10000,7000,6000]
User_Choise = int(input("Enter Tv Number"))
# Conditions 
if User_Choise<=2:
    print(Tv_Brand_Name[User_Choise])
    Offer = int(input("Do you want offer")) # yes = 1, No = 2
    if Offer>=3:
        print("Invalid entery")
    elif Offer==1:
        Tv_Condition = int(input("Tv is working or not")) # put 1 for good conditon and 0 for bad conditon
        if Tv_Condition==1:
            discount_1 = 0.2
            lapse = Tv_Brand_Name[User_Choise]*discount_1
            Finall_Price = Tv_Brand_Name[User_Choise]-lapse
            print("Welcome your Tv Price is = ",Finall_Price)         
        elif Tv_Condition==2:
            discount_2 = 0.02
            lapse = Tv_Brand_Name[User_Choise]*discount_2
            Finall_Price = Tv_Brand_Name[User_Choise]-lapse
            print("Welcome your Tv Price is = ",Finall_Price) 
        elif Tv_Condition==0:
            print("Invalid Entry")           
        elif Tv_Condition>=3:
            print("Invalid Entry")           
    elif Offer==2:
            print("Welcome your Tv Price is = ",Tv_Brand_Name[User_Choise])  
else:
   print("Invalid Entry ")  