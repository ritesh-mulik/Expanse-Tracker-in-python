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

ids = [e["id"] for e in expenses] #sare purane expenses main se only uunki id's nikal kr ek list banai like [1,2,3]
biggest = max(ids, default =0) #uss list mese sabase badi id nikali ,yaha 3 hain
new_id = biggest + 1 # uss main ek jodkar new id banai 4 
#overall purane number dekho, unnme bada find karo, uss se agala number naye expense ko dedo
expense = {  
    "id": new_id,                                    #then naye expense ka dictionary banay  (id=4,date,amount,catagory,note)                                                       
    "date": datetime.now().strftime("%y-%m-%d"),  
    "amount":amount,
    "category": category,
    "note": note,
}

expenses.append(expense) #naya ban hua dictionary(expense) badi list (expenses) ke end main jod deta hain
save_exp(expenses) # ye puri list ko expenses.json  file main likh deta hain tab jab data peremanent hota hain
print("Expense add ho gaya !")


def view_expenses(expenses):#kaam hain expenses ko saji hui table ke jase screen par dikhana 
    if not expenses: # if condition agar True tabhi print hoaga , so agar list khai hain tab False there fore not False = True and then print hoga
        print("abhi koi expence nahi hain.")
        return #agar list khali tho message print hoga and then function end other wise if skip hoga and aage table banegi

        print(f"{'ID:<4'}{'Date':<12}{'category':<10}{'amount':>9} Note")
        print("-" * 50)
        for e in expenses:
            print(f"{e['id']:<4}{e['date']:<12}{e['category']:<10}{e['amount']:>9.2f} {e['note']}")