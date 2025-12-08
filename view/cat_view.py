import questionary
from rich.table import Table
from rich.console import Console
from models.cat import Cat 

console = Console()

def display_all_cats(cats_data: object):
            
    table = Table(title="=== 🐱 ALL CATS ===")
    
    table.add_column("No.", style="cyan", justify="center")
    table.add_column("ID", style="dim")
    table.add_column("Name", style="bold magenta")
    table.add_column("Breed", style="green")
    table.add_column("Weight (Kg)", style="yellow")
    
    for i, cat in enumerate(cats_data, start=1):
        table.add_row(f"{i}", f"{cat.id}", f"{cat.name}", f"{cat.breed}", f"{cat.weight_kg}")

    console.print(table)
    input("\nPress [Enter] to back...")  

def add_new_cat_display():
    while True:
        console.rule("[bold cyan]➕ ADD NEW CAT[/]")
        
        name = questionary.text("🐱 Cat Name:").ask()
        if not name: return 
        
        breed = questionary.text("🧬 Breed/Type:").ask()
        
        while True:
            try:
                weight_input = questionary.text("⚖️  Weight (Kg):").ask()
                weight = float(weight_input)
                break
            except ValueError:
                console.print("[bold red]❌ Error:[/] Weight must be a number (Ex: 4.5)")

        table = Table(title="📝 DRAFT PREVIEW")
        table.add_column("Name", style="magenta")
        table.add_column("Breed", style="green")
        table.add_column("Weight", style="yellow")
        
        table.add_row(name, breed, f"{weight} kg")
        
        console.print(table)
        
        confirm = questionary.confirm("Is this data correct? (Save)").ask()
        
        if confirm:
            new_cat = Cat(name=name, breed=breed, weight_kg=weight)
            new_cat.save()
            display_cat_form_success(name)
            break 
        else:
            retry = questionary.confirm("Do you want to retry input?").ask()
            if not retry:
                console.print("[yellow]❌ Cancelled.[/]")
                break

def display_cat_form_success(cat_name: str):
    console.print(f"\n[bold green]✅ SUCCESS![/] Kucing [cyan]{cat_name}[/] berhasil didaftarkan! 😺🎉")
    input("Tekan [Enter] untuk lanjut...")