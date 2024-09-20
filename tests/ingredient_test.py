import pytest

from Diplom_1.data import IngredientData
from Diplom_1.praktikum.ingredient import Ingredient


# Тестирование класса Bun
class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price",  IngredientData.INGREDIENT_DATA)
    def test_ingredient_initialization(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type and ingredient.get_name() == name and ingredient.get_price() == price
