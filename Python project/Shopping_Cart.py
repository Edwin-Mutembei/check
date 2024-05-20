#  import necessary functions
import os

cart = []

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

# function for adding items to cart
def addItem(item):
    clear_output()
    cart.append(item)
    print(f'{item} has been added successsfuly')

# function to remove items from the cart
def removeItem(item):
    clear_output()
    try:
        cart.remove(item)
        print(f'{item} has been removed successfully')
         
    except:
        print('Sorry, the chosen item does not exist. You can only remove the items which are in the cart')

# function to show items in the cart
def showItems():
    clear_output()
    if cart:
        print('Here is your cart')
        for item in cart:
            print(f'{item}')
    else:
        print('Your cart is empty')

# function to clear items from the cart
def clearItems():
    clear_output()
    cart.clear()
    print('All the items have been cleared from the cart successfully')

    # the function uses built_in clear method to clear all the items from the cart

# function that loops until the user quits
def main():
    done = False
    while not done:
        action = input('Kindly choose an action: quit/add/remove/show/clear: ').lower()
        # base case
        if action == 'quit':
            print('Thanks for using our program.')
            showItems()
            done = True

        elif action == 'add':
            item = input('What would you like to add? ').title()
            addItem(item)

        elif action == 'remove':
            showItems()
            item = input('What item would you like to remove? ').title()
            removeItem(item)

        elif action == 'show':
            showItems()

        elif action == 'clear':
            clearItems()

        else:
            print('Sorry, choose the correct option.')

main()


        
