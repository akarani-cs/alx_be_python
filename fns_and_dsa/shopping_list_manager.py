
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")





shopping_list=[]

def add_item(item):
    item =input("Enter the item to add: ")
    shopping_list.append(item)
    print("Item added, your shopping list includes:", shopping_list)

def remove_item(item):
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print("Item removed, your shopping list includes:", shopping_list)
    else:
        if item not in shopping_list:
            print("item not found in shopping list")

def view_list():
    if shopping_list:
        print("Your shopping list includes: ", shopping_list)
    else:
        print("Kindly add items to your shopping list")
      
