from decimal import Decimal, ROUND_HALF_UP
from typing import List, Optional

# Helper function for validation
def validate_non_empty_string(value: str, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string.")

def validate_positive_integer(value: int, field_name: str) -> None:
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{field_name} must be a positive integer.")

def validate_non_empty_list(value: List[str], field_name: str) -> None:
    if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
        raise ValueError(f"{field_name} must be a non-empty list of non-empty strings.")

class Drinks:
    def __init__(self, drinkname: str, sizeMiliLiters: int, price: int,
                description: Optional[str] = "", ingredientsList: Optional[List[str]] = None) -> None:
        if ingredientsList is None:
            ingredientsList = []
        
        validate_non_empty_string(drinkname, "Drink name")
        validate_positive_integer(sizeMiliLiters, "Size")
        validate_non_empty_string(description, "Description")
        validate_positive_integer(price, "Price")
        validate_non_empty_list(ingredientsList, "Ingredients list")

        self.drinkname = drinkname
        self.sizeMiliLiters = sizeMiliLiters
        self.description = description
        self.ingredientsList = ingredientsList
        self.price = Decimal(price)

        self._summary_cache = None  # Cache summary for efficiency

    def getName(self) -> str:
        return self.drinkname
    
    def getSize(self) -> int:
        return self.sizeMiliLiters
    
    def getDescription(self) -> str:
        return self.description
    
    def getIngredients(self) -> str:
        return ', '.join(self.ingredientsList)
    
    def getPrice(self) -> Decimal:
        return self.price
    
    def applyDiscount(self, percentage: float) -> None:
        if not (0 < percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        discount_amount = self.price * (Decimal(percentage) / Decimal(100))
        new_price = self.price - discount_amount
        if new_price < Decimal(1):
            raise ValueError("Discount results in a price less than $0.01.")
        self.price = new_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        self._clear_summary_cache()

    def getPriceWithTax(self, tax_rate: float) -> Decimal:
        if tax_rate < 0:
            raise ValueError("Tax rate cannot be negative.")
        price_with_tax = self.price * (Decimal(1) + Decimal(tax_rate) / Decimal(100))
        return price_with_tax.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def formatPrice(self) -> str:
        return f"${self.price / Decimal(100):.2f}"

    def _clear_summary_cache(self) -> None:
        self._summary_cache = None  # Clear cache when attributes change

    @property
    def summary(self) -> str:
        if self._summary_cache is None:
            ingredients = self.getIngredients()
            description = self.description or "No description available."
            self._summary_cache = f"{self.drinkname} ({self.sizeMiliLiters}ml)\n" \
                                  f"Description: {description}\n" \
                                  f"Ingredients: {ingredients}\n" \
                                  f"Price: {self.formatPrice()}"
        return self._summary_cache

    def __str__(self, max_ingredients: int = 5) -> str:
        ingredients = ', '.join(self.ingredientsList[:max_ingredients])
        if len(self.ingredientsList) > max_ingredients:
            ingredients += ', ...'
        return f"{self.drinkname} ({self.sizeMiliLiters}ml)\n" \
               f"Description: {self.description}\n" \
               f"Ingredients: {ingredients}\n" \
               f"Price: {self.formatPrice()}"

    def __repr__(self):
        return f"Drinks(drinkname={self.drinkname}, sizeMiliLiters={self.sizeMiliLiters}, " \
               f"price={self.getPrice()}, ingredientsList={self.ingredientsList})"
