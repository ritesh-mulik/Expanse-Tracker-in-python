import json
import os 
from datetime import datetime

FILE_NAME = "expenses.json"

def lod_exp():              #ek function define kiya
    if not os.path.exists(FILE_NAME):     #cheak ki file mojud hain ya nahi ; file ke undar kuch ho ya na ho ye nahi dekhta ; if file exist tho True hoga and tab kahi list return hogi but hum empty list tab return karana chahte hain tab jab file exist na ho therefore not lagaya thaki False wali condition True ho and file exist na hone par hame ek empty list return ho   
        return[] #and agar empty list return hogi tab ye function yahi end ho jaega ; with open wala nahi chalega
    with open(FILE_NAME,"r") as f : # jab if wala skip hoga tab tab with open chalega abd data padhkar return hoga
        return json.load(f) # .lode json module ka ek function hain jo f se text read karata hain and python list banata hain  

def save_exp(expenses): #lod_exp file se data read karta tha but ye data ko file main likh ta hai 
    with open(FILE_NAME,"w") as f:
        json.dump(expenses,f,indent=4) #.dump python list/dict ko JSON Text main badal kr f main likh deta hain


def add_exp(expenses):
    try: 
        amount = float(input("Amount (Rs): "))
    except ValueError: #except ke baad python main ane wale aasli erro ka naam likhan padata hain and agar error ka namm nahi pata tho only try walla part run karo wrong input se the except main likho basically pahale galti karo and then erro ka namm pata kro
        print("Wrong Amount !! Only enter number.")
        return #ye return : ab gadbad ho gai ab niche ka code mat chalao
    
    category = input("Category(food/travel/rent/other): ").strip().lower() #.strip() and .lower() ye string ko saff karne walle methodes hain .strip() string ke faltu spacese ko hathata hain " food " --> "food" beach ka space nahi hatata "best food" and .lower() "FOOD"-->"food" ,"Food"-->"food"
    note = input("Note (optional): ").strip()

new_id = max([e["id"] for e in expenses], default =0) + 1
expense = {
    "id": new_id,
    "date": datetime.now().strftime("%y-%m-%d"),
    "amount":amount,
    "category": category,
    "note": note,
}

expenses.append(expense)
save_exp(expenses)
print("Expense add ho gaya !")
