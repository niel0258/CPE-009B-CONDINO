from Reader import jsonFileEditor,clear_screen,multiple_line_input
from SimpleMenu import SimpleMenu
from Recipe import Recipe,Breakfast,Dinner,Lunch,Snack,Dessert
from time import sleep

class RecipeOrganizer:
    category_names = ["Breakfast","Lunch","Snacks","Dinner","Dessert"]

    def __init__(self):
        self.Breakfast = []
        self.Dinner = []
        self.Lunch = []
        self.Snack = []
        self.Dessert = []

    def _print_recipe(self,list_category,index):
        print("----------------------- RECIPE -----------------------------\n")
        print()
        list_category[index].display_recipe()
        print('------------------------------------------------------------')
        input("Press Enter to continue....")


    def _view_specific_recipe(self,chosen_list,choice):
        if not chosen_list:
            print("There is no recipe in this category")
            print("\n Please wait...")
            sleep(3)
            return
        
        #create list of names
        names_list = []
        for i in range(len(chosen_list)):
            names_list.append(chosen_list[i].get_name())
        
        chosen_recipe = SimpleMenu(names_list,"============================ Choose Recipe: =============================").navigate_menu()

        self._print_recipe(chosen_list,chosen_recipe)
    
    def _view_category_list(self,choice):
        clear_screen()

        chosen_list = []

        match choice:
            case 0:
                chosen_list = self.Breakfast
            case 1:
                chosen_list = self.Lunch
            case 2:
                chosen_list = self.Snack
            case 3:
                chosen_list = self.Dinner
            case 4:
                chosen_list = self.Dessert

        self._view_specific_recipe(chosen_list,choice)

    #1.Bf, 2.Lun, 3. Sna, 4. Din, 5.Des
    def _choose_categ(self):
        categ_menu = SimpleMenu(RecipeOrganizer.category_names,"CATEGORIES")
        
        choice = categ_menu.navigate_menu()

        return choice
        
    def input_recipe(self):
        clear_screen()

        recipe_name = input("Input recipe name: ")
        recipe_ing = multiple_line_input("Input ingredients")
        recipe_steps = multiple_line_input("Input the instructions")
        recipe_equipment = input("Input equipments: ")
        recipe_servings = input("Input serving yield: ")
        recipe_time = input("Input the time it takes to cook: ")

        recipe = 0

        #choose category
        choice = self._choose_categ()

        match choice:
            case 0:
                recipe = Breakfast(recipe_name,recipe_ing,recipe_steps,recipe_equipment,recipe_servings,recipe_time)
                self.Breakfast.append(recipe)
            case 1:
                recipe = Lunch(recipe_name,recipe_ing,recipe_steps,recipe_equipment,recipe_servings,recipe_time)
                self.Lunch.append(recipe)
            case 2:
                recipe = Snack(recipe_name,recipe_ing,recipe_steps,recipe_equipment,recipe_servings,recipe_time)
                self.Snack.append(recipe)
            case 3:
                recipe = Dinner(recipe_name,recipe_ing,recipe_steps,recipe_equipment,recipe_servings,recipe_time)
                self.Dinner.append(recipe)
            case 4:
                recipe = Dessert(recipe_name,recipe_ing,recipe_steps,recipe_equipment,recipe_servings,recipe_time)
                self.Dessert.append(recipe)

    #displays the recipes in this recipe handbook
    def display_handbook(self):
        #check if there is nothing in the menu
        if not (self.Breakfast or self.Dessert or self.Lunch or self.Dinner or self.Snack):
            print("Nothing is in the handbook\nPress wait...")
            sleep(3)
            return 

        choice = self._choose_categ()
        self._view_category_list(choice)
    
    def export_recipe(self):
        #turn each object into a dictionary
        #store these dictionaries in one object
        pass