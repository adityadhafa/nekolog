from rich.table import Table
from rich.console import Console

console = Console()

def display_all_cats(cats_data):
            
    table = Table(title="All Cats")
    
    table.add_column("No.", style="cyan")
    table.add_column("Id", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Breed", style="magenta")
    table.add_column("Weight (Kg)", style="magenta")
    
    for i, cat in enumerate(cats_data, start=1):
        table.add_row(f"{i}", f"{cat.id}", f"{cat.name}", f"{cat.breed}", f"{cat.weight_kg}")

    console.print(table)

def display_cat_form_success(cat_name):
    # Buat nampilin pesan sukses yang gaya
    console.print(f"[bold green]Success![/] Kucing [cyan]{cat_name}[/] berhasil disimpan! 😺")