from lib.recipe import Recipe 

def test_recipe_construct():
    recipe = Recipe(1, 'Pasta', 15, 4)
    assert recipe.id == 1
    assert recipe.name == 'Pasta'
    assert recipe.cooking_time == 15
    assert recipe.rating == 4

def test_recipe_format_nicely():
    recipe = Recipe(1, 'Pasta', 15, 4)
    assert str(recipe) == 'Recipe(1, Pasta, 15, 4)'

def test_recipe_are_equal():
    recipe_1 = Recipe(1, 'Pasta', 15, 4)
    recipe_2 = Recipe(1, 'Pasta', 15, 4)
    assert recipe_1 == recipe_2