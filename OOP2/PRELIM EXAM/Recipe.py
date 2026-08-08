class Recipe:
    # add different parts of the recipe
    def __init__(self, name, ingredients, steps, equipment, serves, cooking_time):
        self._rec_name = name
        self._rec_ingredients = ingredients
        self._rec_steps = steps
        self._rec_equipment = equipment
        self._rec_serves = serves
        self._rec_cooking_time = cooking_time

    def display_name(self):
        print("Recipe Name:", self._rec_name)

    def get_name(self):
        return self._rec_name

    def display_ingredients(self):
        print("Ingredients:", self._rec_ingredients)

    def display_steps(self):
        print("Instructions:", self._rec_steps)
    
    def display_serves(self):
        print("Yield:", self._rec_serves, "Servings")
    
    def display_equipment(self):
        print("Equipment:", self._rec_equipment)

    def display_category(self):
        print("Category : Unknown")

    def display_cooking_time(self):
        # FIX: Added self. to access instance attribute
        print("Cooking Time:", self._rec_cooking_time, "minutes")

    def display_recipe(self):
        print(f"======================== {self.get_name()} =========================")
        self.display_name()
        self.display_category()
        self.display_serves()
        self.display_cooking_time()
        self.display_equipment()
        self.display_ingredients()
        self.display_steps()


class Breakfast(Recipe):
    def display_category(self):
        print("Category: Breakfast")


class Lunch(Recipe):
    def display_category(self):
        print("Category: Lunch")


class Dinner(Recipe):
    def display_category(self):
        print("Category: Dinner")


class Snack(Recipe):
    def display_category(self):
        print("Category: Snack")


class Dessert(Recipe):
    def display_category(self):
        print("Category: Dessert")