from lib.RecipeRepository import RecipeRepository
from lib.recipe import Recipe
def test_get_all_record(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipes = repository.all()

    assert recipes == [
        Recipe(1,'Pasta', 15, 4),
        Recipe(2,'Burger', 10, 3),
        Recipe(3,'Pizza', 30, 4),
        Recipe(4,'Bread', 45, 2),
        Recipe(5,'Fries', 10, 3)
    ]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipe = repository.find(2)
    assert recipe == Recipe(2,'Burger', 10, 3)

