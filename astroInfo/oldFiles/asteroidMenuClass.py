## Asteroid Menu Class
## Programmer: Savannah Chappus
## Last Update: 2.18.2023


# GLOBAL VARIABLES
menu = {}

# method for building a menu
def build(numOptions):
    menuTitle = input("Menu title: ")
    menu[0] = menuTitle
    for item in range(numOptions):
        #menuChoice = input("Menu item " + str(item + 1) + ": ")
        menuChoice = input("Menu item " + str(item + 1) + ": ")
        menu[item + 1] = menuChoice

# method for displaying the menu
def display(menu):
    for num, item in menu.items():
        if num == 0:
            print(str(item))
        else:
            print(str(num) + ". " + str(item))
            
# method for editing the menu
            
# method for running the menu


# TESTING!!! - DELETE LATER
#buildMenu(4)
#displayMenu()
