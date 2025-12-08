import sys
from models.cat import Cat
from models.expense import Expense

from view import main_view as mv
from view import cat_view
from view import expense_view


def main():
    while True:

        ans = mv.display_main_menu()

        if ans == "0":
            print("Terima kasih sudah menggunakan NekoLog! 😺👋")
            sys.exit() 
            
        elif ans == "1":
            while True: 
                cat_want = mv.display_cat_submenu()
                
                if cat_want == "0":
                    break 
                
                elif cat_want == "1": 
                    cat_view.add_new_cat_display()
                    
                elif cat_want == "2": 
                    data = Cat.get_all()
                    cat_view.display_all_cats(data)
                    
                elif cat_want == "3": 
                    cat_view.search_cat_display()
                    
                elif cat_want == "4": 
                    cat_view.update_cat_data_display()
                    
                elif cat_want == "5": 
                    cat_view.delete_cat_display()

        elif ans == "2":
            while True: 
                exp_want = mv.display_expense_submenu()
                
                if exp_want == "0": 
                    break
                
                elif exp_want == "1": 
                    expense_view.add_expense_display()
                    
                elif exp_want == "2":
                    data = Expense.get_leaderboard()
                    
                    expense_view.display_leaderboard(data)

if __name__ == "__main__":
    main()
    