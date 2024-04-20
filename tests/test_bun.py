from praktikum.bun import Bun


class TestBun:

    def test_get_name_of_bun(self):
        buns = Bun(name='Фиолетовая булочка', price=100)
        assert buns.name == 'Фиолетовая булочка'

    def test_get_price_of_bun(self):
        buns = Bun(name='Фиолетовая булочка', price=100)
        assert buns.price == 100
