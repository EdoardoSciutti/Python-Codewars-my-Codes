def cakes(recipe, available):
    return min(available.get(ingredient, 0) // amount for ingredient, amount in recipe.items())