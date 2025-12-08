import questionary
from questionary import Choice
from rich.console import Console
from rich.table import Table

console = Console()

def display_main_menu():
    # 1. DISPLAY TABLE (Header/Info)
    table = Table(title="=== 🐱 NEKOLOG DASHBOARD 🐱 ===")
    table.add_column("Module", style="bold cyan", justify="center")
    table.add_column("Description", style="magenta")
    
    table.add_row("🐱 Cats", "Manage Cat Profiles")
    table.add_row("💰 Finances", "Track Expenses & Leaderboard")
    table.add_row("❌ Exit", "Close Application")
    
    console.print(table) 
    print("") 
    
    # 2. DISPLAY MENU SELECTION (Input)
    answer = questionary.select(
        "Where would you like to go?",
        choices=[
            Choice(title="1. Cats Menu (Manage Profiles)", value="1"),
            Choice(title="2. Finance Menu (Manage Expenses)", value="2"),
            Choice(title="0. Exit", value="0"),
        ]
    ).ask()
    
    return answer

def display_cat_submenu():
    # Submenu Header
    console.rule("[bold cyan]🐱 CAT MANAGEMENT[/]") 
    
    answer = questionary.select(
        "Select Operation:",
        choices=[
            Choice(title="➕ Add New Cat", value="1"),
            Choice(title="👀 View All Cats", value="2"),
            Choice(title="🔍 Search Cat", value="3"),
            Choice(title="✏️  Update Cat Data", value="4"),
            Choice(title="🗑️  Delete Cat", value="5"),
            Choice(title="🔙 Back to Main Menu", value="0"),
        ]
    ).ask()
    
    return answer

def display_expense_submenu():
    console.rule("[bold green]💰 FINANCE MANAGEMENT[/]")
    
    answer = questionary.select(
        "Select Operation:",
        choices=[
            Choice(title="💸 Record New Expense", value="1"),
            Choice(title="🏆 View Expenses Leaderboard", value="2"),
            Choice(title="🔙 Back to Main Menu", value="0"),
        ]
    ).ask()
    
    return answer