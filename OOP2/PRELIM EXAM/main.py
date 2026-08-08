from Recipe import Recipe
from RecipeOrganizer import RecipeOrganizer
from SimpleMenu import SimpleMenu

menu_choices = ["Display Handbook", "Add Recipe", "Exit"]
recipe_menu = SimpleMenu(menu_choices, "Recipe Organizer")
recipe_organizer = RecipeOrganizer()
recipe_organizer.import_recipe()

#ABSTRACTION the function/method definition is hiddent in different modules
while True:
    choice = recipe_menu.navigate_menu()

    if choice == 0:
        recipe_organizer.display_handbook()
    elif choice == 1:
        recipe_organizer.input_recipe()
    else:
        print("Exiting...")
        recipe_organizer.export_recipe()
        break  # Exit the loop when option 2 (Exit) is selected