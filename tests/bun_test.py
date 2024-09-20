import pytest

from Diplom_1.data import BunData
from Diplom_1.praktikum.bun import Bun


# Тестирование класса Bun
class TestBun:
    @pytest.mark.parametrize("name, price", BunData.BUN_DATA)
    def test_bun_initialization(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name and bun.get_price() == price
