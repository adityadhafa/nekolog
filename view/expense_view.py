import questionary
from questionary import Choice
from rich.console import Console
from rich.table import Table
from models.cat import Cat
from models.expense import Expense

console = Console()

def add_expense_display():
    console.rule("[bold green]💸 RECORD NEW EXPENSE[/]")


    search_name = questionary.text("🔍 Search Cat Name:").ask()
    if not search_name: return 

    results = Cat.search_cat(search_name)
    
    if not results:
        console.print("[bold red]❌ No cat found![/] Coba nama lain.", style="red")
        input("Press Enter to return...")
        return

    cat_choices = []
    for row in results:
        cat_choices.append(Choice(title=f"🐱 {row[1]} (ID: {row[0]})", value=row[0]))
    
    cat_choices.append(Choice(title="❌ Cancel", value="cancel"))

    selected_cat_id = questionary.select(
        "Select the cat:",
        choices=cat_choices
    ).ask()
    
    if selected_cat_id == "cancel": return


    while True:
        try:
            amount_input = questionary.text("💰 Amount (Rp):").ask()
            amount = int(amount_input)
            break
        except ValueError:
            console.print("[red]❌ Error:[/] Harus angka, Bro!")

    category = questionary.select(
        "📂 Category:",
        choices=["Food", "Medical/Vet", "Toys", "Grooming", "Other"]
    ).ask()
    
    description = questionary.text("📝 Description:").ask()
    
    import datetime
    today = datetime.date.today().strftime("%Y-%m-%d")
    date = questionary.text(f"📅 Date (YYYY-MM-DD):", default=today).ask()


    table = Table(title="🧾 EXPENSE DRAFT")
    table.add_column("Item", style="cyan")
    table.add_column("Value", style="yellow")
    
    table.add_row("Cat ID", str(selected_cat_id))
    table.add_row("Amount", f"Rp {amount:,}")
    table.add_row("Category", category)
    table.add_row("Date", date)
    table.add_row("Desc", description)
    
    console.print(table)
    
    confirm = questionary.confirm("Save this expense?").ask()
    
    if confirm:
        new_expense = Expense(amount=amount, category=category, date=date, description=description, cat_id=selected_cat_id)
        new_expense.save()
        console.print("\n[bold green]✅ SAVED![/] Uang melayang, Kucing senang! 💸😺")
        input("Press Enter to continue...")
    else:
        console.print("[yellow]❌ Cancelled.[/]")