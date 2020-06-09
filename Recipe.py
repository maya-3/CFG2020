#https://spoonacular.com/food-api/docs
#https://spoonacular.com/food-api/docs#Search-Recipes-by-Ingredients

import requests

chosen_ing = input("What ingredients do you have? ")

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

querystring = {"number": "5", "ranking": "1", "ignorePantry": "false", "ingredients": chosen_ing}

headers={'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "ab9a39777bmsh5823444553992e1p129695jsn15a6699651cb"
    }

response = requests.request("GET", url, headers=headers, params=querystring).text
print(response)

with open('recipes.txt', 'w+') as new_file:
    recipes = response
    new_file.write(recipes)
print("Suggested recipes were saved as recipes.txt file for your convenience")

chosen_id = input("Which recipe would you like to see? Please input recipe ID: ")

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{}/analyzedInstructions".format(chosen_id)

querystring = {"stepBreakdown":"true"}

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "ab9a39777bmsh5823444553992e1p129695jsn15a6699651cb"
    }

response2 = requests.request("GET", url, headers=headers).text

print("The recipe is being saved to recipes.txt file." + '\n'"The details will be displayed in the terminal shortly.")
with open('recipes.txt', 'r') as recipes_file:
    recipes = recipes_file.read()
recipes = recipes + '\n' + response2
with open('recipes.txt', 'w+') as recipes_file:
    recipes_file.write(recipes)
print(response2)









