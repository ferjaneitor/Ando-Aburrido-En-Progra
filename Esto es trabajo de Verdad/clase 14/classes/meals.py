from typing import List, Optional, Union
from drinks import Drinks  # Assuming this imports the Drinks class from the drinks module
from food import Food     # Assuming this imports the Food class from the food module

class Meals:
    def __init__(self, foodList: Optional[List[Food]] = None, drinkList: Optional[List[Drinks]] = None) -> None:
        self.foodList = foodList if foodList else []
        self.drinkList = drinkList if drinkList else []
    
    def addFood(self, foodName: str, quantity: int) -> None:
        food_item = next((food for food in self.foodList if food.getName() == foodName), None)
        if food_item:
            for _ in range(quantity):
                self.foodList.append(food_item)
        else:
            raise ValueError(f"Food item '{foodName}' not found in the meal list.")
    
    def addDrinks(self, drinkName: str, quantity: int) -> None:
        drink_item = next((drink for drink in self.drinkList if drink.getName() == drinkName), None)
        if drink_item:
            for _ in range(quantity):
                self.drinkList.append(drink_item)
        else:
            raise ValueError(f"Drink item '{drinkName}' not found in the drink list.")
    
    def removeFood(self, foodName: str, quantity: int) -> None:
        food_item = next((food for food in self.foodList if food.getName() == foodName), None)
        if food_item:
            count = self.foodList.count(food_item)
            if count >= quantity:
                for _ in range(quantity):
                    self.foodList.remove(food_item)
            else:
                raise ValueError(f"Not enough '{foodName}' in the meal to remove.")
        else:
            raise ValueError(f"Food item '{foodName}' not found in the meal list.")
    
    def removeDrinks(self, drinkName: str, quantity: int) -> None:
        drink_item = next((drink for drink in self.drinkList if drink.getName() == drinkName), None)
        if drink_item:
            count = self.drinkList.count(drink_item)
            if count >= quantity:
                for _ in range(quantity):
                    self.drinkList.remove(drink_item)
            else:
                raise ValueError(f"Not enough '{drinkName}' in the meal to remove.")
        else:
            raise ValueError(f"Drink item '{drinkName}' not found in the drink list.")
    
    def showAll(self) -> List[Union[Food, Drinks]]:
        """Show all food and drink items in the meal."""
        return self.foodList + self.drinkList
    
    def showFood(self) -> List[Food]:
        """Show only food items in the meal."""
        return self.foodList
    
    def showDrinks(self) -> List[Drinks]:
        """Show only drink items in the meal."""
        return self.drinkList
