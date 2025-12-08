import questionary
from questionary import Choice
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


def update_cat_data_display():
    console.rule("[bold orange1]✏️ UPDATE CAT DATA[/]")
    
    search_name = questionary.text("🔍 Search Cat Name:").ask()
    if not search_name: return 

    results = Cat.search_cat(search_name)
    
    if not results:
        console.print("[bold red]❌ No cat found![/] Try other name.", style="red")
        input("Press Enter to return...")
        return

    cat_choices = []
    for cat in results:
        cat_choices.append(Choice(title=f"🐱 {cat.name} (ID: {cat.id})", value=cat.id))
    
    cat_choices.append(Choice(title="❌ Cancel", value="cancel"))

    selected_cat_id = questionary.select(
        "Select the cat to edit:",
        choices=cat_choices
    ).ask()
    
    if selected_cat_id == "cancel": return
    
    current_cat = Cat.get_by_id(selected_cat_id)
    
    if not current_cat:
        console.print("[red]Error: Data kucing tidak ditemukan di DB.[/]")
        return

    console.print(f"\n[dim]Editing data for: [bold cyan]{current_cat.name}[/][/dim]")
    console.print("[dim] Press [Enter] jika tidak ingin mengubah data.[/dim]\n")

    new_name = questionary.text("🐱 Name:", default=current_cat.name).ask()
    new_breed = questionary.text("🧬 Breed:", default=current_cat.breed).ask()
    
    while True:
        try:
            weight_input = questionary.text("⚖️  Weight (Kg):", default=str(current_cat.weight_kg)).ask()
            new_weight = float(weight_input)
            break
        except ValueError:
            console.print("[bold red]❌ Error:[/] Weight must be a number!")

    table = Table(title="📝 UPDATE PREVIEW")
    table.add_column("Field", style="cyan")
    table.add_column("Old Value", style="dim")
    table.add_column("New Value", style="bold green")
    
    table.add_row("Name", current_cat.name, new_name)
    table.add_row("Breed", current_cat.breed, new_breed)
    table.add_row("Weight", f"{current_cat.weight_kg} kg", f"{new_weight} kg")
    
    console.print(table)
    
    confirm = questionary.confirm("Save changes?").ask()
    
    if confirm:
        current_cat.update(name=new_name, breed=new_breed, weight_kg=new_weight)
        
        console.print(f"\n[bold green]✅ UPDATED![/] Data {new_name} berhasil diperbarui! 😺")
        input("Press Enter to return...")
    else:
        console.print("[yellow]❌ Cancelled.[/]")
        
def delete_cat_display():
    console.rule("[bold red]🗑️  DELETE CAT[/]")

    search_name = questionary.text("🔍 Search Cat Name to Delete:").ask()
    if not search_name: return 

    results = Cat.search_cat(search_name)
    
    if not results:
        console.print("[bold red]❌ No cat found![/] Try other name.", style="red")
        input("Press Enter to return...")
        return

    cat_choices = []
    for cat in results:
        cat_choices.append(Choice(title=f"🐱 {cat.name} (ID: {cat.id})", value=cat.id))
    
    cat_choices.append(Choice(title="❌ Cancel", value="cancel"))

    selected_cat_id = questionary.select(
        "Select the cat to DELETE:",
        choices=cat_choices
    ).ask()
    
    if selected_cat_id == "cancel": return

    target_cat = Cat.get_by_id(selected_cat_id)
    
    if not target_cat:
        console.print("[red]Error: Data kucing tidak ditemukan.[/]")
        return

    console.print(f"\n[bold white on red] ⚠️  WARNING! ⚠️ [/]")
    console.print(f"You are about to delete [bold cyan]{target_cat.name}[/] permanently.")
    console.print("This action cannot be undone.\n")
    
    confirm = questionary.confirm(
        f"Are you 100% sure you want to delete {target_cat.name}?",
        default=False 
    ).ask()
    
    if confirm:
        target_cat.delete()
        console.print(f"\n[bold green]✅ DELETED![/] Data [strike]{target_cat.name}[/] telah dihapus dari muka bumi NekoLog. 👋")
        input("Press Enter to return...")
    else:
        console.print("[yellow]❌ Cancelled. The cat is safe![/]")

def search_cat_display():
    console.rule("[bold cyan]🔍 SEARCH CAT[/]")

    keyword = questionary.text("Enter cat name to search:").ask()
    if not keyword: return # Return if empty
    
    results = Cat.search_cat(keyword)

    if results:
        console.print(f"\n[italic green]Found {len(results)} cats matching '{keyword}':[/]")

        display_all_cats(results) 
        
    else:
        console.print(f"\n[bold red]❌ NO RESULTS![/] No cats found matching [bold white]'{keyword}'[/].")
        input("Press [Enter] to return...")