import pytest
from unittest.mock import Mock

from Diplom_1.data import MockBurger
from Diplom_1.praktikum.bun import Bun
from Diplom_1.praktikum.burger import Burger
from Diplom_1.praktikum.ingredient import Ingredient


@pytest.fixture
def burger_fixture():
    # Создаем экземпляры необходимых объектов
    mock_bun = Mock(spec=Bun)
    mock_bun.get_name.return_value = MockBurger.BUN_NAME
    mock_bun.get_price.return_value = MockBurger.BUN_PRICE

    mock_ingredient = Mock(spec=Ingredient)
    mock_ingredient.get_price.return_value = MockBurger.INGREDIENT_PRICE
    mock_ingredient.get_name.return_value = MockBurger.INGREDIENT_NAME
    mock_ingredient.get_type.return_value = MockBurger.INGREDIENT_TYPE

    another_mock_ingredient = Mock(spec=Ingredient)
    another_mock_ingredient.get_price.return_value = MockBurger.ANOTHER_INGREDIENT_PRICE
    another_mock_ingredient.get_name.return_value = MockBurger.ANOTHER_INGREDIENT_NAME
    another_mock_ingredient.get_type.return_value = MockBurger.ANOTHER_INGREDIENT_TYPE

    # Инициализируем бургер с булочкой
    burger = Burger()
    burger.set_buns(mock_bun)

    return burger, mock_ingredient, another_mock_ingredient, mock_bun
