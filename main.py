def get_app_name():
    return "Expense Tracker"

def get_valid_amount():
     while True:
        
         try:
             amount=float(input("enter the amount: "))
             if amount <= 0:
                 print("entered  number  must be  positve")
                 continue
             return amount
         except ValueError:
             print("invalid value")

def get_valid_text(field_name):
     while True:
        value=input(f"enter the field name {field_name}: ").strip()
        if value =="":
            print(f"{field_name.capitalize()} cannot be empty")
            continue
        return value





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
amount=get_valid_amount()
category=get_valid_text("category")
description=get_valid_text("descrption")


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
            


