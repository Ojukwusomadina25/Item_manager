def display_menu():
    print("\nItem manager")
    print("---------------")
    print("1. View all items")
    print("2. Add new items")
    print("3. Remove items")
    print("4. Edit items")
    print("5. Swap items")
    print("6. Exit")

def view_items(items):
    if not items:
        print("No items in the list.")
    else:
        print("Current items:")               
        for idx, item in enumerate(items):
            print(f"{idx}: {item}")

def add_items(items):
    new_items = input("Enter the items you want to add: ")
    items.append(new_items)
    print(f"{new_items} added successfully!")
    
def remove_items(items):
    view_items(items)
    try:
        index = int(input("Enter the index of the item to remove: "))
        removed = items.pop(index)
        print(f"'{removed}'removed successfully!")
    except ValueError:
        print("Invalid input. Try again.")
    except IndexError:
        print("That index doesn't exist. Please choose one from the list.")
    except ValueError:
        print("Please enter a valid number.")    
def edit_items(items):
     index = int(input("Enter the index of the item to edit: "))
     new_value = input("Enter the new item: ")
     items[index] = new_value
     print("Item updated.")

def swap_items(items):
    view_items(items)
    try:
        a = int(input("Enter the index of the first items to swap: "))
        b = int(input("Enter the index of the second item to swap: "))
        items [a], items [b] = items[b], items[a]
        print("Items swapped successfully!")
    except (ValueError, IndexError):
        print("Invalid indexex. Please Try again.")
# Main loop
items = ["Strawberries", "Spaghetti", "Banana", "Rice", "Orange", "Shopping", "Apple"]
while True:
    display_menu()    
    choice = input("Select an option 1–6: ")
    
    if choice == "1":
        view_items(items)
    elif choice == "2":
        add_items(items)
    elif choice == "3":
        remove_items(items)
    elif choice == "4":
        edit_items(items)
    elif choice == "5":
        swap_items(items)
    elif choice == "6":
        import time
        print("Exiting program. closing windows...")
        time.sleep(30/5)
        print("See you next time!")
        break
    else:
        print("Invalid choice. Please select a number from 1 to 6.")