class BunData:
    BUN_DATA = [
        ("Марсианка", 257),
        ("Луна", 155),
        ("Центр Вселенной", 1000)
    ]

class IngredientData:
    INGREDIENT_DATA = [
        ("SAUCE", "Вулканическая пыль", 355),
        ("FILLING", "Филе единорога", 1557)
    ]

class MockBurger:
    BUN_NAME = "Марсианка"
    BUN_PRICE = 257
    INGREDIENT_PRICE  = 424
    INGREDIENT_NAME = "Биокотлета из марсианской Магнолии"
    INGREDIENT_TYPE = "FILLING"
    ANOTHER_INGREDIENT_PRICE = 15
    ANOTHER_INGREDIENT_NAME = "Соус традиционный галактический"
    ANOTHER_INGREDIENT_TYPE = "SAUCE"
    EXPECTED_RECEIPT = '(==== Марсианка ====)\n= filling Биокотлета из марсианской Магнолии =\n(==== Марсианка ====)\n\nPrice: 938'