from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_get_ingredient_type(self):
        ingredient = Ingredient(name='Сальса', price=1000, ingredient_type='Соус')
        assert ingredient.get_type() == 'Соус'

    def test_get_ingredient_name(self):
        ingredient = Ingredient(name='Сальса', price=1000, ingredient_type='Соус')
        assert ingredient.get_name() == 'Сальса'

    def test_get_ingredient_price(self):
        ingredient = Ingredient(name='Сальса', price=1000, ingredient_type='Соус')
        assert ingredient.get_price() == 1000