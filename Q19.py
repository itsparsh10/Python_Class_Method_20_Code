# Design a recipe management system with classes for recipes, ingredients, and
# users. Implement methods for adding recipes, searching by ingredients
class Ingredient:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Ingredient: {self.name}")

class Recipe:
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

    def display_recipe(self):
        print(f"Recipe name: {self.title}")
        print("Recipe Ingredients:")
        for ingredient in self.ingredients:
            ingredient.display_info()
        print(f"Instructions: {self.instructions}")

class User:
    def __init__(self, username):
        self.username = username
        self.saved_recipes = []

class RecipeManagementSystem:
    def __init__(self):
        self.recipes = []
        self.users = []

    def add_user(self, username):
        user = User(username)
        self.users.append(user)
        return user

    def add_recipe(self, title, ingredients, instructions):
        recipe = Recipe(title, ingredients, instructions)
        self.recipes.append(recipe)
        return recipe

    def display_all_recipes(self):
        print("All Recipes:")
        for recipe in self.recipes:
            recipe.display_recipe()
            print()

    def search_by_ingredient(self, ingredient_name):
        matching_recipes = []
        for recipe in self.recipes:
            if any(ingredient.name.lower() == ingredient_name.lower() for ingredient in recipe.ingredients):
                matching_recipes.append(recipe)
        return matching_recipes

def main():
    recipe_system = RecipeManagementSystem()

    a = input("Enter your name: ")
    user1 = recipe_system.add_user(a)
    print("Welcome to Recipe Management System")

    while True:
        print("1. Add recipes")
        print("2. View recipes by ingredient")
        print("3. View all recipes")
        print("4. Exit")
        b = int(input("Enter your choice: "))
        d=[]
        if b == 1:
            # Add recipes
            a=input("Enter recipe name: ")
            b=input("Enter instructions: ")
            while True:
                c=input("Enter ingredient name(Done to exit): ")
                if c.lower()=="done":
                    break
                else:
                    d.append(Ingredient(c))
            recipe1 = recipe_system.add_recipe(a,d,b)
            # Users save recipes
            user1.saved_recipes.append(recipe1)
        elif b == 2:
            # Search recipes by ingredient
            b = input("Enter ingredient to search: ")
            ingredient_to_search = b
            matching_recipes = recipe_system.search_by_ingredient(ingredient_to_search)

            # Display results
            print(f"Recipes containing {ingredient_to_search}:\n")
            for recipe in matching_recipes:
                recipe.display_recipe()
                print()
        elif b == 3:
            # View all recipes
            recipe_system.display_all_recipes()
        elif b == 4:
            print("Thank You! Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()