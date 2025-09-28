def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
                
        elif choice == '2':
            if not shopping_list:
                print("The list is currently empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ").strip()
            
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            else:
                print(f"Item '{item_to_remove}' not found in the list.")
                
        elif choice == '3':
            print("\nCurrent Shopping List:")
            if shopping_list:
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("The shopping list is empty.")
                
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()