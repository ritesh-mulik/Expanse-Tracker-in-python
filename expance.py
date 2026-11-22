import json
import os 
from datetime import datetime

FILE_NAME = "expenses.json"

def lod_expenses():              #ek function define kiya
    if not os.path.exists(FILE_NAME):     #cheak ki file mojud hain ya nahi ; file ke undar kuch ho ya na ho ye nahi dekhta ; if file exist tho True hoga and tab kahi list return hogi but hum empty list tab return karana chahte hain tab jab file exist na ho therefore not lagaya thaki False wali condition True ho and file exist na hone par hame ek empty list return ho   
        return[] #and agar empty list return hogi tab ye function yahi end ho jaega ; with open wala nahi chalega
    with open(FILE_NAME,"r") as f : # jab if wala skip hoga tab tab with open chalega abd data padhkar return hoga
        return json.load(f) # .lode json module ka ek function hain jo f se text read karata hain and python list banata hain  

def save_expenses(expenses): #lod_exp file se data read karta tha but ye data ko file main likh ta hai 
    with open(FILE_NAME,"w") as f:
        json.dump(expenses,f,indent=4) #.dump python list/dict ko JSON Text main badal kr f main likh deta hain


def add_expenses(expenses):
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
    save_expenses(expenses) # ye puri list ko expenses.json  file main likh deta hain tab jab data peremanent hota hain
    print("Expense add ho gaya !")


def view_expenses(expenses):#kaam hain expenses ko saji hui table ke jase screen par dikhana 
    if not expenses: # if condition agar True tabhi print hoaga , so agar list khai hain tab False there fore not False = True and then print hoga
        print("abhi koi expence nahi hain.")
        return #agar list khali tho message print hoga and then function end other wise if skip hoga and aage table banegi

    print(f"{'ID':<4}{'Date':<12}{'Category':<10}{'Amount':>9} Note")
    print("-" * 50)
    for e in expenses:
        print(f"{e['id']:<4}{e['date']:<12}{e['category']:<10}{e['amount']:>9.2f} {e['note']}")


def delete_expenses(expenses):
    try:
        del_id = int(input("Delete karne walla ID : "))
    except ValueError:
        print("Galat ID !")
        return
    for e in expenses:
        if e["id"]==del_id:
            expenses.remove(e) #wo expense list d=se hata diya
            save_expenses(expenses) #update list file main likh di, tab permanent hua
            print("Expense delete ho gaya")
            return
    print("ye ID mili nahi") #ye loop ke bahar hain , ye tahbi chal ta hain jab loop pura ghum gaya aur kahi return nahi chala, yani koi expence match hua hi nahi
#Correct ID mili ->remove->save->print->return
#NO ID found ->loop pura ghuma ->"ye ID mili nahi"


def show_summary(expenses):
    if not expenses:
        print("Summary ke liya koi data nahi hain.")
        return
    total = sum (e["amount"] for e in expenses)
    by_category = {}
    for e in expenses:
        cat = e["category"]
        by_category[cat] = by_category.get(cat,0) + e["amount"]
    print(f"\nTotal kharcha: Rs {total:.2f}")
    print("Category-wise:")
    for cat, amt in sorted(by_category.items(), key=lambda x: x[1], reverse=True):
        percent = amt / total * 100   
        print(f" {cat:<10} Rs {amt:>8.2f} ({percent:.1f}%)")
        
        
def main():
   expenses = lod_expenses()
   while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Delete expense")
        print("4. Summary")
        print("5. Exit")
        choice = input("Choice (1-5): ").strip()
        
        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expenses(expenses)
        elif choice == "4":
            show_summary(expenses)
        elif choice == "5":
            print("Bye! Paisa sambhal ke kharch karo.")
            break
        else:
            print("Galat choice, 1 se 5 ke beech daalo.")


if __name__ == "__main__":
    main()
