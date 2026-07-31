"""
Sample output ;;;
Welcome to Expense Tracker 

=========Menu=========
1. Add Expense 
2. View All Expenses
3. View Total Spending
4.Exit
=======================

Enter your Choice (1-4):
 3
 Total spending 

"""
expenses = [] #list of expenses int form of dictionary

print("Welcome to Expense Tracker")

while True:
    print("=========Menu=========")
    print("1. Add Expense ")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4.Exit")
    choice = int(input("Please Enter your choice : "))

    # Add Expense 
    if(choice==1):
        date = input("Date of the Spend money :  ")
        category = input("Type of Expense : " )
        description = input("more detail  : ")
        amount =int(input("Enter the spend money : "))


        expense = {
        "date":date,
         "category":category,
         "description":description,
         "amount":amount
        }
        expenses.append(expense)
        print("expenses added successfully")
#  2 . view all Expenses


    if(choice==2):
        if(len(expenses)==0):
            print("no expenses added ")
        else:
            print(" ======= Here is your All Expenses ")
            count= 1
            for expen in expenses:
                print(f"Item no . {count} -> Date : {expen["date"]}, Category : {expen["category"]} ,{expen["description"]},  amount of Expenses = ${expen["amount"]} ")
                count= count+1

# 3. view total spending 
 
    elif(choice==3):
        total = 0
        for eachspend in expenses :
           total = total +eachspend["amount"]

        print("Total spending expenses : " , total)      

 # 4 . Exit 

    elif(choice==4):
        print("Successfully completed") 
        break 
    else:
        print("Invalid Choice")