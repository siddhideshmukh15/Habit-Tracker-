habits=[]
while True:
    print("\n1. Add habit \n2.view habits\n 3.complete habit \n 4.Delete habit \n5.exit")
    choice=input("Enter choice:")

    if choice=="1":
        name=input("Enter habit:")
        habits.append({"name":name,"done":False})
        print("Habit added!")
    elif choice=="2":
        for i,h in enumerate(habits,1):
            print(i,h["name"],"-","Done" if h["done"] else "pending")
            if not habits:
                print("No habits found!")

    elif choice=="3":
        try:
            n=int(input("Habit number:"))

            if 1<=n<=len(habits):
                habits[n-1]["done"]=True
                print("Habit completed")
            else:
                print(" Invalid number!")
        except ValueError:
            print("Invalid number!")

    elif choice=="4":
        try:
            n-int(input("Habit number"))
            if 1<=n<= len(habits):
                habits.pop(n-1)
                print("Habit deleted!")
            else:
                print("Invalid number!")
        except ValueError:
            print("Enter a valid number!")

    elif choice=="5":
        print("Thank you for using!")
        break
else:
    print("Invalid choice!")
    

