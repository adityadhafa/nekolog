from rich.table import Table
from rich.console import Console

console = Console()

def display_main_menu():
    table = Table(title="=== 🐱 NEKOLOG 🐱 ===")
    table.add_column("No.", style="cyan")
    table.add_column("Menu", style="bold white")
    
    table.add_row("1", "About Cat (Menu Kucing)")
    table.add_row("2", "About Expenses (Menu Keuangan)")
    table.add_row("0", "Exit")
    
    console.print(table)
    return input("Select menu (No.): ")

def display_cat_submenu():
    table = Table(title="=== CATS MENU ===")
    table.add_column("No.", style="cyan")
    table.add_column("Menu", style="magenta")
    
    table.add_row("1.", "Add a Cat")
    table.add_row("2.", "Show All Cats")
    table.add_row("3.", "Search Cat")       
    table.add_row("4.", "Update Cat Data")
    table.add_row("5.", "Delete a Cat")
    table.add_row("0.", "Back")
    
    console.print(table)           
    return input("Select (No.): ") 

def display_expense_submenu():
    table = Table(title="=== EXPENSE MENU ===") 
    table.add_column("No.", style="cyan")
    table.add_column("Menu", style="green")
    
    table.add_row("1.", "Add Expense")          
    table.add_row("2.", "Leaderboard Sultan")
    table.add_row("0.", "Back")
    
    console.print(table)           
    return input("Select (No.): ") 