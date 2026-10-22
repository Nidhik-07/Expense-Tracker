Expenseprint ("Welcome to the Expense Tracker")
total=0
elst=[]
while True:
    print("\n⭐️ Menu ⭐️\n 1. Add Expense \n 2. View All Expenses \n 3. View Total Spending \n 4. Exit")
    choice=int(input("Enter your Choice: "))
    if choice==1:
        date=input("Enter date of spend : ")
        category=input("Enter category of spend (Food, Travel, Shopping, Bill, Outings etc): ")
        amount=float(input("Enter amount of spent: "))
        edict={"Date":date,"Category":category,"Amount":amount}
        elst.append(edict)
        total=total+edict["Amount"]
        print("\nExpense Added")
    elif choice==2:
        if len(elst)==0:
            print("\n No Expenses")
        else: 
            c=1
            for i in elst:
                print(f"\nYour Expenses {c} is: {i}")
                c+=1
    elif choice==3:
        if total==0:
            print("No Spending")
        else:
            print("\nYour Total Spending is: ",total)
    elif choice==4:
        print("\nThankyou for using Expense Tracker")
        break
    else:
        print("Invalid Choice")
        break
