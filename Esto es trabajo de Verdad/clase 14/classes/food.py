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

class Food:
    def __init__(self, foodname: str, weightGrams: int, extraInfo: Optional[str], 
                 description: str, ingredientsList: List[str], price: int) -> None:
        validate_non_empty_string(foodname, "Food name")
        validate_positive_integer(weightGrams, "Weight")
        validate_non_empty_string(description, "Description")
        validate_positive_integer(price, "Price")
        validate_non_empty_list(ingredientsList, "Ingredients list")
        if extraInfo is not None:
            validate_non_empty_string(extraInfo, "Extra info")
        
        self.foodname = foodname
        self.weightGrams = weightGrams
        self.extraInfo = extraInfo
        self.description = description
        self.ingredientsList = ingredientsList.copy()
        self.price = Decimal(price)

        self._summary_cache = None  # Cache summary for efficiency

    def getName(self) -> str:
        return self.foodname
    
    def getWeight(self) -> int:
        return self.weightGrams
    
    def getExtraInfo(self) -> str:
        return self.extraInfo or "No extra information"
    
    def getDescription(self) -> str:
        return self.description

    def getIngredients(self) -> str:
        return ', '.join(self.ingredientsList)
    
    def getPrice(self) -> Decimal:
        return self.price
    
    def applyDiscount(self, percentage: float) -> None:
        if not (0 < percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        discount_amount = (self.price * Decimal(percentage)) / Decimal(100)
        self.price -= discount_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

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
            extra_info = self.getExtraInfo()
            self._summary_cache = f"{self.foodname} ({self.weightGrams}g)\n" \
                                  f"Description: {self.description}\n" \
                                  f"Ingredients: {ingredients}\n" \
                                  f"Price: {self.formatPrice()}\n" \
                                  f"Extra Info: {extra_info}"
        return self._summary_cache

    def __str__(self, max_ingredients: int = 5) -> str:
        ingredients = ', '.join(self.ingredientsList[:max_ingredients])
        if len(self.ingredientsList) > max_ingredients:
            ingredients += ', ...'
        return f"{self.foodname} ({self.weightGrams}g)\n" \
               f"Description: {self.description}\n" \
               f"Ingredients: {ingredients}\n" \
               f"Price: {self.formatPrice()}\n" \
               f"Extra Info: {self.extraInfo or 'No additional info'}"

    def __repr__(self):
        return f"Food(foodname={self.foodname}, weightGrams={self.weightGrams}, " \
               f"price={self.price}, ingredientsList={self.ingredientsList})"
