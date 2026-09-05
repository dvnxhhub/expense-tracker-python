def get_app_name():
    return "Expense Tracker"


if __name__ == "__main__":
    print(get_app_name())
    expenses = []

expense = {
    "amount": 250.0,
    "category": "Food",
    "description": "Lunch"
}
expenses.append(expense)



expense={
        "amount":100.0,
        "category":"travel",
        "description":"Bus fair"
    }
expenses.append(expense) 
while True:
    try:
        amount=float(input("enter the  amount: "))
        if amount <=0:
            print("the  number  must  be  positive")
            continue
        break
    except ValueError:
      print("Invalid amount. Please enter a number.")
    
category=input("enter  the category: ")

description=input("enter the description: ")
expense = {
    "amount": amount,
    "category": category,
    "description": description
}
expenses.append(expense)
print(expenses)
total  =  0
for expense in expenses:
    total=total+expense["amount"]
    
    
print(" total amount  is: ",total)   
    


