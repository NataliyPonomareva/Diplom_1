from unittest.mock import Mock

from Diplom_1.data import MockBurger
from Diplom_1.praktikum.bun import Bun
from Diplom_1.praktikum.ingredient import Ingredient


class TestBurger:

    def test_set_bun(self, burger_fixture):
        burger, _, _, _  = burger_fixture

        # Установите макет булочки
        new_bun = Mock(spec=Bun)
        burger.set_buns(new_bun)

        # Проверьте, была ли булочка установлена
        assert burger.bun == new_bun


    def test_add_ingredient(self, burger_fixture):
        burger, mock_ingredient, _, _  = burger_fixture

        # Добавьте ингредиент в бургер
        burger.add_ingredient(mock_ingredient)

        # Проверьте, добавился ли ингредиент
        assert mock_ingredient in burger.ingredients


    def test_remove_ingredient(self, burger_fixture):
        burger, mock_ingredient, another_mock_ingredient, _  = burger_fixture

        # Добавляем ингредиенты в бургер
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(another_mock_ingredient)

        # Удаляем первый ингредиент
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1 and burger.ingredients[0].get_name() == MockBurger.ANOTHER_INGREDIENT_NAME

    def test_move_ingredient(self, burger_fixture):
        burger, mock_ingredient, another_mock_ingredient, _  = burger_fixture
        mock_ingredient = Mock(spec=Ingredient)
        another_mock_ingredient = Mock(spec=Ingredient)

        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(another_mock_ingredient)

        burger.move_ingredient(0, 1)  # Перемещаем первый ингредиент на вторую позицию

        assert burger.ingredients[0] == another_mock_ingredient and burger.ingredients[1] == mock_ingredient

    def test_get_price(self, burger_fixture):
        burger, mock_ingredient, _, mock_bun = burger_fixture
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        price = burger.get_price()
        # Цена должна быть: 2 * цена булочки + цена ингредиента
        assert price == 257 * 2 + 424

    def test_get_receipt(self, burger_fixture):
        burger, mock_ingredient, _, mock_bun = burger_fixture
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_receipt = MockBurger.EXPECTED_RECEIPT
        assert burger.get_receipt() == expected_receipt
