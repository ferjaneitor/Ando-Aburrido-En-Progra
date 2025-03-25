from datetime import datetime, timedelta
import re
from meals import Meals
from food import Food  # Import Food class
from drinks import Drinks  # Import Drinks class

class Reservation:
    
    def __init__(self, reservation_name: str, reservation_date: str, reservation_time: str, reservation_duration: str, quantity_of_persons: int, meal: Meals) -> None:
        self.name = reservation_name
        self.date = reservation_date
        self.time = reservation_time
        self.length = reservation_duration
        self.quantity_of_persons = quantity_of_persons
        self.meal = meal
    
    def validate_date(self, date: str) -> str:
        """Validates the format of the reservation date."""
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            raise ValueError("Invalid date format. It should be YYYY-MM-DD.")
    
    def validate_time(self, time: str) -> str:
        """Validates the format of the reservation time."""
        if re.match(r'^\d{2}:\d{2}$', time):
            return time
        else:
            raise ValueError("Invalid time format. It should be HH:MM.")
    
    def validate_length(self, length: str) -> tuple:
        """Validates and converts reservation duration into hours and minutes."""
        try:
            hours, minutes = map(int, length.split(':'))
            if hours < 0 or minutes < 0 or minutes >= 60:
                raise ValueError("Hours and minutes must be positive, and minutes should be less than 60.")
            return hours, minutes
        except ValueError:
            raise ValueError("Duration must be in the format 'hours:minutes' with valid numeric values.")
    
    def validate_quantity(self, quantity: int) -> int:
        """Validates that the quantity of persons is a positive integer."""
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("The number of persons must be a positive integer.")
        return quantity

    @property
    def date(self) -> str:
        """Gets the reservation date."""
        return self._date
    
    @date.setter
    def date(self, value: str):
        """Sets the reservation date after validating it."""
        self._date = self.validate_date(value)
    
    @property
    def time(self) -> str:
        """Gets the reservation time."""
        return self._time
    
    @time.setter
    def time(self, value: str):
        """Sets the reservation time after validating it."""
        self._time = self.validate_time(value)
    
    @property
    def length(self) -> str:
        """Gets the reservation duration in 'X hours Y minutes' format."""
        return f"{self.length_hours} hours {self.length_minutes} minutes"
    
    @length.setter
    def length(self, value: str):
        """Sets the reservation duration from given hours and minutes."""
        self.length_hours, self.length_minutes = self.validate_length(value)
    
    @property
    def name(self) -> str:
        """Gets the reservation name."""
        return self._name
    
    @name.setter
    def name(self, value: str):
        """Sets a new reservation name."""
        self._name = value
    
    @property
    def quantity_of_persons(self) -> int:
        """Gets the number of persons for the reservation."""
        return self._quantity_of_persons
    
    @quantity_of_persons.setter
    def quantity_of_persons(self, value: int):
        """Sets the number of persons after validating it."""
        self._quantity_of_persons = self.validate_quantity(value)
    
    @property
    def meal(self) -> int:
        ...
    
    @meal.setter
    def meal  (self,):
        ...
    
    def end_time(self) -> str:
        """Calculates the end time of the reservation."""
        try:
            start_datetime = datetime.strptime(f"{self.date} {self.time}", "%Y-%m-%d %H:%M")
            end_datetime = start_datetime + timedelta(hours=self.length_hours, minutes=self.length_minutes)
            return end_datetime.strftime('%H:%M')
        except ValueError:
            raise ValueError("Invalid start date or time.")
    
    def meal_summary(self) -> str:
        """Returns a detailed summary of the meal associated with the reservation."""
        meal_summary = self.meal.showAll()  # Get all food and drink items
        summary = []
        for item in meal_summary:
            if isinstance(item, Food):
                summary.append(f"Food: {item.summary}")
            elif isinstance(item, Drinks):
                summary.append(f"Drink: {item.summary}")
        return "\n".join(summary)
    
    def to_dict(self) -> dict:
        """Converts the reservation to a dictionary for storage."""
        return {
            'name': self.name,
            'date': self.date,
            'time': self.time,
            'length_hours': self.length_hours,
            'length_minutes': self.length_minutes,
            'quantity_of_persons': self.quantity_of_persons,
        }

    def __str__(self) -> str:
        """Returns a string representation of the reservation."""
        meal_details = self.meal_summary()
        return f"Reservation for {self.name} on {self.date} at {self.time}.\n" \
               f"Duration: {self.length}\n" \
               f"Number of Persons: {self.quantity_of_persons}\n" \
               f"Meal Details:\n{meal_details}"

