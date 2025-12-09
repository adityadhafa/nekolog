from models.cat import Cat

def test_create_cat():
    momo = Cat(name="Momo", breed="Persian", weight_kg=4.5)
    momo.save()

    assert momo.id is not None
    assert momo.name == "Momo"

def test_search_cat():
    Cat(name="Garfield", breed="Orange", weight_kg=6.0).save()
    Cat(name="Tom", breed="Grey", weight_kg=4.0).save()

    results = Cat.search_cat("Gar")

    assert len(results) == 1
    assert results[0].name == "Garfield"

def test_update_cat():
    oyen = Cat(name="Oyen", breed="Kampung", weight_kg=3.0)
    oyen.save()
    
    oyen.update(name="Oyen King", breed="Kampung", weight_kg=5.0)
    
    updated_cat = Cat.get_by_id(oyen.id)
    
    assert updated_cat.weight_kg == 5.0
    assert updated_cat.name == "Oyen King"