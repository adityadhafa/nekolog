from models.cat import Cat
from models.expense import Expense

from rich.console import Console
from rich.table import Table

def main():
    want = ""
    while(want != "0"):
        table = Table(title="=== 🐱 NEKOLOG 🐱 ===")
        table.add_column("No.",)
        table.add_column("Menu",)
        
        table.add_row("1.", "Add a Cat")
        table.add_row("2.", "Print All Cats")
        table.add_row("3.", "Add Expenses")
        table.add_row("4.", "Expenses Leaderboard")
        table.add_row("0.", "Exit")
        
        console = Console()
        console.print(table)
        want = input("Select menu (No.): ")
        
        if(want == "2"):
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
            
        elif(want == "3"):
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
            date =  input("input date (YYYY-MM-DD): ")
            description = input("desc: ")
            
            new_expenses = Expense(amount=amount, category=category, date=date, description=description, cat_id=cat_id)
            
            new_expenses.save()
            
            print("expenses saved!")
            
        elif(want == "4"):
            res = Expense.get_leaderboard()
            
            table = Table(title="🏆 EXPENSES LEADERBOARD 🏆")
            
            table.add_column("No.", style="cyan")
            table.add_column("Name", style="magenta")
            table.add_column("Total Expenses", style="magenta")
            
            for i, cat in enumerate(res, start=1):
                table.add_row(f"{i}", f"{cat[0]}", f"{cat[1]}")
            
            console = Console()
            console.print(table)
            
        elif(want == "1"):
            name = input("name: ")
            breed = input("breed: ")
            weight = float(input("weight: "))
            
            new_cat = Cat(name=name, breed=breed, weight_kg=weight)
            new_cat.save()
            
            print("cat saved!")
    
if __name__ == "__main__":
    main()
    