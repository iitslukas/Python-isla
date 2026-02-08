import requests

url = "https://boozeapi.com/api/v1/cocktails"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if isinstance(data, dict) and "data" in data:
        cocktails = data["data"]
    else:
        cocktails = data

    vodka_count = 0
    gin_count = 0
    rum_count = 0

    for drink in cocktails:
        ingredients = drink.get("ingredients", [])
        ingredient_names = [ing.get("name", "").lower() for ing in ingredients if isinstance(ing, dict)]

        if any("vodka" in name for name in ingredient_names):
            vodka_count += 1

        if any("gin" in name for name in ingredient_names):
            gin_count += 1

        if any("rum" in name for name in ingredient_names):
            rum_count += 1

    print("Drink counts:")
    print("Vodka drinks:", vodka_count)
    print("Gin drinks:", gin_count)
    print("Rum drinks:", rum_count)

else:
    print("Error", response.status_code, response.text)
