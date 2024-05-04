import pytest
from typing import List
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient


class TestDataBase:

    @pytest.mark.parametrize('price, id', [[100, 0], [200, 1], [300, 2]])
    def test_get_price_on_available_buns(self, price: int, id: int):
        database: Database = Database()
        buns: List[Bun] = database.available_buns()
        assert price == buns[id].get_price()

    @pytest.mark.parametrize('bun, id', [["black bun", 0], ["white bun", 1], ["red bun", 2]])
    def test_get_buns_on_available_buns(self, bun: str, id: int):
        database: Database = Database()
        buns: List[Bun] = database.available_buns()
        assert bun == buns[id].get_name()

    @pytest.mark.parametrize('ingredient, id', [
        ["hot sauce", 0],
        ["sour cream", 1],
        ["chili sauce", 2],
        ["cutlet", 3],
        ["dinosaur", 4],
        ["sausage", 5],
    ])
    def test_get_bun_available_buns(self, ingredient: str, id: int):
        database: Database = Database()
        ingredients: List[Ingredient] = database.available_ingredients()
        assert ingredient == ingredients[id].get_name()

    @pytest.mark.parametrize('price, id', [
        [100, 0],
        [200, 1],
        [300, 2],
        [100, 3],
        [200, 4],
        [300, 5],
    ])
    def test_get_bun_available_buns(self, price:int, id: int):
        database: Database = Database()
        ingredients: List[Ingredient] = database.available_ingredients()
        assert price == ingredients[id].get_price()


