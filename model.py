import requests

API_KEY = "634dbb23e9ca4079a230c3d23212c8ff"

def suggest_recipes(available_ingredients):
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={available_ingredients}&number=5&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    recipes = []
    for recipe in data:
        recipes.append({
            "title": recipe["title"],
            "image": recipe["image"]
        })

    return recipes
