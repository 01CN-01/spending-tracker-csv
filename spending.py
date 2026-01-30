import csv
from datetime import datetime
from error_handling import int_checker, input_checker, date_format_checker, round_checker

# Add Transactions
# Delete Transactions
# Spending Summaries
# View All Transactions
# Edit Transactions
# End Program

class Transaction:
    def __init__(self,transaction_id, date, category, amount, description):
        self.transaction_id = transaction_id
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description
        

class TransactionSystem:
    def __init__(self):
        self.transaction_system_list = []
# Checks to see if file exists. If it does add data too the list.        
        try:
            with open("spending_tracker_transaction.csv", "r") as csvfile:
                old_data = csv.DictReader(csvfile)
                self.transaction_system_list.extend(old_data)
        except:
            self.transaction_system_list = []
            
# Last ID number given too prevent using the same ID        
        try:
            with open("last_id_number.txt", "r") as txtfile:
                self.last_id_number = txtfile.read()
        except:
            self.last_id_number = 0
    
    def add_transaction(self):
        loop = int_checker("How many transactions would you like too add?: ")
        
        transaction_id = self.last_id_number
        transaction_id = int(transaction_id)
        for i in range(loop):
            transaction_id += 1
            print(f"TransactionID: {transaction_id}")
            date = date_format_checker("Date of transaction (DD/MM/YYYY):")
            category = input_checker("Category of transaction: ")
            amount = round_checker("Enter amount of transaction: £")
            description = input("Description of transaction (optional): ")
            
            transaction_data = Transaction(transaction_id, date, category, amount, description)
            
            print("------------ You have Successfully added ------------")
            print(f"TransactionID: {transaction_data.transaction_id}")
            print(f"Date: {transaction_data.date}")
            print(f"Category: {transaction_data.category}")
            print(f"Amount: {transaction_data.amount:.2f}")
            if transaction_data.description == "": # checks if user wrote anything
                print(f"Description: N/A")
            else:
                print(f"Description: {transaction_data.description}")
            print("-----------------------------------------------------")
            
            date_str = transaction_data.date #converts too string
            
            transaction_data_dict = {
                "TransactionID": transaction_data.transaction_id,
                "Date": date_str,
                "Category": transaction_data.category.lower(),
                "Amount": transaction_data.amount,
                "Description": transaction_data.description
            }
            self.transaction_system_list.append(transaction_data_dict)
# Writes Last transaction id number        
        with open("last_id_number.txt", "w") as txtfile:
            txtfile.write(str(transaction_id))
# Writes all transaction data into csv file.            
        with open("spending_tracker_transaction.csv", "w", newline = "") as csvfile:
            fieldnames = ["TransactionID", "Date", "Category", "Amount", "Description"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.transaction_system_list)
        
    def delete_transaction(self):
# Displays data to user
        for transaction_data in self.transaction_system_list:
            print("-" * 30)
            print("TransactionID: {transaction_data['TransactionID']}")
            print(f"Date: {transaction_data['Date']}")
            print(f"Category: {transaction_data['Category']}")
            print(f"Amount: {transaction_data['Amount']}")
            print(f"Description: {transaction_data['Description']}")
            print("-" * 30)
# Checks if users number is in range of the TransactionID data.        
        while True:    
            del_index_transaction_id = int_checker("Enter a TransctionID to delete: ")   
            if del_index_transaction_id > int(self.last_id_number) or del_index_transaction_id == 0:
                print("Invalid option. Choose by using TransactionID")
            else:
                # Check the index for the data
                counter = -1
                found = False
                for transaction_data in self.transaction_system_list:
                    counter += 1
                    if int(transaction_data["TransactionID"]) == del_index_transaction_id:
                        found = True
                        print(f"You have chosen too delete TransactionID ({del_index_transaction_id})")
                        break
                        
                    
# Not Found Data corresponding too the ID
            if found == False:
                print("Not Found.")
# Deletes Data                    
            else:
                del self.transaction_system_list[counter] # Delete it from list
# Puts new data in csv
                with open("spending_tracker_transaction.csv", "w", newline = "") as csvfile:
                    fieldnames = ["TransactionID", "Date", "Category", "Amount", "Description"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(self.transaction_system_list)
                print("Deleted")
                break
    
    def spending_summary_transaction(self):
        seen_category = []
# Puts all Categories in a List
        for transaction_data in self.transaction_system_list:
            category = transaction_data["Category"]
            if category not in seen_category:
                print(category)
                seen_category.append(category)
                
        if len(seen_category) > 0: # Checks to see if theres any categories
            while True:
                select_category = input_checker("Select a Category: ").lower()
                if select_category in seen_category: # Checks if its in list from the transaction data
                    for transaction_data in self.transaction_system_list:
                        if transaction_data["Category"] == select_category: # Filters Data
                            print("-" * 30)
                            print(f"TransactionID: {transaction_data['TransactionID']}")
                            print(f"Date: {transaction_data['Date']}")
                            print(f"Category: {transaction_data['Category']}")
                            print(f"Amount: {transaction_data['Amount']}")
                            print(f"Description: {transaction_data['Description']}")
                            print("-" * 30)
                    break
                else:
                    print("Category Not Found.")
        else:
            print("No data Found")
     
    def view_all_transaction(self):
        for transaction_data in self.transaction_system_list:
            print("-" * 30)
            print(f"TransactionID: {transaction_data['TransactionID']}")
            print(f"Date: {transaction_data['Date']}")
            print(f"Category: {transaction_data['Category']}")
            print(f"Amount: {transaction_data['Amount']}")
            print(f"Description: {transaction_data['Description']}")
            print("-" * 30)

    def edit_transaction(self):
# Displays data to user
        if len(self.transaction_system_list) > 0:
            for transaction_data in self.transaction_system_list:
                print("-" * 30)
                print(f"TransactionID: {transaction_data['TransactionID']}")
                print(f"Date: {transaction_data['Date']}")
                print(f"Category: {transaction_data['Category']}")
                print(f"Amount: {transaction_data['Amount']}")
                print(f"Description: {transaction_data['Description']}")
                print("-" * 30)
    # Checks if users number is in range of the TransactionID data.        
            while True:    
                edit_index_transaction_id = int_checker("Enter a TranscationID to edit: ")
                found = False   
                if edit_index_transaction_id > int(self.last_id_number) or edit_index_transaction_id == 0:
                    print("Invalid option. Choose by using TransactionID")
                else:
                    # Check the index for the data
                    counter = -1
                    for transaction_data in self.transaction_system_list:
                        counter += 1
                        if int(transaction_data["TransactionID"]) == edit_index_transaction_id:
                            found = True
                            print(f"You have chosen too edit TransactionID ({edit_index_transaction_id})")
    # Edit data from list   
                            edit_part = input_checker("What part of the data do you want to edit? (Date, Category, Amount, Description): ").lower()
                            # Date Selection
                            if edit_part == "date":
                                transaction_id_edit = self.transaction_system_list[counter]
                                print(f"Current Date: {transaction_id_edit['Date']}")
                                change = date_format_checker("What do you want to change the date to? (DD/MM/YYYY): ")
                                transaction_id_edit['Date'] = change #Overwrites it
                            # Category Selection
                            elif edit_part == "category":
                                transaction_id_edit = self.transaction_system_list[counter]
                                print(f"Current Category: {transaction_id_edit['Category']}")
                                change = input_checker("What do you want to change the category to?: ")
                                transaction_id_edit['Category'] = change #Overwrites it
                            # Amount Selection
                            elif edit_part == "amount":
                                transaction_id_edit = self.transaction_system_list[counter]
                                print(f"Current Amount: £{float(transaction_id_edit['Amount']):.2f}")
                                change = round_checker("What do you want to change the amount to?: £")
                                transaction_id_edit['Amount'] = change #Overwrites it
                            # Description Selection
                            elif edit_part == "description":
                                transaction_id_edit = self.transaction_system_list[counter]
                                print(f"Current Description: {transaction_id_edit['Description']}")
                                change = input("What do you want to change the description to?: ")
                                transaction_id_edit['Description'] = change #Overwrites it 
                            else:
                                print("Invalid Option (Date, Category, Amount, Description)") 
                                break                                                    
            
                if found:        
                    with open("spending_tracker_transaction.csv", "w", newline="") as csvfile:
                        fieldnames = ["TransactionID","Date", "Category", "Amount", "Description"]
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(self.transaction_system_list)
                        break
                else:
                    print(f"TransactionID:{edit_index_transaction_id} was not found.")
        else:
            print("No Data Found")
                    