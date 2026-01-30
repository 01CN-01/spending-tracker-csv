from spending import TransactionSystem
from error_handling import int_checker

def menu():

    while True:
        transaction_system = TransactionSystem()
        print("================= Menu =================")
        print("|        1) Add Transaction            |")
        print("|       2) Delete Transaction          |")
        print("|       3) Spending Summaries          |")
        print("|      4) View All Transactions        |")
        print("|        5) Edit Transaction           |")
        print("|           6) End Program             |")
        print("========================================")
        
        menu_choice = int_checker("Choose an option: ")
        if menu_choice == 1:
            transaction_system.add_transaction()
        elif menu_choice == 2:
            transaction_system.delete_transaction()
        elif menu_choice == 3:
            transaction_system.spending_summary_transaction()
        elif menu_choice == 4:
            transaction_system.view_all_transaction()
        elif menu_choice == 5:
            transaction_system.edit_transaction()
        elif menu_choice == 6:
            print("Program Ended")
        else:
            print("Invalid Option Choice.")


menu()