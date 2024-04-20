from typing import List

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_get_receipt(self):
        database: Database = Database()
        burger: Burger = Burger()
        buns: List[Bun] = database.available_buns()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.set_buns(buns[0])
        burger.add_ingredient(ingredients[1])
        burger.add_ingredient(ingredients[2])
        assert burger.get_receipt() == '(==== black bun ====)\n= sauce sour cream =\n= sauce chili sauce =\n(==== black bun ====)\n\nPrice: 700'

    def test_get_change_ingredient(self):
        database: Database = Database()
        burger: Burger = Burger()
        buns: List[Bun] = database.available_buns()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.set_buns(buns[0])
        burger.add_ingredient(ingredients[1])
        burger.add_ingredient(ingredients[2])
        burger.move_ingredient(1, 0)
        assert burger.get_receipt() == '(==== black bun ====)\n= sauce chili sauce =\n= sauce sour cream =\n(==== black bun ====)\n\nPrice: 700'

    def test_remove_ingredient(self):
        database: Database = Database()
        burger: Burger = Burger()
        buns: List[Bun] = database.available_buns()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.set_buns(buns[0])
        burger.add_ingredient(ingredients[1])
        burger.add_ingredient(ingredients[2])
        burger.remove_ingredient(1)
        assert burger.get_receipt() == '(==== black bun ====)\n= sauce sour cream =\n(==== black bun ====)\n\nPrice: 400'

    def test_get_price(self):
        database: Database = Database()
        burger: Burger = Burger()
        buns: List[Bun] = database.available_buns()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.set_buns(buns[0])
        burger.add_ingredient(ingredients[1])
        burger.add_ingredient(ingredients[2])
        assert burger.get_price() == 700