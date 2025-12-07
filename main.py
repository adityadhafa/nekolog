from models.cat import Cat
from models.expense import Expense

from rich.console import Console
from rich.table import Table

def main():
    want = ""
    while(want != "0"):
        print("=== 🐱 NEKOLOG 🐱 ===")
        print("1. Print All Cats")
        print("2. Catat Pengeluaran")
        print("3. Liat Leaderboard Sultan")
        print("0. Keluar")
        want = input("Select menu: ")
        
        if(want == "1"):
            res = Cat.get_all()
            
            table = Table(title="All Cats")
            
            table.add_column("No.", style="cyan")
            table.add_column("Id", style="cyan")
            table.add_column("Name", style="magenta")
            table.add_column("Breed", style="magenta")
            table.add_column("Weight (Kg)", style="magenta")
            
            for i, cat in enumerate(res, start=1):
                table.add_row(f"{i}", f"{cat.id}", f"{cat.name}", f"{cat.breed}", f"{cat.weight_kg}")
            
            console = Console()
            console.print(table)
            
        elif(want == "2"):
            amount = int(input("amount: "))
            
            name = input("name: ")
            res = Cat.search_cat(name=name)
            for i, cat in enumerate(res, start=1):
                print(f"{i}. id= {cat[0]}, name= {cat[1]}")
            
            if res != []:
                cat_id = int(input("input cat id: "))
            else:
                print("salah nama kali")
                continue
            
            category = input("input category: ")
            date =  input("input date (YY-MM-DD): ")
            description = input("desc: ")
            
            new_expenses = Expense(amount=amount, category=category, date=date, description=description, cat_id=cat_id)
            
            new_expenses.save()
            
            print("expenses saved!")
            
        elif(want == "3"):
            res = Expense.get_leaderboard()
    
if __name__ == "__main__":
    main()
    