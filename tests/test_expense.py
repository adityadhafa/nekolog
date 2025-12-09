from models.expense import Expense
from models.cat import Cat

def test_save_expense():
    momo = Cat(name="Momo", breed="Persia", weight_kg=4.5)
    momo.save()

    jajan = Expense(
        amount=50000, 
        category="Food", 
        date="2023-10-01", 
        description="Beli Whiskas", 
        cat_id=momo.id
    )
    jajan.save()

    assert jajan.id is not None
    assert jajan.amount == 50000

def test_get_total_per_cat():
    oyen = Cat(name="Oyen", breed="Kampung", weight_kg=3.5)
    oyen.save()

    Expense(amount=10000, category="Food", date="2023-10-01", description="Snack A", cat_id=oyen.id).save()
    Expense(amount=20000, category="Toy", date="2023-10-02", description="Mainan B", cat_id=oyen.id).save()

    total = Expense.get_total_by_cat_id(oyen.id)
    assert total == 30000

def test_leaderboard():
    sultan = Cat(name="King", breed="Maine Coon", weight_kg=8.0)
    sultan.save()
    Expense(amount=1000000, category="Food", date="2023-10-01", description="Steak", cat_id=sultan.id).save()
    
    rakyat = Cat(name="Jelata", breed="Kampung", weight_kg=3.0)
    rakyat.save()
    Expense(amount=5000, category="Food", date="2023-10-01", description="Pindang", cat_id=rakyat.id).save()
    
    ranking = Expense.get_leaderboard()

    assert ranking[0][0] == "King"        
    assert ranking[0][1] == 1000000      

    assert ranking[1][0] == "Jelata"
    assert ranking[1][1] == 5000